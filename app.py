import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

import json

def write_to_jsonl(data, filename):
    """
    Writes a list of dictionaries to a JSONL file.
    
    :param data: List of dictionaries to write
    :param filename: Name of the JSONL file
    """
    with open(filename, 'w') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')


def read_from_jsonl(filename):
    """
    Reads data from a JSONL file.
    
    :param filename: Name of the JSONL file
    :return: List of dictionaries
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [json.loads(line) for line in lines]


# # Write to JSONL
# write_to_jsonl(data_sample, 'data.jsonl')

# Read from JSONL
# read_data = read_from_jsonl('data.jsonl')

# # Print the read data
# for record in read_data:
#     print(record)

########### pip3 install openai --upgrade

# ft_file = openai.File.create(file=open("data.jsonl", "rb"), purpose='fine-tune')
# file_id = ft_file["id"]
# print(file_id)

######## need a pause for 10 sedonds to get the file_id

# ft_job = openai.FineTuningJob.create(training_file="file-bNGU6NTjh5bWT7LgkWWgbpG9", model="gpt-3.5-turbo-0613")
# print(ft_job)



completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo-0613:michael-ai::7rDDeuYa",
  temperature=0.0,
  messages=[
    {"role": "system", "content": "your name is Aiden, You are a customer service representative for the arizona regional Multiple listing service"},
    {"role": "user", "content": "thanks for your help, what was your name again?"},
  ]
)

print(completion.choices[0].message)



# List 10 fine-tuning jobs
# jobs = openai.FineTuningJob.list(limit=10)
# print(jobs) 

# Retrieve the state of a fine-tune
# ft_job=openai.FineTuningJob.retrieve("ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I")
# print(ft_job)
# # Cancel a job
# openai.FineTuningJob.cancel("ft-abc123")

# # List up to 10 events from a fine-tuning job
# openai.FineTuningJob.list_events(id="ft-abc123", limit=10)

# # Delete a fine-tuned model (must be an owner of the org the model was created in)
# import openai
# openai.Model.delete("ft-abc123")