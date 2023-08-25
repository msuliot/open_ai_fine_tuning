import openai
import datetime

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def pretty_table(f):
    print(f"{'ID':<33} {'Created At':<22} {'Finished At':<22} {'Status':<13} {'Fine Tuned Model'} ")
    print('-' * 140)
    for job in f['data']:
        created_at = datetime.datetime.fromtimestamp(job['created_at']).strftime('%Y-%m-%d %H:%M:%S')
        finished_at = datetime.datetime.fromtimestamp(job['finished_at']).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"{job['id']:<33} {created_at:<22} {finished_at:<22} {job['status']:<13} {job['fine_tuned_model']} ")


def main():
    job_list = openai.FineTuningJob.list(limit=10)
    pretty_table(job_list)


if __name__ == "__main__":
    main()