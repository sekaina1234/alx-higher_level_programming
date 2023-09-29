#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)
    except requests.exceptions.RequestException as e:
        if response.status_code >= 400:
            print("Error code:", response.status_code)
    except Exception as e:
        print("Error:", e)
else:
    print("Usage: ./7-error_code.py <URL>")
