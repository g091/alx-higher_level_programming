#!/bin/bash
# That takes in a URL as an arg, sends a GET request to it, & displays the body
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
