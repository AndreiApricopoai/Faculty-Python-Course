# Ex1 - Create a Python script that does the following:
# * Takes a directory path and a file extension as command line arguments (use sys.argv).
# * Searches for all files with the given extension in the specified directory (use os module).
# * For each file found, read its contents and print them.
# * Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.

import os
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python ex1.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path, file_extension = sys.argv[1], sys.argv[2]

    if not os.path.isdir(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        sys.exit(1)

    if not file_extension.startswith('.'):
        file_extension = '.' + file_extension

    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            print(f"\nContents of {file_path}:")
                            print(f.read())
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
