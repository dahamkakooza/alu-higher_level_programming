#!/bin/bash
# Sends a GET request to the provided URL and displays the body only if the response status code is 200
response=$(curl -s -o /dev/null -w "%{http_code}" -L "$1")[ "$response" -eq 200 ] && curl -s -L "$1"
