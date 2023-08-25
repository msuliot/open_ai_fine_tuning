import json

# File must be in jsonlines format (https://jsonlines.org/)
def read_from_jsonl(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return [json.loads(line) for line in lines]
    except Exception as e:
        print("Error reading file, invalid format: ", e)
        return []


def main():
    # Read data from jsonl file
    read_data = read_from_jsonl('data.jsonl')

    for record in read_data:
        print(record)


if __name__ == "__main__":
    main()

