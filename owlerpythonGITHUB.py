import requests
import json
from base64 import b64encode # Shouldn't be necessary, but keep it still.

# Login section
username = "Fluffy"
password = "hu$>++~vc7'#Hie"
login_request = requests.get("https://api.owler.cloud/v1/account/verify_credentials.json", auth=(username, password))
# Status code checks
if login_request.status_code == 401:
    print("Failed to authenticate due to bad username or password.")
    exit(1)
elif login_request.status_code == 400:
    print("Failed to authenticate due to a server or validation error.")
    exit(1)
# Owler status stuff
url = "https://api.owler.cloud/v1/statuses/update.json"
print("Login successful!\nSubmit a status:")
x = input()
print("Your status is: " + x)
post_request = requests.post(f"{url}?status={x}&source=a python script", auth=(username, password)) # update request
# Status code checks 2
if post_request.status_code == 401:
    print("Failed to post due to bad login credientials (This should *not* happen, but it happened anyways. Go figure.)")
    exit(1)
elif post_request.status_code == 400:
    print("Error! Error!")
    exit(1)
elif post_request.status_code == 200:
    print("Success! Check your owler page now.")
    exit(1)
