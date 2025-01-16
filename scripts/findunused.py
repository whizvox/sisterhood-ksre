from pathlib import Path
from sishoodutil import update_paths, resolve_path, sh_glob

blacklist = ["", "bg", "ev", "black", "hanako", "hisao", "lilly", "naomi", "natsume", "takawa", "kenji", "hanagown", "emi"]

def find_usages() -> dict[str, list[tuple[str, int]]]:
    all_usages = {}
    for scriptpath in sh_glob("script-*.rpy"):
        with scriptpath.open(mode="r", encoding="utf-8") as script:
            linenum = 0
            for line in script:
                linenum += 1
                line = line.strip()
                asset = None
                if line.startswith("show") or line.startswith("scene"):
                    asset = line[line.find(" ")+1:]
                    if " at " in asset:
                        asset = asset[0:asset.find(" at ")]
                    if " behind " in asset:
                        asset = asset[0:asset.find(" behind ")]
                    if "#" in asset:
                        asset = asset[0:asset.find("#")]
                    if asset.endswith(":"):
                        asset = asset[0:-1]
                    if (not asset.startswith("bg ") and not asset.startswith("ev ")) and (asset.endswith("_ni") or asset.endswith("_rn") or asset.endswith("_ss")):
                        asset = asset[0:-3]
                elif line.startswith("play") or line.startswith("queue"):
                    asset = line[line.find(" ")+1:]
                    if asset.startswith("music ") or asset.startswith("sound "):
                        asset = asset[6:]
                    if asset.startswith("ambient "):
                        asset = asset[8:]
                    if " fadein " in asset:
                        asset = asset[0:asset.find(" fadein ")]
                    if " fadeout " in asset:
                        asset = asset[0:asset.find(" fadeout ")]
                    if " volume " in asset:
                        asset = asset[0:asset.find(" volume ")]
                    if asset.endswith(" loop"):
                        asset = asset[0:-5]
                    if asset.endswith(" noloop"):
                        asset = asset[0:-7]
                if asset not in blacklist and asset is not None:
                    usages = None
                    if asset in all_usages:
                        usages = all_usages[asset]
                    else:
                        usages = []
                        all_usages[asset] = usages
                    usages.append((scriptpath.name, linenum))
    return all_usages

def get_all_assets() -> list[tuple[str, str, Path]]:
    assets = []
    # bgm
    assets.append(("bgm", "music_waltz", resolve_path("bgm/Waltz_in_A_Minor.ogg")))
    assets.append(("bgm", "music_bloom", resolve_path("bgm/Bloom.ogg")))
    # bgs
    for bgpath in sh_glob("bgs/**/*.jpg"):
        assets.append(("bg", "bg " + bgpath.stem, bgpath))
    # events
    for evpath in sh_glob("event/**/*.jpg"):
        assets.append(("ev", "ev " + evpath.stem, evpath))
    # sfx
    for sfxpath in sh_glob("sfx/**/*.ogg"):
        assets.append(("sfx", "sfx_" + sfxpath.stem, sfxpath))
    # sprites
    for spritepath in sh_glob("sprites/**/*.png"):
        stem = spritepath.stem
        name = stem[0:stem.find("_")]
        variant = stem[stem.find("_")+1:]
        assets.append(("sprite", name + " " + variant, spritepath))
    return assets

def main(args: dict[str, any] = dict()) -> None:
    import json
    usages = find_usages()
    usagesfile = resolve_path("scripts/usages.json")
    with usagesfile.open("w", encoding="utf-8") as fp:
        json.dump(usages, fp, indent=4)
    assets = get_all_assets()
    for asset in assets:
        kind = asset[0]
        id = asset[1]
        path = asset[2]
        if id not in usages:
            if kind == "sprite":
                print(f"DELETING {path}")
                path.unlink()

if __name__ == "__main__":
    update_paths()
    main()