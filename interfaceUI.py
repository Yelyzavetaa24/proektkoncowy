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
