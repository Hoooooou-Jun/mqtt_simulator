import json

file_path = "./dummy.json"
def read_json():
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Success read file in {file_path}")
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path}")
        return False
