#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = 'http://0.0.0.0:5000/search_user'
payload = {'q': q}

try:
    response = requests.post(url, data=payload)
    response.raise_for_status()

    data = response.json()
    if data:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
except requests.exceptions.RequestException as e:
    print("No result")
