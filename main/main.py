import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)
from aws_parser.open_file import open_file
from aws_parser.parser_scripts.parser_regex import parser_regex
from aws_parser.convert_to_json import convert_to_json

def main():
    file_path = "aws_parser\\receipts\\receipt.txt"
    output_file = 'parsed_data.json'
    # call functions
    file_contents = open_file(file_path)
    parsed_info = parser_regex(file_contents)
    convert_to_json(parsed_info, output_file)

if __name__ == "__main__":
    main()