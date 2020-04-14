#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable X-Request-Id in the
response header"""

if __name__ == '__main__':
    import requests
    import sys
    request = requests.get(sys.argv[1])
    if request.status_code >= 400:
        print('Error code: {}'.format(request.status_code))
    else:
        print(request.text)
