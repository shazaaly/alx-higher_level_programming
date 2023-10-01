#!/bin/bash
# Get the byte size of the HTTP response using cURL
curl -s "$1" | wc -c
