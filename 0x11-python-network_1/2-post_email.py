#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary containing the email parameter
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except Exception as e:
        print("Error:", e)
else:
    print("Usage: ./2-post_email.py <URL> <email>")
