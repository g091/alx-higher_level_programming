#!/bin/bash
# Script that sends a rqst to a URL, & displays only the status code
curl -s -o /dev/null -I --w "%{http_code}" "$1"
