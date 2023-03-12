import concurrent.futures
import requests
from bs4 import BeautifulSoup
import urllib.parse
import argparse


# Parse arguments from user
parser = argparse.ArgumentParser()
parser.add_argument("--headers", type=str, required=False,
                    help="custom headers in format: key1:value1,key2:value2")
parser.add_argument("--filename", type=str, required=True,
                    help="filename containing URLs")
args = parser.parse_args()

# Prompt user for payload and custom headers
payload = "()<>\"';:+ TESTOOO001122"
headers = {}
header_input = args.headers
if header_input:
    for header in header_input.split(','):
        key, value = header.split(':')
        headers[key.strip()] = value.strip()

# Define function to test a single URL
def test_url(url):
    # Split the URL into base URL and query parameters
    url_parts = urllib.parse.urlsplit(url)
    base_url = url_parts.scheme + "://" + url_parts.netloc + url_parts.path
    query_params = urllib.parse.parse_qs(url_parts.query)

    if query_params:
                # Test each query parameter separately
                for param in query_params:
                    try:
                        param_value = query_params[param][0]
                        query_url = base_url + "?" + param + "=" + param_value
                        method = "GET" if not url_parts.query else "POST"
                        response = requests.request(method, query_url, data=payload, headers=headers,timeout=10)
                        soup = BeautifulSoup(response.content, 'html.parser')

                        # Find TESTOOO001122 in HTML code
                        test_string = "TESTOOO001122"
                        test_string_start_index = str(soup).find(test_string)

                        # Check for characters before and after TESTOOO001122
                        char_count = 0
                        reflected_chars = ""
                        for char in payload:
                            if char in str(soup)[test_string_start_index-1:test_string_start_index] or \
                               char in str(soup)[test_string_start_index+len(test_string):test_string_start_index+len(test_string)+1]:
                                char_count += 1
                                reflected_chars += char

                        # Check if at least 3 characters were reflected correctly
                        if char_count >= 3:
                            print("The URL {} passed the test. Reflected characters: {}".format(query_url, reflected_chars))
                            return True
                        else:
                            print("The URL {} failed the test. Reflected characters: {}".format(query_url, reflected_chars))
                            return False
                    except:
                        pass
    else:
        try:
            # Test the URL as it is
            method = "GET" if not url_parts.query else "POST"
            response = requests.request(method, url, data=payload, headers=headers,timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find TESTOOO001122 in HTML code
            test_string = "TESTOOO001122"
            test_string_start_index = str(soup).find(test_string)

            # Check for characters before and after TESTOOO001122
            char_count = 0
            reflected_chars = ""
            for char in payload:
                if char in str(soup)[test_string_start_index-1:test_string_start_index] or \
                   char in str(soup)[test_string_start_index+len(test_string):test_string_start_index+len(test_string)+1]:
                    char_count += 1
                    reflected_chars += char

            # Check if at least 3 characters were reflected correctly
            if char_count >= 3:
                print("The URL {} passed the test. Reflected characters: {}".format(url, reflected_chars))
                return True
            else:
                print("The URL {} failed the test. Reflected characters: {}".format(url, reflected_chars))
                return False
        except:
            pass
# Read URLs from file and create a thread pool
with open(args.filename, "r") as file:
    urls = file.readlines()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit tasks for each URL
    futures = [executor.submit(test_url, url.strip()) for url in urls]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)
