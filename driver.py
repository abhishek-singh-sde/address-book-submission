import sys
import requests

#Getting the first argument which will decide the method to call
choice=sys.argv[1][2:4]

#Instead of branching, we can use a factory method here
#But since we have 4 only for now, hence used switch/elif


#For creating an address
if choice=="ad":
        address_string=sys.argv[2][6:]
        latitude=float(sys.argv[3][6:])
        longitude=float(sys.argv[4][6:])
        
        url = 'http://127.0.0.1:8080/address/'
        myobj={"address": address_string,"latitude": latitude,"longitude": longitude}

        #Sending the post request with required body
        resp=requests.post(url, json = myobj)


        #This works because we are returning an ID only upon successful creation
        #We can check it via status code as well. Used this to only show response.
        if "id" in resp.json():
            print("Address added and the assigned ID is "+str(resp.json()['id']))
        else:
            print("Incorrect Input")


#For updating an address
elif choice=="up":
        address_string=sys.argv[2][6:]
        latitude=float(sys.argv[3][6:])
        longitude=float(sys.argv[4][6:])
        id_string=sys.argv[5][5:]

        url = 'http://127.0.0.1:8080/address/'+id_string
        myobj={"address": address_string,"latitude": latitude,"longitude": longitude}

        #Sending the put request with required body 
        #Includes the id that will take care which record to update
        resp=requests.put(url, json = myobj)
        

        #This works because we are returning a message only upon successful creation
        #We can check it via status code as well. Used this to only show response.
        if "message" in resp.json():
            print("Address updated")
        else:
            print("Incorrect input")


#For deleting an address
elif choice=="de":
        id_string=sys.argv[2][5:]
        url = 'http://127.0.0.1:8080/address/'+id_string

        #Sending the delete request with required body 
        #Includes the id that will take care which record to update
        resp=requests.delete(url)
        
        if "message" in resp.json():
            print("Address deleted")
        else:
            print("ID doesn't exist")


#For finding matching addresses
elif choice=="fi":
        #Getting the 3 values for searching in current database (distance to be entered in KM)
        latitude=float(sys.argv[2][6:])
        longitude=float(sys.argv[3][6:])
        distance=float(sys.argv[4][6:])
        

        url = 'http://127.0.0.1:8080/address/'

        created_params={"latitude": latitude,"longitude": longitude,"distance": distance}

        #Sending the get request with required parameters 
        resp=requests.get(url, params=created_params)
        
        if(len(list(resp.json()['addresses'])))==0:
              print("No Addresses Found")
        else:
              print("Following addresses have been found with matching criteria:")
              for address in list(resp.json()['addresses']):
                    print(address)