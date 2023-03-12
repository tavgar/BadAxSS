import requests
from bs4 import BeautifulSoup
import urllib.parse

# Prompt user for payload and custom headers
payload = "()<>\"';:+ TESTOOO001122"
headers = {}
header_input = input("Enter custom headers (format: key1:value1,key2:value2): ")
if header_input:
    for header in header_input.split(','):
        key, value = header.split(':')
        headers[key.strip()] = value.strip()

# Determine request type based on whether the URL contains a query string
def get_method(url):
    if urllib.parse.urlparse(url).query:
        return "GET"
    else:
        return "POST"

# Define function to test a single URL
def test_url(url):
    method = get_method(url)

    # Send request with payload and custom headers
    if method == "GET":
        response = requests.get(url + payload, headers=headers)
    else:
        response = requests.post(url, data=payload, headers=headers)

    # Parse HTML code
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
# Read URLs from file and test each one
filename = input("Enter filename containing URLs: ")
with open(filename, "r") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    test_url(url)
