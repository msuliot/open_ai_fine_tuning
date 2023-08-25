# Open AI Fine Tuning

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

    - You should check the status of your fine tuning file by running the following command
    - You will not be able to proceed to the next step until the status is "processed"
    ```bash
    python3 step2_file_validation.py
    ```

3. ** Step 3: Create job for Fine Tuned Model **
    - Using the ID from step 2, update the "TRAINING_FILE_ID" variable in step3_create_finetuned_model.py
    - Run the following command to create your fine tuned model
    ```bash
    python3 step3_create_finetuned_model.py
    ```
    - You should check the status of your fine tuned model by running the following command
    - You will not be able to proceed to the next step until the status is "succeeded" and Fine Tuned Model has a value.
    - This could take some time based on where you are in the queue
    - You will also receive an email from OpenAI when the model is ready
    ```bash
    python3 step3_model_validation.py
    ```

4. ** Step 4: Test New Model  **
    - Using the Fine Tuned Model ID from step 3, update the "FINE_TUNED_MODEL_ID" variable in step4_test_finetuned_model.py
    - Run the following command to test your new model
    ```bash
    python3 step4_test_finetuned_model.py
    ```