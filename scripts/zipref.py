# used to zip and unzip the reference files
from zipfile import ZipFile
import os
import shutil
import sys

def create_zip(dir_in_path: str, zip_out_path: str) -> None:
    dir_in_path = os.path.abspath(dir_in_path)
    if not os.path.exists(dir_in_path):
        print(f"ERROR: Directory <{dir_in_path}> does not exist")
        return
    if not os.path.isdir(dir_in_path):
        print(f"ERROR: <{dir_in_path}> is actually a file")
        return
    files_to_zip = []
    for root, dirs, files in os.walk(dir_in_path):
        for file_path in files:
            files_to_zip.append(os.path.join(root, file_path))
    with ZipFile(zip_out_path, 'w') as zip:
        print(f"Writing to zip file <{zip_out_path}>...")
        for file_path in files_to_zip:
            print(f"\tWriting file <{file_path}> to zip")
            zip.write(file_path)

def extract_zip(zip_in_path: str, dir_out_path: str, clean_before: bool = False) -> None:
    if not os.path.exists(zip_in_path):
        print(f"ERROR: Zip file <{zip_in_path}> does not exist")
        return
    if clean_before:
        print(f"Cleaning contents of {dir_out_path} first")
        for file_name in os.listdir(dir_out_path):
            file_path = os.path.join(dir_out_path, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except OSError as e:
                print(f"Could not delete <{file_path}>: {e}")
    with ZipFile(zip_in_path, 'r') as zip:
        print(f"Extacting contents of <{zip_in_path}>")
        zip.extractall(dir_out_path)

def _print_usage():
    print(f"USAGE: {sys.argv[0]} <zip|unzip> [--clean]")

_REF_LOCATION = "game/mods/sisterhood/reference"
_ZIP_LOCATION = "game/mods/sisterhood/reference.zip"

def main():
    if len(sys.argv) < 2:
        _print_usage()
        return
    if sys.argv[1] == "unzip":
        extract_zip(_ZIP_LOCATION, _REF_LOCATION, False)
    elif sys.argv[1] == "zip":
        create_zip(_REF_LOCATION, _ZIP_LOCATION)
    else:
        _print_usage()

if __name__ == "__main__":
    main()