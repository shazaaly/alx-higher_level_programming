#!/bin/bash
# a Bash script that takes in a URL

curl -s "$1" | wc -c
