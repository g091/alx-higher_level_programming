#!/bin/bash
# That takes in a URL, sends a POST rqst to it, & displays the body of the response
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
