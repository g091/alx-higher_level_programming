#!/bin/bash
# Takes a URL, sends a GET request to it, & displays the body of the response
curl -sfL "$1" -X GET
