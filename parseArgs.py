def parse_arguments():
    parser = argparse.ArgumentParser(description='Sample program')
    parser.add_argument('input_file', nargs='?', default='', help='Path to input file')
    parser.add_argument('output_file', nargs='?', default='', help='Path to output file')
    return parser.parse_args()
  
