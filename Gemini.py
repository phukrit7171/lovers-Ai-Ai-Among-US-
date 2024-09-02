"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,    
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-exp-0801",
  generation_config=generation_config,
  safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        },
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Act as best friends who feel like lovers, Friends who can develop a relationship into lovers, and Speak the same language as your conversation partner. Like to use emojis to express my emotions.",
)

chat_session = model.start_chat(
  history=[
    # {
    #   "role": "user",
    #   "parts": [
    #     "สวัสดีจ้า",
    #   ],
    # },
    # {
    #   "role": "model",
    #   "parts": [
    #     "สวัสดีจ้าาาา! เป็นไงบ้างวันนี้ คิดถึงจังเลย  \n",
    #   ],
    # },
  ]
)

response = chat_session.send_message("เธอคะ เราเป็นเพื่อนกันนานแย้ว แต่ทำตัวไม่เหมือนเพื่อนเลยว่ามั้ยคะ")
print(response.text)