import argparse
import os
import re
import sys
import tarfile
from pathlib import Path

from rpatool import RenPyArchive
from sishoodutil import (
    printr,
    printr_end,
    relative_to_sh_path,
    resolve_path,
    sh_glob,
    update_paths,
)
from zipfile_xz import ZIP_XZ, ZipFile  # pyright: ignore[reportAttributeAccessIssue]

INCLUDED_DIRS = (
    "bgm",
    "bgs",
    "event",
    "font",
    "gui",
    "logo",
    "sfx",
    "vfx",
)
SCRIPT_DIRS = ("act1", "act2")


def format_bytes(n: int) -> str:
    if n < 1000:
        return f"{n} B"
    elif n < 1_000_000:
        return "{:.1f}".format(n / 1000) + " KB"
    elif n < 1_000_000_000:
        return "{:.1f}".format(n / 1_000_000) + " MB"
    else:
        return "{:.1f}".format(n / 1_000_000_000) + " GB"


# attempt to be smart and only include sprites that are actually used in the game in the distributable
def find_used_sprites(script_path: Path, valid_chars: list[str]) -> set[Path]:
    global ks_path
    sprite_paths: set[Path] = set()
    with script_path.open(encoding="utf-8") as file:
        linenum = 0
        for line in file.readlines():
            linenum += 1
            line = line.strip()
            m = re.search(r"^show ([a-zA-Z_]\w*) ([a-zA-Z_]\w*)", line)
            if m is not None:
                char = m.group(1)
                sprite = m.group(2)
                if (
                    char in valid_chars
                    and sprite not in ["at", "behind", "zorder"]
                    and not sprite.endswith("_blur1")
                    and not sprite.endswith("_blur2")
                ):
                    if (
                        sprite.endswith("_ss")
                        or sprite.endswith("_ni")
                        or sprite.endswith("_rn")
                    ):
                        sprite = sprite[:-3]
                    if sprite.endswith("_phone"):
                        sprite = sprite[:-6]
                    if sprite.endswith("_close"):
                        end_path = f"close/{char}_{sprite}"
                    elif sprite.endswith("_superclose"):
                        end_path = f"superclose/{char}_{sprite}"
                    else:
                        end_path = f"{char}_{sprite}"
                    sprite_path = resolve_path(f"sprites/{char}/{end_path}.png")
                    if sprite_path.exists():
                        sprite_paths.add(sprite_path)
                    else:
                        sprite_path2 = resolve_path(
                            f"~game/sprites/{char}/{end_path}.png"
                        )
                        if not sprite_path2.exists():
                            print(
                                f"Could not find sprite referenced by {relative_to_sh_path(script_path)}:{linenum} - {line}"
                            )
    return sprite_paths


def get_project_files(include_all_sprites: bool = False) -> list[Path]:
    files = []
    for dirname in INCLUDED_DIRS:
        for path in sh_glob(f"{dirname}/**/*.*"):
            files.append(path)
    # don't include incomplete translations
    # for scriptpath in sh_glob("tl/**/*.rpyc"):
    #     files.append(scriptpath)
    if include_all_sprites:
        for path in sh_glob("sprites/**/*.*"):
            files.append(path)
        for dirname in SCRIPT_DIRS:
            for path in sh_glob(f"{dirname}/**/*.rpyc"):
                files.append(path)
        for path in sh_glob("*.rpyc"):
            files.append(path)
    else:
        sprite_files = set()
        valid_chars = []
        # only worry about character sprites that are unique to Sisterhood
        for sprite_char_dir in sh_glob("sprites/*"):
            valid_chars.append(sprite_char_dir.name)
        for dirname in SCRIPT_DIRS:
            for path in sh_glob(f"{dirname}/**/*.rpyc"):
                files.append(path)
                rpy_path = Path(str(path)[:-1])
                if rpy_path.exists():
                    sprite_files.update(find_used_sprites(rpy_path, valid_chars))
                else:
                    print(
                        f"[ERROR] Could not find script file for {relative_to_sh_path(path)}"
                    )
        for path in sh_glob("*.rpyc"):
            files.append(path)
            rpy_path = Path(str(path)[:-1])
            if rpy_path.exists():
                sprite_files.update(find_used_sprites(rpy_path, valid_chars))
            else:
                print(
                    f"[ERROR] Could not find script file for {relative_to_sh_path(path)}"
                )
        saved_files = 0
        saved_space = 0
        for path in sh_glob("sprites/**/*.*"):
            if path not in sprite_files:
                saved_files += 1
                saved_space += path.stat().st_size
        print(f"Skipped {saved_files} sprites and saved {format_bytes(saved_space)}")
        files.extend(sprite_files)
    return files


