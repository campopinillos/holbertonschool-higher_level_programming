#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable X-Request-Id in the
response header"""

if __name__ == '__main__':
    import requests
    request = requests.get('https://intranet.hbtn.io/status')
    print(request.headers.get('X-Request-Id'))
