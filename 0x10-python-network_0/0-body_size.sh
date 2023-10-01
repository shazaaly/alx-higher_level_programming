#!/bin/bash
#  a Bash script that takes in a URL,
# sends a request to that URL, and displays
# the size of the body of the response
# The size must be displayed in bytes
# You have to use curl

if [ $# -lt 1 ]; then
	exit 1
fi

url="$1"
curl -s "$url" | wc -c
