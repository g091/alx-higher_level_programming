#!/bin/bash
# That takes in a URL as an arg, sends a GET request to it, & displays the body
curl -si -X "OPTIONS" $1 | grep "Allow" | cut -d " " -f 2-
