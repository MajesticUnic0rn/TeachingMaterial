import os
import requests
from pydantic import BaseModel, Field
import dotenv
from dotenv import load_dotenv
import openai
from openai import OpenAI
load_dotenv()
client = OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")

# establish youtube link
youtube_link= 'https://www.youtube.com/watch?v=m0rs8rho4qA'

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


class food_service(BaseModel):
    order: str = Field(..., description="give me on sentence what the customer ordered")


chat_tools = [
    {
        "type": "function",
        "function": {
            "name": "food_service",
            "description": "Summarize this transcript into a food service structure",
            "parameters": food_service.model_json_schema(),
            "required": ["order"]
        }
    }
]

# model list: gpt-3.5-turbo-1106 , gpt-4-0613
def chat_summary(full_transcription, tools=chat_tools, tool_choice=None, model='gpt-3.5-turbo-1106'):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai.api_key,
    }

    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant designed to break down a transcript and give me the customer order in a short sentence."})
    messages.append({"role": "user", "content": f" {full_transcription}"})
    
    json_data = {"model": model, "messages": messages}
    if tools is not None:
        json_data.update({"tools": tools})
    if tool_choice is not None:
        json_data.update({"tool_choice": tool_choice})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

llm_output=chat_summary(json_response, tools=chat_tools, tool_choice=None, model='gpt-3.5-turbo-1106')
print(llm_output.text)