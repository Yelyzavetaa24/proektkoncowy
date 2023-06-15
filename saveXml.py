def save_xml_data(data, file_path):
    try:
        tree = ET.ElementTree(data)
        tree.write(file_path)
    except:
        print('Error when saving data to file')