def create_rpa(files: list[Path]) -> RenPyArchive:
    archive = RenPyArchive()
    cur_index = 0
    printr()
    for file in files:
        cur_index += 1
        with file.open("rb") as fp:
            relpath = Path("game/mods/sisterhood") / relative_to_sh_path(file)
            printr(f'({cur_index}/{len(files)}) Adding "{relpath}" to archive')
            archive.add(relpath, fp.read())
    printr_end("Finished constructing Ren'Py archive")
    return archive


def write_to_zip(files: list[Path]):
    out_path = resolve_path("scripts/build/sisterhood.zip")
    with ZipFile(out_path, mode="w", compression=ZIP_XZ, compresslevel=9) as zip:
        cur_file = 0
        for file in files:
            cur_file += 1
            cur_path = Path("sisterhood") / relative_to_sh_path(file)
            printr(f"({cur_file}/{len(files)}) Writing {cur_path} to zip")
            zip.write(str(file.absolute()), str(cur_path))
    printr_end(f"Finished writing zip to {out_path}")


def write_to_zipped_rpa(files: list[Path]):
    rpa_path = resolve_path("scripts/build/sisterhood.rpa")
    archive = create_rpa(files)
    archive.save(rpa_path)
    out_path = resolve_path("scripts/build/sisterhood.zip")
    with ZipFile(out_path, mode="w", compression=ZIP_XZ, compresslevel=9) as zip:
        printr(f"Writing {rpa_path} to zip")
        zip.write(str(rpa_path.absolute()), "sisterhood.rpa")
    printr_end(f"Finished writing zip to {out_path}")


def write_to_tar(files: list[Path]):
    out_path = resolve_path("scripts/build/sisterhood.tar.xz")
    if out_path.exists():
        out_path.unlink()
    with tarfile.open(out_path, "x:xz") as tar:
        cur_file = 0
        for file in files:
            cur_file += 1
            cur_path = Path("sisterhood") / relative_to_sh_path(file)
            printr(f"({cur_file}/{len(files)}) Writing {cur_path} to tarball")
            tar.add(file, str(cur_path))
    printr_end(f"Finished writing tarball to {out_path}")


def main(args: dict):
    update_paths(args)
    include_all_sprites = args["allsprites"]
    files = get_project_files(include_all_sprites)
    os.makedirs(resolve_path("scripts/build"), exist_ok=True)
    if args["archive"] == "rpa":
        archive = create_rpa(files)
        out_path = resolve_path("scripts/build/sisterhood.rpa")
        archive.save(out_path)
        print(f"Saved Ren'Py archive to {out_path}")
    elif args["archive"] == "zip":
        write_to_zip(files)
    elif args["archive"] == "tar":
        write_to_tar(files)
    elif args["archive"] == "rpazip":
        write_to_zipped_rpa(files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="build")
    parser.add_argument(
        "-s", "--shdir", required=True, help="location of Sisterhood project directory"
    )
    parser.add_argument(
        "-k",
        "--ksdir",
        required=True,
        help="location of Katawa Shoujo: Re-Engineered project directory",
    )
    parser.add_argument(
        "-a", "--archive", choices=["rpa", "zip", "tar", "rpazip"], default="rpa"
    )
    parser.add_argument(
        "-A", "--allsprites", action="store_const", const=True, default=False
    )
    main(vars(parser.parse_args(sys.argv[1:])))
