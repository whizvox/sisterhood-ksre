from rpatool import RenPyArchive
from sishoodutil import sh_glob, relative_to_ks_path, resolve_path, update_paths, relative_to_sh_path
from pathlib import Path
from zipfile import ZipFile
import argparse
import sys

INCLUDED_DIRS = ("bgm", "bgs", "event", "font", "gui", "logo", "sfx", "sprites", "vfx")

def get_project_files() -> list[Path]:
    files = []
    for dirname in INCLUDED_DIRS:
        for path in sh_glob(f"{dirname}/**/*.*"):
            files.append(path)
    for scriptpath in sh_glob("tl/**/*.rpyc"):
        files.append(scriptpath)
    for scriptpath in sh_glob("*.rpyc"):
        files.append(scriptpath)
    return files


def create_rpa(files: list[Path]) -> RenPyArchive:
    archive = RenPyArchive()
    for file in files:
        with file.open("rb") as fp:
            relpath = Path("mods/sisterhood") / relative_to_sh_path(file)
            print(f"Adding \"{relpath}\" to archive")
            archive.add(relpath, fp.read())
    return archive


def write_to_zip(files: list[Path], zip: ZipFile) -> None:
    for file in files:
        zip.write(str(file.absolute), str(relative_to_ks_path(file)))


def main(args: dict[str, any]):
    update_paths(args)
    build_dir = Path(args["builddir"])
    files = get_project_files()
    if args["archive"] == "rpa":
        archive = create_rpa(files)
        archive.save(build_dir / "sisterhood.rpa")
    elif args["archive"] == "zip":
        with ZipFile(build_dir / "sisterhood.zip") as zip:
            for file in files:
                zip.write(str(file.absolute), str(relative_to_ks_path(file)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="build")
    parser.add_argument("-a", "--archive", choices=["rpa", "zip"], default="rpa")
    parser.add_argument("-s", "--shdir", required=True, help="location of Sisterhood root project directory")
    parser.add_argument("-k", "--ksdir", required=True, help="location of KS:RE root project directory")
    parser.add_argument("-b", "--builddir", required=True, help="location of build directory")
    main(vars(parser.parse_args(sys.argv[1:])))
