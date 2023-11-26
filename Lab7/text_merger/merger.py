def merge_files(file_list, output_file, separator=''):
    with open(output_file, 'w') as outfile:
        for i, file_path in enumerate(file_list):
            with open(file_path, 'r') as infile:
                outfile.write(infile.read())
                if i < len(file_list) - 1:
                    outfile.write(separator)
