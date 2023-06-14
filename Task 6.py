# xml_handler.py

import xml.etree.ElementTree as ET

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Ошибка загрузки XML: {e}")
        return None

# Пример использования
root = load_xml("data.xml")
if root is not None:
    # Обработка данных
    # ...
