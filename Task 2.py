# json_handler.py

import json

def load_json(file_path):
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Ошибка загрузки JSON: {e}")
            return None

# Пример использования
data = load_json("data.json")
if data is not None:
    # Обработка данных
    # ...
