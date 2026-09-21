import sys
from pathlib import Path
from argparse import ArgumentParser
from sishoodutil import add_arguments

def find_rpyc_files(dir: Path) -> list[Path]:
    return [filepath for filepath in dir.glob("**/*.rpyc")]

def clean_rpyc_files(dir: Path):
    for filepath in find_rpyc_files(dir):
        print(f"Deleting file at {filepath}")
        filepath.unlink()

def main(args: dict):
    shdir = Path(args["shdir"])
    if args["list"]:
        for filepath in find_rpyc_files(shdir):
            print(f"Found file at {filepath}")
    else:
        clean_rpyc_files(shdir)

if __name__ == "__main__":
    parser = ArgumentParser()
    add_arguments(parser, ksdir=False)
    parser.add_argument("-l", "--list", action='store_true', help="only list files, don't delete anything")
    main(vars(parser.parse_args(sys.argv[1:])))
