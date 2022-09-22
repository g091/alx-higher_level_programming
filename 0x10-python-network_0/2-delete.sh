#!/bin/bash
# That sends a DELETE request to the URL passed as the 1st arg & displays the body
curl -s "$1" -X DELETE
