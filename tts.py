apikey = 'Vx7fL81hsF6MfhAlsUi8Eakc3t2lQATX1p3HWTiP'
voice = 'mickey'
text = 'Hi there from Python'
url = f'https://api.narakeet.com/text-to-speech/m4a?voice={voice}'

import requests

options = {
    'headers': {
        'Accept': 'application/octet-stream',
        'Content-Type': 'text/plain',
        'x-api-key': apikey,
    },
    'data': text.encode('utf8')
}

with open('output.m4a', 'wb') as f:
    f.write(requests.post(url, **options).content)

