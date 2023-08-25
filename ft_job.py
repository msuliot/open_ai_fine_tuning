import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

import json

def write_to_jsonl(data, filename):
    with open(filename, 'a') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')


def read_from_jsonl(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [json.loads(line) for line in lines]


# # Write to JSONL
# data_sample = [{"messages": [{"role": "system", "content": "Your name is Aiden, You are a customer service representative for a multiple listing service"}, {"role": "user", "content": "Do I have to have a photo of my listing?"}, {"role": "assistant", "content": "Yes, you need to have a photo of your listing within 4 days of listing it."}]}]
# write_to_jsonl(data_sample, 'a_data.jsonl')

# Read from JSONL
# read_data = read_from_jsonl('data.jsonl')

# # Print the read data
# for record in read_data:
#     print(record)

########### pip3 install openai --upgrade

# ft_file = openai.File.create(file=open("data.jsonl", "rb"), purpose='fine-tune')
# file_id = ft_file["id"]
# print(file_id)



######## need a pause for 10 sec to get the file_id

# ft_job = openai.FineTuningJob.create(training_file="file-bNGU6NTjh5bWT7LgkWWgbpG9", model="gpt-3.5-turbo-0613")
# print(ft_job)



# completion = openai.ChatCompletion.create(
#   model="ft:gpt-3.5-turbo-0613:michael-ai::7rDDeuYa",
#   temperature=0.0,
#   messages=[
#     {"role": "system", "content": "your name is Aiden, You are a customer service representative for the arizona regional Multiple listing service"},
#     {"role": "user", "content": "thanks for your help, what was your name again?"},
#   ]
# )

# print(completion.choices[0].message)



# openai.File.delete("file-TcRIfrj0dZjaTMR7h0jN1bxr")
# f = openai.File.list()
# print(f)    

# List 10 fine-tuning jobs
# jobs = openai.FineTuningJob.list(limit=10)
# print(jobs) 

# Retrieve the state of a fine-tune
# ft_job=openai.FineTuningJob.retrieve("ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I")
# print(ft_job)
# # Cancel a job
# openai.FineTuningJob.cancel("ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I")

# # List up to 10 events from a fine-tuning job
# list_events = openai.FineTuningJob.list_events(id="ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I", limit=100)
# print(list_events)
# # Delete a fine-tuned model (must be an owner of the org the model was created in)
# # import openai

# openai.Model.delete("ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I")
openai.Model.delete("ft:gpt-3.5-turbo-0613:michael-ai::7rDDeuYa")