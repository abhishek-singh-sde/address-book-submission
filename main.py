#Note: If you want to check via Postman, just supply the required request with body/query containing key value pairs as defined in model

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

#We will use this for calculating distance bewtween 2 points
import haversine as hs


#Defining our Address model
class Address(BaseModel):
    address: str
    latitude: float
    longitude: float


#We are creating the address table with 4 columns
import sqlite3
conn = sqlite3.connect('master_address_table.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS addresses
             (id INTEGER PRIMARY KEY, address TEXT, latitude REAL, longitude REAL)''')
conn.commit()


#We want to keep a store of the respective logs, hence mode is append, else use write for every fresh start
#Intentionally not including severity/level because only one validation is there, have included time
import logging
logger = logging.getLogger()
logging.basicConfig(filename='myapp.log',  encoding='utf-8',filemode='a',format="%(asctime)s - %(message)s",level=logging.DEBUG)


#To check if supplied points are within range
def check_coordinates(latitude, longitude):
    if (-90 <= latitude <= 90) and (-180 <= longitude <= 180):
        return True
    else:
        return False


#For keeping an auto incremental ID
#It is better handled by most DBs like PostgreSQL
cnt=0


#Add the address
@app.post('/address/')
async def create_address(address: Address):

    if not check_coordinates(address.latitude, address.longitude):
        logger.error('Incorrect values supplied')
        raise HTTPException(status_code=400, detail='Invalid latitude or longitude.')

    cursor.execute("INSERT INTO addresses (address, latitude, longitude) VALUES (?, ?, ?)",
              (address.address, address.latitude, address.longitude))
    conn.commit()
    global cnt
    cnt+=1
    logger.info('Address created')
    
    #We are returning the id of the created address which can later be used to update/delete
    return {'message': 'Address created successfully.','id':str(cnt)}


#Update the address by providing ID
@app.put('/address/{address_id}')
async def update_address(address_id: int, address: Address):

    if not check_coordinates(address.latitude, address.longitude):
        logger.error('Incorrect values supplied')
        raise HTTPException(status_code=400, detail='Invalid latitude or longitude.')

    cursor.execute("UPDATE addresses SET address=?, latitude=?, longitude=? WHERE id=?",
              (address.address, address.latitude, address.longitude, address_id))
    conn.commit()
    logger.info('Address updated')
    return {'message': 'Address updated successfully.'}


#Delete the address by providing ID
@app.delete('/address/{address_id}')
async def delete_address(address_id: int):
    
    cursor.execute("DELETE FROM addresses WHERE id=?", (address_id,))
    conn.commit()
    logger.info('Address deleted')
    return {'message': 'Address deleted successfully.'}


#All 3 arguments are expected for searching
@app.get('/address/')
async def get_addresses_within_distance(latitude: float = Query(..., description='Latitude'),
                                        longitude: float = Query(..., description='Longitude'),
                                        distance: float = Query(..., description='Distance')):
    
    if not check_coordinates(latitude, longitude):
        logger.error('Incorrect values supplied')
        raise HTTPException(status_code=400, detail='Invalid latitude or longitude.')

    cursor.execute("SELECT * FROM addresses")
    addresses = cursor.fetchall()

    #This will store the final result
    addresses_within_distance = []

    #This point is supplied, will be checked against others
    given_loc=(latitude,longitude)

    for addr in addresses:
        addr_latitude = addr[2]
        addr_longitude = addr[3]
        table_loc = (addr_latitude, addr_longitude)
        
        #Default output of haversine is in KM only
        if hs.haversine(table_loc,given_loc)<=distance:
            addresses_within_distance.append({'id': addr[0], 'address': addr[1], 'latitude': addr[2],
                                               'longitude': addr[3]})

    if len(addresses_within_distance)!=0:
        logger.info("Locations found successfully.")
    else:
        logger.info("No locations found.")

    return {'addresses': addresses_within_distance}