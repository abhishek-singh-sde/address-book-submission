# address-book-submission

The logger file and the DB shall be created once the driver code is executed.

## Step 0: Create a virtual env

```
py -m venv venv
cd venv\Scripts
activate
```

## Step 1: Install the required libraries

```
pip install -r requirements.txt
```

## Step 2: Run the server
```
uvicorn main:app --host 127.0.0.1 --port 8080
```

## Step 3: Run the driver code
In a seperate terminal, run main.py



The following flags are expected (in order) for the respective operations:
```
Create ==> 
py driver.py --add --str=<Any_address_Name> --lat=<Latitude> --lon=<Longitude>

Read   ==> 
py driver.py --find --lat=<Latitude> --lon=<Longitude> --dis=<Distance>

Update ==> 
py driver.py --update --str=<Any_address_Name> --lat=<Latitude> --lon=<Longitude> --id=<ID>

Delete ==> 
py driver.py --delete --id=<ID>
```

## Sample Runs:
```
(venv) C:\Users\abhin\OneDrive\Desktop\Submission>py driver.py --add --str=PointA --lat=12.43 --lon=12.32

(venv) C:\Users\abhin\OneDrive\Desktop\Submission>py driver.py --add --str=PointA --lat=12.43 --lon=12.32
Address added and the assigned ID is 1

(venv) C:\Users\abhin\OneDrive\Desktop\Submission>py driver.py --add --str=PointB --lat=12.44 --lon=12.33
Address added and the assigned ID is 2

(venv) C:\Users\abhin\OneDrive\Desktop\Submission>py driver.py --add --str=PointB --lat=12.44 --lon=12.33
Address added and the assigned ID is 3

(venv) C:\Users\abhin\OneDrive\Desktop\Submission>py driver.py --del --id=3
Address deleted

(venv) C:\Users\abhin\OneDrive\Desktop\Submission>py driver.py --add --str=PointC --lat=12.45 --lon=12.34
Address added and the assigned ID is 4

(venv) C:\Users\abhin\OneDrive\Desktop\Submission>py driver.py --update --str=PointA --lat=12.40 --lon=12.30 --id=1
Address updated

(venv) C:\Users\abhin\OneDrive\Desktop\Submission>py driver.py --find --lat=12.40 --lon=12.30 --dis=900
Following addresses have been found with matching criteria:
{'id': 1, 'address': 'PointA', 'latitude': 12.4, 'longitude': 12.3}
{'id': 2, 'address': 'PointB', 'latitude': 12.44, 'longitude': 12.33}
{'id': 3, 'address': 'PointC', 'latitude': 12.45, 'longitude': 12.34}
```
