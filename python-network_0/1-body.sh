#!/bin/bash
# Sends a GET request to the provided URL and displays the body only if the response status code is 200
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -s "$1"
