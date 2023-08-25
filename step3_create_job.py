import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


###### Validate the file as been uploaded
###### id ==> training file id
###### status ==> processed
###### purpose ==> fine-tune
# f = openai.File.list()
# print(f)


##### You will need to replace the file id with the one you got from the previous step.
# ft_job = openai.FineTuningJob.create(training_file="file-iTJamSDwT9iKQ71FoxjBDxOp", model="gpt-3.5-turbo-0613")
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
ft_job=openai.FineTuningJob.retrieve("ftjob-YF07m2GU0GWXp6LgBZFKr7Bk")
print(ft_job)
print(ft_job["fine_tuned_model"])
# # Cancel a job
# openai.FineTuningJob.cancel("ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I")

# # List up to 10 events from a fine-tuning job
# list_events = openai.FineTuningJob.list_events(id="ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I", limit=100)
# print(list_events)
# # Delete a fine-tuned model (must be an owner of the org the model was created in)
# # import openai

# openai.Model.delete("ftjob-9FKDzGk9LL3pJ4Ou44sCcT7I")
