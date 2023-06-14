# yaml_handler.py

import yaml

def save_yaml(data, file_path):
    with open(file_path, "w") as file:
        yaml.dump(data, file)

# Пример использования
data = {"key": "value"}
save_yaml(data, "data.yml")
