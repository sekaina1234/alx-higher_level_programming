#!/bin/bash

# Check for the correct number of command-line arguments
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL provided as a command-line argument
url="$1"

# Use curl to send a HEAD request to the URL
curl -I "$url" 2>/dev/null

# Check the HTTP response code (assuming HTTP)
http_response_code=$(curl -I "$url" 2>/dev/null | head -n 1 | awk '{print $2}')

# Check if curl encountered an error or the server is down
if [ $? -ne 0 ] || [ "$http_response_code" != "200" ]; then
  echo "Error: The web server is not running or the URL is inaccessible."
  exit 1
fi

echo "The web server on $url is up and running."
