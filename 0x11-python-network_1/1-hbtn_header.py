#!/usr/bin/python3
import urllib.request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            header = response.info()
            x_request_id = header.get('X-Request-Id')
            if x_request_id is not None:
                print(x_request_id)
    except Exception as e:
        print("Error:", e)
