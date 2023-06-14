# json_handler.py

import json

def save_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Пример использования
data = {"key": "value"}
save_json(data, "data.json")
