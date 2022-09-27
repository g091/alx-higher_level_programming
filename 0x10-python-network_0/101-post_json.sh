#!/bin/bash
# Script sends a JSON POST rqst to a URL & displays the body's response
curl -s -X POST "$1" -d @"$2" --header "Content-Type: application/json"
