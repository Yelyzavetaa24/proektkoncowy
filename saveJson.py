def save_json_data(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print('Error when saving data to a file')
