#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./10-my_github.py <username> <token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

headers = {
    'Authorization': 'Basic ' + (username + ':' + token).encode('utf-8').decode('base64')
}

url = 'https://api.github.com/user'

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    print(data.get('id'))
except requests.exceptions.RequestException as e:
    print(None)
except ValueError:
    print(None)
