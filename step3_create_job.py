import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

##### You will need to replace the file id with the one you got from the previous step.
ft_job = openai.FineTuningJob.create(training_file="TRAINING_FILE_ID", model="gpt-3.5-turbo-0613")
print(ft_job)
