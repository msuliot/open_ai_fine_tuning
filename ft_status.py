import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

import json

print("List 10 fine-tuning jobs")
job_list = openai.FineTuningJob.list(limit=10)
print(job_list) 

print("List 10 files")
file_list = openai.File.list(limit=10)
print(file_list) 


# # Retrieve the state of a fine-tune
# ft_job=openai.FineTuningJob.retrieve("ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I")
# print(ft_job)

# openai.Model.delete("ft:gpt-3.5-turbo-0613:michael-ai::7rDDeuYa")

# # List up to 10 events from a fine-tuning job
# openai.FineTuningJob.list_events(id="ft-abc123", limit=10)