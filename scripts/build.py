from rpatool import RenPyArchive
from sishoodutil import sh_glob, relative_to_ks_path, resolve_path, update_paths
from pathlib import Path

INCLUDED_DIRS = ("bgm", "bgs", "event", "font", "gui", "logo", "sfx", "sprites", "vfx")

def get_project_files() -> list[Path]:
    files = []
    for dirname in INCLUDED_DIRS:
        for path in sh_glob(f"{dirname}/**/*.*"):
            files.append(path)
    for scriptpath in sh_glob("*.rpyc"):
        files.append(scriptpath)
    return files

def create_renpy_archive(files: list[Path]) -> RenPyArchive:
    archive = RenPyArchive()
    for file in files:
        with file.open("rb") as fp:
            relpath = relative_to_ks_path(file)
            print(f"Adding \"{relpath}\" to archive")
            archive.add(relpath, fp.read())
    return archive

def main():
    update_paths()
    files = get_project_files()
    archive = create_renpy_archive(files)
    archive.save(resolve_path("scripts/build/sisterhood.rpa"))
    
if __name__ == "__main__":
    main()