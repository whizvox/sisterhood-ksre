from PIL.ImageFont import FreeTypeFont
from pathlib import Path
from argparse import ArgumentParser
import re
import sys

COMMON_FONT = FreeTypeFont("../../../font/playtime.ttf", 34)
ZH_FONT = FreeTypeFont("../../../font/XiaolaiSC-Regular.ttf", 34)
JP_FONT = FreeTypeFont("../../../font/VL-PGothic-Regular.ttf", 34)

def word_wrap_text(text: str, font: FreeTypeFont) -> int:
    lines = []
    for line in text.split("\n"):
        currlines = [""]
        for word in line.split():
            line = f"{currlines[-1]} {word}".strip()
            bbox = font.getbbox(line)
            if bbox[2] > 576:
                currlines.append(word)
            else:
                currlines[-1] = line
        lines.extend(currlines)
    return lines


def get_text_lines(text: str, font: FreeTypeFont) -> int:
    return len(word_wrap_text(text, font))


class Image:
    def __init__(self, image: str, xpos: float, ypos: float | None, gap: int, rotation: float):
        self.image = image
        self.xpos = xpos
        self.ypos = ypos
        self.gap = gap
        self.rotation = rotation

    def __str__(self):
        return f"EmbeddedImage(image={self.image}, xpos={self.xpos}, ypos={self.ypos}, gap={self.gap}, rotation={self.rotation})"

    def __repr__(self):
        return self.__str__()
    
    def is_picture(self) -> bool:
        return self.image[0] == 'p'

    def is_relative(self) -> bool:
        return self.ypos is None


class Page:
    def __init__(self, text: str, images: list[Image]):
        self.text = text
        self.images = images

    def __str__(self):
        return f"Page(text={self.text}, images={self.images})"

    def __repr__(self):
        return self.__str__()


def parse_image(text: str) -> Image:
    text = re.sub(r'\s', "", text)
    tokens = text.split(",")
    image = tokens[0]
    xpos = None
    ypos = None
    gap = None
    rotation = 0
    for token in tokens[1:]:
        if token.startswith("x="):
            xpos = float(token[2:])
        elif token.startswith("y="):
            ypos = float(token[2:])
        elif token.startswith("gap="):
            gap = int(token[4:])
        elif token.startswith("rot="):
            rotation = float(token[4:])
        else:
            print(f"[WARN] Invalid property: {token}")
    if xpos is None:
        if image[0] == "d":
            xpos = 0.2
        else:
            xpos = 0.14
    if gap is None:
        if image[0] == "d":
            gap = 5
        else:
            gap = 12
    return Image(image, xpos, ypos, gap, rotation)


def parse_journal(text: str, font: FreeTypeFont) -> list[Page]:
    text = text.replace("\r", "")
    pages: list[Page] = []
    images: list[Image] = []
    page = ""
    for line in text.split("\n"):
        line = line.strip()
        if line == "":
            continue
        if line == "===":
            pages.append(Page(page, images))
            page = ""
            images = []
        else:
            is_header = False
            if page == "":
                if line.startswith("#"):
                    line = line[1:].lstrip()
                    is_header = True
                else:
                    page += "\n\n"
            else:
                page += "\n"
            if line.startswith("!{") and line[-1] == "}":
                img = parse_image(line[2:-1])
                if img.is_relative():
                    img.ypos = 0.03558 * (get_text_lines(page, font) - 1) + 0.075
                    if img.gap > 0:
                        page += "\n" * img.gap
                images.append(img)
            else:
                page += line
            if is_header:
                page += "\n"
    pages.append(Page(page, images))
    return pages


def read_journal_file(file_path: str, font: FreeTypeFont) -> list[Page]:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()
    return parse_journal(text, font)


def verify_pages(pages: list[Page], font: FreeTypeFont) -> list[str]:
    warnings = []
    for i, page in enumerate(pages):
        lines = word_wrap_text(page.text, font)
        if len(lines) > 26:
            warnings.append(f"[#{i+1}] [+{len(lines)-26}] {lines[26]}")
    return warnings


def export_rpy_images(images: list[Image], xoff=0) -> str:
    imgstr = ""
    for img in images:
        if len(imgstr) > 0:
            imgstr += ",\n        "
        if img.is_picture():
            imgstr += f"(Composite((610, 410), (0, 0), f\"{{sh_path}}/gui/journal/dropshadow.png\", (5, 5), f\"{{sh_path}}/gui/journal/{img.image}.png\"), {xoff+img.xpos}, {img.ypos})"
        else:
            imgstr += f"(Image(f\"{{sh_path}}/gui/journal/{img.image}.png\"), {xoff+img.xpos}, {img.ypos})"
    return imgstr


def export_rpy(pages: list[Page]) -> str:
    calls: list[str] = []
    for i in range(len(pages) // 2):
        callstr = "call screen sh_journal(\n    "
        left = i * 2
        right = i * 2 + 1
        lefttext = pages[left].text.replace("\n", "\\n")
        leftimages = pages[left].images.copy()
        for img in leftimages:
            img.xpos = round(img.xpos / 2, 2)
            img.ypos = round(img.ypos, 2)
        if right < len(pages):
            righttext = pages[right].text.replace("\n", "\\n")
            callstr += f"\"{lefttext}\",\n    \"{righttext}\""
            rightimages = pages[right].images.copy()
            for img in rightimages:
                img.xpos = round(img.xpos / 2 + 0.5, 2)
                img.ypos = round(img.ypos, 2)
            imgstr = export_rpy_images(leftimages + rightimages)
        else:
            callstr += f"\"{lefttext}\""
            imgstr = export_rpy_images(leftimages)
        if len(imgstr) > 0:
            callstr += f",\n    [\n        {imgstr}\n    ]"
        callstr += "\n)"
        if len(calls) == 0:
            callstr += " with dissolve"
        calls.append(callstr)
    return "\n\n".join(calls)


def main(args: dict[str, any]):
    file_path = f"journal/{args['lang']}.txt"
    if not Path(file_path).exists():
        print(f"[ERROR] Unknown journal entry: {file_path}")
        return
    if args["font"] == "zh":
        font = ZH_FONT
    elif args["font"] == "jp":
        font = JP_FONT
    else:
        font = COMMON_FONT
    with open(file_path, encoding="utf-8") as file:
        text = file.read()
    if args["action"] == "export":
        print("=" * 20)
        print(f"  EXPORTING {args['lang']} JOURNAL")
        print("=" * 20)
        print()
        print(export_rpy(parse_journal(text, font)))
        print()
        print("=" * 20)
        print(f"  FINISH EXPORT")
        print("=" * 20)
    else:
        print("=" * 20)
        print(f"  VERIFYING {args['lang']} JOURNAL")
        print("=" * 20)
        print()
        print("\n".join(verify_pages(parse_journal(text, font), font)))
        print()
        print("=" * 20)
        print(f"  FINISH VERIFY")
        print("=" * 20)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-a", "--action", choices=["export", "verify"], default="export")
    parser.add_argument("-f", "--font", choices=["common", "zh", "jp"], default="common")
    parser.add_argument("-l", "--lang", default="en")
    main(vars(parser.parse_args(sys.argv[1:])))
