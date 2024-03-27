# address-book-submission

## Step 0: Create a virtual env

For linux, use source
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

Create ==> 
py driver.py --add --str=<Any_address_Name> --lat=<Latitude> --lon=<Longitude>

Read   ==> 
py driver.py --find --lat=<Latitude> --lon=<Longitude> --dis=<Distance>

Update ==> 
py driver.py --update --str=<Any_address_Name> --lat=<Latitude> --lon=<Longitude> --id=<ID>

Delete ==> 
py driver.py --delete --id=<ID>
