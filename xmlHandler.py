def load_xml_data(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print('Файл не найден')
        return None
    except ET.ParseError:
        print('Ошибка при разборе файла XML')
        return None
