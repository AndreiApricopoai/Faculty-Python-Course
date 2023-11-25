# Ex4 - Write a Python script that counts the number of files with each
# extension in a given directory. The script should:
# * Accept a directory path as a command line argument (using sys.argv).
# * Use the os module to list all files in the directory.
# * Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
# * Include error handling for scenarios such as the directory not being found,
# no read permissions, or the directory being empty.


import os
import sys


def count_files_by_extension(directory_path):
    if not os.path.exists(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory.")
        return

    extension_count = {}
    try:
        for item in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, item)):
                name, extension = os.path.splitext(item)
                if extension in extension_count:
                    extension_count[extension] += 1
                else:
                    extension_count[extension] = 1

        if not extension_count:
            print("The directory is empty or contains no files.")
            return

        for ext, count in extension_count.items():
            print(f"Extension '{ext}': {count} file(s)")

    except PermissionError:
        print(f"Error: No permission to read the directory '{directory_path}'.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex4.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    count_files_by_extension(directory_path)


if __name__ == "__main__":
    main()
