#!/bin/bash
#  a Bash script that takes in a URL and send header of x school 98
curl -sH "X-School-User-Id: 98" "${1}"
