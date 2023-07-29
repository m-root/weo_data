import requests
import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get the current file's directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Create the paths to the files
file = os.path.abspath(os.path.join(current_dir, '..', 'data', 'test_data.json'))

url = "http://127.0.0.1:5000/predict"

headers = {'Content-Type': 'application/json'}

data = json.load(open(file, 'r'))

response = requests.post(url, data=json.dumps(data), headers=headers)

logging.info("Status Code: %s", response.status_code)
logging.info("Response Body: %s", response.text)

if response.status_code == 200:
    try:
        logging.info(response.json())
    except json.JSONDecodeError:
        logging.error("Couldn't decode the response as JSON.")
else:
    logging.error("Received error from server, status code: %s", response.status_code)
