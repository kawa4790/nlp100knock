# 46.川柳の作成
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "「四月」をお題として、川柳を10個作成してください。"

response = model.generate_content(prompt)
print(response.text)