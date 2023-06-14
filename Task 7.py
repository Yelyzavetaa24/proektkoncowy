# xml_handler.py

import xml.etree.ElementTree as ET

def save_xml(root, file_path):
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

# Пример использования
root = ET.Element("root")
tree = ET.ElementTree(root)
save_xml(tree, "data.xml")
