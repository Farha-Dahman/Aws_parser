import json

def convert_to_json(parsed_info, output_file):
    # Save the dictionary to json file
    with open(output_file, 'w') as f:
        json.dump(parsed_info, f, indent=4)