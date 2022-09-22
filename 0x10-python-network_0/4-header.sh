#!/bin/bash
# That takes in a URL as an arg, sends a GET request to it, & displays the body
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
