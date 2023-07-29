import requests
import json

url = "http://127.0.0.1:5000/predict"

headers = {'Content-Type': 'application/json'}

data = json.load(open('data/test_data.json', 'r'))

response = requests.post(url, data=json.dumps(data), headers=headers)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

try:
    print(response.json())
except json.JSONDecodeError:
    print("Couldn't decode the response as JSON.")
