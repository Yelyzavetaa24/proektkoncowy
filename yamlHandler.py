def load_yaml_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print('File not found')
        return None
    except yaml.YAMLError:
        print('Error in parsing the YAML file')
        return None
