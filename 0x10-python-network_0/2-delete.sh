#!/bin/bash
# Bash Script that sends a DELETE request to the URL passed as the first argument
curl -sX DELETE "$1"
