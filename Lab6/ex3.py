# Ex3 - Create a Python script that calculates the total size
# of all files in a directory provided as a command line argument.
# The script should:
# * Use the sys module to read the directory path from the command line.
# * Utilize the os module to iterate through all the files in the given directory and its subdirectories.
# * Sum up the sizes of all files and display the total size in bytes.
# * Implement exception handling for cases like the directory not existing,
# permission errors, or other file access issues.


import os
import sys


def calculate_total_size(directory_path):
    total_size = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                total_size += os.path.getsize(file_path)
            except OSError as e:
                print(f"Error accessing file {file_path}: {e}")

    return total_size


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex3.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        sys.exit(1)

    try:
        total_size = calculate_total_size(directory_path)
        print(f"Total size of all files: {total_size} bytes")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
