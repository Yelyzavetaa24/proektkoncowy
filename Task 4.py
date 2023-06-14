# yaml_handler.py

import yaml

def load_yaml(file_path):
    with open(file_path, "r") as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Ошибка загрузки YAML: {e}")
            return None

# Пример использования
data = load_yaml("data.yml")
if data is not None:
    # Обработка данных
    # ...
