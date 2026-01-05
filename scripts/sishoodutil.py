import os
from pathlib import Path

sh_path: Path = Path(".")
ks_path: Path = Path(".")
_last_printr_msg_len = 0


def update_paths(args: dict = dict()) -> None:
    global sh_path
    global ks_path
    if "shdir" in args and args["shdir"] is not None:
        sh_path = Path(args["shdir"])
    else:
        sh_path = Path(__file__).parent.parent
    if "ksdir" in args and args["ksdir"] is not None:
        ks_path = Path(args["ksdir"])
    else:
        ks_path = sh_path.parent.parent
    if not (sh_path / "fireflies.rpy").exists():
        raise Exception(f'sh_path "{sh_path}" is not a valid Sisterhood directory')
    if not (ks_path / "game").exists():
        raise Exception(f'ks_path "{ks_path}" is not a valid KS:RE directory')
    print(f'Sisterhood-related paths updated: sh_path="{sh_path}", ks_path="{ks_path}"')


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


def printr(msg: str | None = None):
    width, _ = os.get_terminal_size()
    global _last_printr_msg_len
    if msg is None:
        _last_printr_msg_len = 0
    else:
        if len(msg) >= width:
            msg = msg[: width - 4] + "..."
        print(msg, " " * (_last_printr_msg_len - len(msg)), end="\r")
        _last_printr_msg_len = len(msg)


def printr_end(msg: str):
    global _last_printr_msg_len
    print(msg, " " * (_last_printr_msg_len - len(msg)))
    _last_printr_msg_len = 0
