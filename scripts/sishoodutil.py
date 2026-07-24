import os
from argparse import ArgumentParser
from pathlib import Path

sh_path: Path = Path(".")
ks_path: Path = Path(".")
ref_path: Path = Path(".")
_last_printr_msg_len = 0


def add_arguments(
    parser: ArgumentParser,
    shdir=True,
    ksdir=True,
    refdir=False,
):
    if shdir:
        parser.add_argument(
            "-s",
            "--shdir",
            required=True,
            help="location of Sisterhood project directory",
        )
    if ksdir:
        parser.add_argument(
            "-k",
            "--ksdir",
            required=True,
            help="location of Katawa Shoujo: Re-Engineered project directory",
        )
    if refdir:
        parser.add_argument(
            "-r",
            "--refdir",
            required=True,
            help="location of the Sisterhood reference directory",
        )


def update_paths(args: dict = dict()) -> None:
    global sh_path
    global ks_path
    global ref_path

    if "shdir" in args and args["shdir"] is not None:
        sh_path = Path(args["shdir"])
    else:
        sh_path = Path(__file__).parent.parent
    if "ksdir" in args and args["ksdir"] is not None:
        ks_path = Path(args["ksdir"])
    else:
        ks_path = sh_path.parent.parent
    if "refdir" in args and args["refdir"] is not None:
        ref_path = Path(args["refdir"])

    if not (sh_path / "fireflies.rpy").exists():
        raise Exception(
            f'sh_path "{sh_path}" is not a valid Sisterhood directory'
        )
    if not (ks_path / "game").exists():
        raise Exception(f'ks_path "{ks_path}" is not a valid KS:RE directory')

    print(f"""Sisterhood-related paths updated:
    \tsh_path={sh_path}
    \tks_path={ks_path}
    \tref_path={ref_path}""")


def resolve_path(plainpath: str) -> Path:
    # paths that start with a tilde (~) should be in reference to the katawa shoujo game directory
    if len(plainpath) > 0 and plainpath[0] == "~":
        return Path(ks_path, plainpath[1:])
    # paths starting with @ should be in reference to the reference directory
    if len(plainpath) > 0 and plainpath[0] == "@":
        return Path(ref_path, plainpath[1:])
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
