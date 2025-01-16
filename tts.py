import os
api_key = os.environ['NARAKEET_API_KEY']
voice = 'mickey'
text = 'Hi there from Python'
url = f'https://api.narakeet.com/text-to-speech/m4a?voice={voice}'

import requests

options = {
    'headers': {
        'Accept': 'application/octet-stream',
        'Content-Type': 'text/plain',
        'x-api-key': api_key,
    },
    'data': text.encode('utf8')
}

try:
    response = response = requests.post(url, **options)
    response.raise_for_status()
    with open('output.m4a', 'wb') as f:
        f.write(response.content)
except requests.exceptions.HTTPError as e:
     # Enhance the error message to include response content if available
    error_message = f'HTTP error occurred: {e.response.status_code} - {e.response.reason}'
    error_details = e.response.text
    raise Exception(f'{error_message}. Details: {error_details}') from None

