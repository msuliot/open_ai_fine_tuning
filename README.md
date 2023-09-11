# Open AI Fine Tuning

## YouTube Video Tutorial For this GitHub Repository
[Open AI Fine Tuning](https://youtu.be/Q1VfJwLk3hg)


## The basics

1. Must have Python3.
2. Get repository
```bash
git clone https://github.com/msuliot/open_ai_fine_tuning.git
```
3. use pip3 to install any dependencies. (must have latest version of OpenAI)
```bash
pip3 install --upgrade -r requirements.txt
```

## Open AI / ChatGPT

Make sure to get an OpenAI key from https://platform.openai.com/account/api-keys

Create a ".env" file and put your OpenAI key in that file
```bash
OPENAI_API_KEY='your key here'
```

## Instructions:

1. ** Step 1: Fine Tuning File **
    - Your fine tuning file must in the the format of JSON Lines (jsonl) 
    - Sample file is provided in the repository
    - Run the following command to validate your file is in the proper JSON Lines format for OpenAI
    ```bash
    python3 step1_validate_finetune_file.py
    ```

2. ** Step 2: Upload File to OpenAI **
    - Run the following command to upload your file to OpenAI
    ```bash
    python3 step2_upload_file.py
    ```
    - This will return a "id" which you will need for the next step

3. ** Step 3: File Validation at OpenAI **
    - You should check the status of your fine tuning file by running the following command
    - You will not be able to proceed to the next step until the status is "processed"
    ```bash
    python3 step3_file_validation.py
    ```

4. ** Step 4: Create job for Fine Tuned Model at OpenAI **
    - Using the ID from step 2 or 3, update the "TRAINING_FILE_ID" variable in step4_create_finetuned_model.py
    - Run the following command to create your fine tuned model
    ```bash
    python3 step4_create_finetuned_model.py
    ```

5. ** Step 5: Model Validation at OpenAI **
    - You should check the status of your fine tuned model by running the following command
    - You will not be able to proceed to the next step until the status is "succeeded" and Fine Tuned Model has a value.
    - This could take some time based on where you are in the queue anywhere from 5 minutes to 20 minutes
    - You will also receive an email from OpenAI when the model is ready or run the following command to check the status
    ```bash
    python3 step5_model_validation.py
    ```

6. ** Step 6: Test New Model  **
    - Using the Fine Tuned Model ID from step 4 or 5, update the "FINE_TUNED_MODEL_ID" variable in step6_test_finetuned_model.py
    - Run the following command to test your new model
    ```bash
    python3 step6_test_finetuned_model.py
    ```

## Full Automatic
- Full automatic will run the entire process from start to finish, You're welcome!

    ```bash
    python3 full_automatic.py
    ```


##  Clean Up: Delete Files and Fine Tuned Models
- Use the cleanup.py file to list all files and models
- Delete your files 
- Delete your fine tuned models
- Download files
- Commands are commented out in the botton of the file