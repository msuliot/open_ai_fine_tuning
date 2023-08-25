import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def delete_file(file_id):
    try:
        openai.File.delete(file_id)
        print("File deleted successfully")
    except Exception as e:
        print("Error deleting file: ", e)


def delete_finetune_model(model_id):
    try:
        openai.Model.delete(model_id)
        print("Model has been deleted successfully")
    except Exception as e:
        print("Error deleting model: ", e)

# delete_file("file-vdVqfMGiIzQedB4zavb9Ywk2")   
# delete_finetune_model("ft:gpt-3.5-turbo-0613:michael-ai::7rDDeuYa")
