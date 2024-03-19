import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)
from aws_parser.open_file import open_file
from aws_parser.parser_scripts.parser_regex import parser_regex
from aws_parser.parser_scripts.parser_splitter import parser_splitter
from aws_parser.convert_to_json import convert_to_json

def main():
    file_path = "aws_parser\\receipts\\receipt.txt"
    output_file = 'parsed_data.json'

    # Prompt the user to choose the parser type
    parser_type = input("Choose parser type ('regex' or 'splitter'): ").strip().lower()

    # Validate the user input
    if parser_type not in ['regex', 'splitter']:
        raise ValueError("Invalid parser type specified")

    # Call functions based on parser type
    file_contents = open_file(file_path)
    if parser_type == 'regex':
        parsed_info = parser_regex(file_contents)
    elif parser_type == 'splitter':
        parsed_info = parser_splitter(file_contents)
    else:
        raise ValueError("Invalid parser type specified")

    # Convert the parsed data to json format
    convert_to_json(parsed_info, output_file)

if __name__ == "__main__":
    main()