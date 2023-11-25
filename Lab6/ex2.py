# Ex2 - Write a script using the os module that renames all files in a specified
# directory to have a sequential number prefix. For example, file1.txt, file2.txt, etc.
# Include error handling for cases like the directory not existing or files that can't be renamed.


import os
import sys


def rename_files(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    try:
        directory_contents = os.listdir(directory_path)

        files = []
        for entry in directory_contents:
            full_entry_path = os.path.join(directory_path, entry)
            if os.path.isfile(full_entry_path):
                files.append(entry)

        files.sort()

        for i, filename in enumerate(files, start=1):
            new_filename = f"{i}_{filename}"

            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_filename)

            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except OSError as e:
                print(f"Error renaming file {filename}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex2.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    rename_files(directory_path)


if __name__ == "__main__":
    main()
