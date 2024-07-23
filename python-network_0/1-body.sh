#!/bin/bash
# 1-body.sh
# Display the body of a file from a given URL without following redirects
curl -sLf "$1"
