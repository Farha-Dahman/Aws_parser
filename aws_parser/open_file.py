def open_file(file_path):
    # Open the text file in read mode
    with open(file_path, 'r', encoding='utf-16') as file:
        # Read the contents of the file
        file_contents = file.read()
        return file_contents
    