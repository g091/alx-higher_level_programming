#!/bin/bash
# That takes in a URL as an arg, sends a GET request to it, & displays the body
curl -s "$1" -X GET -H "X-School-User-Id: 98"
