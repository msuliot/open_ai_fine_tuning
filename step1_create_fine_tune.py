import json

def write_to_jsonl(data, filename):
    with open(filename, 'a') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')

def read_from_jsonl(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [json.loads(line) for line in lines]

# Write to JSONL
data_sample = [{"messages": [{"role": "system", "content": "Your name is Aiden, You are a customer service representative for a multiple listing service"}, {"role": "user", "content": "Do I have to have a photo of my listing?"}, {"role": "assistant", "content": "Yes, you need to have a photo of your listing within 4 days of listing it."}]}]
write_to_jsonl(data_sample, 'data.jsonl')

# Read from JSONL
read_data = read_from_jsonl('data.jsonl')

# # Print the read data
for record in read_data:
    print(record)
