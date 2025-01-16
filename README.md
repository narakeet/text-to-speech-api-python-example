# Narakeet Text to Speech Streaming API example in Python

This repository provides a quick example demonstrating how to access the Narakeet [streaming Text to Speech API](https://www.narakeet.com/docs/automating/text-to-speech-api/) from Python. 

The example sends a request to generate audio from text and saves it `output.m4a` in the local directory.

The example uses the [requests](https://requests.readthedocs.io/en/latest/) python library to send HTTPS requests to the Narakeet API.

Note that Narakeet also has a text to speech API to generate long content, suitable for larger conversion tasks. See the [Long Content Text to Speech API Example](https://github.com/narakeet/text-to-speech-polling-api-python-example) for more information on how to use that.

## Prerequisites

To use this example, you will need Python (3.7 or more recent), and an API key for Narakeet.

## Running the example using Docker

You can run the example using Docker without a local Python installation, using the following command line (replace `YOUR_NARAKEET_API_KEY` with your Narakeet API key):

```
make run NARAKEET_API_KEY=YOUR_NARAKEET_API_KEY
```

## Running the example without Docker

1. edit [tts.py](tts.py) and add your API key on line 1, instead of the value `'YOUR_API_KEY_HERE'`. You can optionally modify the voice and text parameters on lines 2 and 3, which control the text to speech synthesis voice and the text sent to the API for synthesis.
2. run `pip install -r requirements.txt` to install the required libraries
3. run `python tts.py` to create the output audio. 

## More information

Check out <https://www.narakeet.com/docs/automating/text-to-speech-api/> for more information on the Narakeet Text to Speech API
