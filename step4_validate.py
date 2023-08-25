import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo-0613:michael-ai::7rFvNGY4",
  temperature=0.0,
  messages=[
    {"role": "system", "content": "Your name is Aiden, You are a customer service representative for a multiple listing service"},
    {"role": "user", "content": "How can I reactivate my expired listing?"},
  ]
)

print(completion.choices[0].message)

