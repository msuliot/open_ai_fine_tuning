import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
  model="FINE_TUNED_MODEL_ID",
  temperature=0.0,
  messages=[
    {"role": "system", "content": "You are a helpful and professional customer service representative for a multiple listing service"},
    {"role": "user", "content": "dude... what is name? i forgot my password."},
  ]
)

print(completion.choices[0].message)

