# import random
# import string

# # Generate a 24-character alphanumeric string
# random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
# print(random_string)


import requests
import json

url = "http://127.0.0.1:8002/register_with"  # Assuming 8000 is the correct port
headers = {"Content-Type": "application/json"}
data = {"node_address": "http://127.0.0.1:8000"}  # Adjust according to your node setup

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.text)

# import requests

# Perform GET request on port 8001
# response_8001 = requests.get("http://localhost:8001/chain")
# print("Response from port 8001:", response_8001.text)

# # # Perform GET request on port 8002
# response_8002 = requests.get("http://localhost:8002/chain")
# print("Response from port 8002:", response_8002.text)

# # # Perform GET request on port 8000
# response_8000 = requests.get("http://localhost:8000/chain")
# print("Response from port 8000:", response_8000.text)
