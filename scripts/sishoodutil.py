from pathlib import Path

sh_path: Path = None
ks_path: Path = None

def update_paths(args: dict[str, any] = dict()) -> None:
    global sh_path
    global ks_path
    if "shdir" in args and args["shdir"] is not None:
        sh_path = Path(args["shdir"])
    else:
        sh_path = Path(__file__).parent.parent
    ks_path = sh_path.parent.parent
    print(f"Sisterhood-related paths updated: sh_path=\"{sh_path}\", ks_path=\"{ks_path}\"")

def resolve_path(plainpath: str) -> Path:
    # paths that start with a tilde (~) should be in reference to the katawa shoujo game directory
    if len(plainpath) > 0 and plainpath[0] == "~":
        return Path(ks_path, plainpath[1:])
    # otherwise, by default, paths will be in reference to the sisterhood directory
    else:
        return Path(sh_path, plainpath)

def relative_to_sh_path(path: Path) -> Path:
    return path.relative_to(sh_path)

def relative_to_ks_path(path: Path) -> Path:
    return path.relative_to(ks_path)

def sh_glob(pattern: str) -> list[Path]:
    return list(sh_path.glob(pattern))

def ks_glob(pattern: str) -> list[Path]:
    return list(ks_path.glob(pattern))