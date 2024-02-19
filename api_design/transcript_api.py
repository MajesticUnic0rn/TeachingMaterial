import requests
import json

# establish youtube link
youtube_link= 'https://www.youtube.com/watch?v=MGsalg2f9js&t=546s'

# create a json object

json_data = {
    "url": youtube_link
    }

# send a post request to the server
response_transcription=requests.post('https://stingray-app-7ldgi.ondigitalocean.app/transcribe', json=json_data)

# convert request object to json
json_response = response_transcription.json()

# print out json_response
print(json_response)