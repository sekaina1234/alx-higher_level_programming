#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        print("Your email is:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
else:
    print("Usage: ./6-post_email.py <URL> <email>")
