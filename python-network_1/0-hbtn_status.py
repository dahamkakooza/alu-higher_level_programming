#!/usr/bin/python3
"""
A Python script to fetch the status from a URL.

This module uses the urllib.request module to perform an HTTP GET request
to the specified URL and prints the response content in both raw bytes and
UTF-8 decoded formats. It also includes error handling for HTTP and URL errors.

Functions:
    main(): The main function that performs the HTTP GET request and handles the response.

Usage:
    Run this script directly to see the output from fetching the URL.
"""

import urllib.request

def main():
    """
    Fetches the status from the specified URL and prints the response.

    This function sends an HTTP GET request to the URL 'https://intranet.hbtn.io/status'
    with a User-Agent header to mimic a browser request. It then reads the response
    and prints the type of the response content, the raw content, and the UTF-8 decoded content.

    It also handles potential HTTP and URL errors and prints appropriate error messages.
    """
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == '__main__':
    main()
