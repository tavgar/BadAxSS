# BadAxSS
BadAxSS Tool: to find reflected XSSs
# Reflective Cross-Site Scripting (XSS) Tester

This script tests URLs for reflective Cross-Site Scripting (XSS) vulnerabilities by injecting a test string with chars and then checking if they are reflected back in the HTML code.

## Installation

This script requires Python 3 and the following packages:

- requests
- beautifulsoup4

You can install them using pip:

```pip install requests beautifulsoup4```


## Usage

python Main.py --filename <filename> [--headers key1:value1,key2:value2]


### Arguments

- `--filename`: Required. Specifies the name of the file containing the URLs to test.
- `--headers`: Optional. Allows you to specify custom headers to be included in the requests. Should be in the format `key1:value1,key2:value2`.

## How it works

The script sends GET or POST requests to the URLs in the specified file, injecting a test payload string: `()<>\"';:+ TESTOOO001122`. It then checks if the test string is reflected back in the HTML code. If it is, the script checks if at least 3 characters of the payload string are correctly reflected. As well as it tests every parameter in the given URL and teste it even if it doesn't.

## Note

This script is intended for educational purposes only. Do not use it to test websites that you do not have permission to test.-Site Scripting (XSS) Tester

This script tests URLs for reflective Cross-Site Scripting (XSS) vulnerabilities by injecting a test string and checking if it is reflected back in the HTML code.

## Installation

This script requires Python 3 and the following packages:

- requests
- beautifulsoup4

You can install them using pip:

```pip install requests beautifulsoup4```


## Usage

```python main.py --filename <filename> [--headers key1:value1,key2:value2]```


### Arguments

- `--filename`: Required. Specifies the name of the file containing the URLs to test.
- `--headers`: Optional. Allows you to specify custom headers to be included in the requests. Should be in the format `key1:value1,key2:value2`.

## How it works

The script sends GET or POST requests to the URLs in the specified file, injecting a test payload string: `()<>\"';:+ TESTOOO001122`. It then checks if the test string is reflected back in the HTML code. If it is, the script checks if at least 3 characters of the payload string are correctly reflected.

## Note

This script is intended for educational purposes only. Do not use it to test websites that you do not have permission to test.
