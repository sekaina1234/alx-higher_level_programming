#!/usr/bin/python3
import requests

url = 'https://alx-intranet.hbtn.io/status'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP status codes >= 400
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
except requests.exceptions.RequestException as e:
    print("Error:", e)
