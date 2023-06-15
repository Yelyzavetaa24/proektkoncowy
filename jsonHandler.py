def load_json_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('File not found')
        return None
    except json.JSONDecodeError:
        print('Error when parsing a JSON file')
        return None
