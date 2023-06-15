def save_yaml_data(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except:
        print('Error when saving data to file')
