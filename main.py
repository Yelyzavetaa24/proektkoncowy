import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import asyncio
import tkinter as tk
from tkinter import filedialog

def parse_arguments():
    parser = argparse.ArgumentParser(description='Sample program')
    parser.add_argument('input_file', nargs='?', default='', help='Path to input file')
    parser.add_argument('output_file', nargs='?', default='', help='Path to output file')
    return parser.parse_args()

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

def save_json_data(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print('Error when saving data to a file')

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

def save_yaml_data(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except:
        print('Error when saving data to file')

def load_xml_data(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print('File not found')
        return None
    except ET.ParseError:
        print('Error in parsing the XML file')
        return None


def save_xml_data(data, file_path):
    try:
        tree = ET.ElementTree(data)
        tree.write(file_path)
    except:
        print('Error when saving data to file')


def run_with_ui():
    root = tk.Tk()

    def open_file():
        file_path = filedialog.askopenfilename()
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

    def save_file():
        file_path = filedialog.asksaveasfilename()
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

    def convert_files():
        input_file = input_entry.get()
        output_file = output_entry.get()

        json_data = load_json_data(input_file)
        if json_data:
            save_json_data(json_data, output_file)

        yaml_data = load_yaml_data(input_file)
        if yaml_data:
            save_yaml_data(yaml_data, output_file)

        xml_data = load_xml_data(input_file)
        if xml_data:
            save_xml_data(xml_data, output_file)

        root.destroy()

    input_label = tk.Label(root, text="Input File:")
    input_label.pack()
    input_entry = tk.Entry(root)
    input_entry.pack()
    input_button = tk.Button(root, text="Browse", command=open_file)
    input_button.pack()

    output_label = tk.Label(root, text="Output File:")
    output_label.pack()
    output_entry = tk.Entry(root)
    output_entry.pack()
    output_button = tk.Button(root, text="Browse", command=save_file)
    output_button.pack()

    convert_button = tk.Button(root, text="Convert", command=convert_files)
    convert_button.pack()

    root.mainloop()

async def load_and_save_data_async(input_file, output_file):
    loop = asyncio.get_event_loop()
    json_data = await loop.run_in_executor(None, load_json_data, input_file)
    if json_data:
        await loop.run_in_executor(None, save_json_data, json_data, output_file)

    yaml_data = await loop.run_in_executor(None, load_yaml_data, input_file)
    if yaml_data:
        await loop.run_in_executor(None, save_yaml_data, yaml_data, output_file)

    xml_data = await loop.run_in_executor(None, load_xml_data, input_file)
    if xml_data:
        await loop.run_in_executor(None, save_xml_data, xml_data, output_file)

def main():
    args = parse_arguments()

    input_file = args.input_file
    output_file = args.output_file

    if input_file and output_file:
        json_data = load_json_data(input_file)
        if json_data:
            save_json_data(json_data, output_file)

        yaml_data = load_yaml_data(input_file)
        if yaml_data:
            save_yaml_data(yaml_data, output_file)

        xml_data = load_xml_data(input_file)
        if xml_data:
            save_xml_data(xml_data, output_file)
    else:
        run_with_ui()

    if input_file and output_file:
        asyncio.run(load_and_save_data_async(input_file, output_file))

if __name__ == '__main__':
    main()
