#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id is not None:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
else:
    print("Usage: ./5-hbtn_header.py <URL>")
