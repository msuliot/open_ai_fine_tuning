import requests
import time
import openai
import datetime
import json
import sys
# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def read_from_jsonl(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return True
    except Exception as e:
        print("Error reading file, invalid format: ", e)
        return False
    

# Step 1: validate the file
def step1():
    return read_from_jsonl('data.jsonl')


# Step 2: upload the file
def step2():
    ft_file = openai.File.create(file=open("data.jsonl", "rb"), purpose='fine-tune')
    # print(ft_file)
    return ft_file["id"]


# Step 4: create the finetuned model
def step4(training_file_id):
    ##### You will need to replace the TRAINING_FILE_ID with the one you got from the previous step.
    ft_job = openai.FineTuningJob.create(training_file=training_file_id, model="gpt-3.5-turbo-0613")
    return ft_job["id"] 


# # Step 5: Validate the model succeeded
# def step5():
#     job_list = openai.FineTuningJob.list(limit=10)
#     # print(job_list)
#     pretty_table5(job_list)


# Step 6: Test the model
def step6(model_id, prompt):
    completion = openai.ChatCompletion.create(
        model=model_id,
        temperature=0.0,
        messages=[
            {"role": "system", "content": "You are a helpful and professional customer service representative for a multiple listing service"},
            {"role": "user", "content": prompt},
        ]
    )

    print(completion.choices[0].message)





# Step 1: validate the file
is_file_valid = step1()
if is_file_valid == False:
    print("File is not valid")
    sys.exit()

# Step 2: upload the file and wait for it to be processed
file_id = step2()
looptime = 0
while True:
    looptime += 1
    print(f"Waiting for file to be processed... {looptime}")
    file_status = openai.File.retrieve(file_id)
    if file_status["status"] == "processed":
        print(f"File processed: {file_status['id']}")
        break
    time.sleep(5)

print("\nFile processed\n")


looptime = 0
fine_tuning_job = step4(file_id)
model_id = ""
while True:
    looptime += 1
    print(f"Waiting for model to be processed... {looptime}")
    model_status = openai.FineTuningJob.retrieve(fine_tuning_job)
    if model_status["status"] == "succeeded":
        model_id = model_status["fine_tuned_model"]
        break
    time.sleep(30)

print(f"Model created: {model_id}")

# Step 6: Test the model
print("\nTesting the model\n")
step6(model_id, "dude... i forgot my password.") 
