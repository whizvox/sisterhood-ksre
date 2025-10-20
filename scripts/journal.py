from PIL.ImageFont import FreeTypeFont
from pathlib import Path
from argparse import ArgumentParser
import re
import sys

COMMON_FONT = FreeTypeFont("../../../font/playtime.ttf", 34)
ZH_FONT = FreeTypeFont("../../../font/XiaolaiSC-Regular.ttf", 34)
JP_FONT = FreeTypeFont("../../../font/VL-PGothic-Regular.ttf", 34)

LINES = 26
LINE_GAP = 0.034116
TOP = 0.075
LEFT = 0.19
LEFT_P2 = 0.57

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
    def __init__(self, image: str | None, text: str | None, xpos: float, ypos: float | None, yoff: float, xanchor: float, yanchor: float, gap: int, rotation: float):
        self.image = image
        self.text = text
        self.xpos = xpos
        self.ypos = ypos
        self.yoff = yoff
        self.xanchor = xanchor
        self.yanchor = yanchor
        self.gap = gap
        self.rotation = rotation

    def __str__(self):
        return f"EmbeddedImage(image={self.image}, text={self.text}, xpos={self.xpos}, ypos={self.ypos}, yoff={self.yoff}, gap={self.gap}, rotation={self.rotation})"

    def __repr__(self):
        return self.__str__()

    def get_type(self) -> str:
        return 't' if self.image is None else self.image[0]

    def is_relative(self) -> bool:
        return self.ypos is None

    def is_default_anchor(self):
        return self.xanchor == 0.5 and self.yanchor == 0


class Page:
    def __init__(self, text: str, images: list[Image]):
        self.text = text
        self.images = images

    def __str__(self):
        return f"Page(text={self.text}, images={self.images})"

    def __repr__(self):
        return self.__str__()


def parse_image(text: str) -> Image:
    tokens = text.split(",")
    # start of string, could contain commas
    if tokens[0][0].lstrip() == '"' and (tokens[0].rstrip()[-1] != '"' and not tokens[0].rstrip().endswith('\\"')):
        for i in range(1, len(tokens)):
            # in case there's a space after the double quote but before the comma
            temp = tokens[i].rstrip()
            # if ends with double quote and not escaped
            if not temp[-1] == '"' or temp.endswith('\\"'):
                tokens[0] += "," + tokens[i]
            else:
                tokens = [tokens[0] + ',' + temp] + tokens[i+1:]
                break
    tokens[0] = tokens[0].strip()
    for i in range(1, len(tokens)):
        tokens[i] = re.sub(r'\s', "", tokens[i])
    image = tokens[0]
    text = None
    if image[0] == '"' and image[-1] == '"':
        text = image[1:-1]
        image = None
    xpos = None
    ypos = None
    yoff = 0
    xanchor = 0.5
    yanchor = 0
    gap = None
    rotation = 0
    for token in tokens[1:]:
        if token.startswith("x="):
            xpos = float(token[2:])
        elif token.startswith("y="):
            ypos = float(token[2:])
        elif token.startswith("top="):
            yoff = float(token[4:]) * LINE_GAP
        elif token.startswith("px="):
            xanchor = float(token[3:])
        elif token.startswith("py="):
            yanchor = float(token[3:])
        elif token.startswith("gap="):
            gap = int(token[4:])
        elif token.startswith("rot="):
            rotation = float(token[4:])
        else:
            print(f"[WARN] Invalid property: {token}")
    if xpos is None:
        xpos = 0.5
    if gap is None:
        if image is None or image[0] == "d":
            gap = 5
        else:
            gap = 12
    return Image(image, text, xpos, ypos, yoff, xanchor, yanchor, gap, rotation)


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
                    img.ypos = 0.034116 * (get_text_lines(page, font) - 1) + 0.092058
                    # newline is added before the next bit of text
                    if img.gap > 1:
                        page += "\n" * (img.gap - 1)
                img.ypos += img.yoff
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
        if len(lines) > LINES:
            warnings.append(f"[#{i+1}] [+{len(lines)-LINES}] {lines[LINES]}")
    return warnings


def export_rpy_images(images: list[Image], xoff=0) -> str:
    imgstr = ""
    for img in images:
        if len(imgstr) > 0:
            imgstr += ",\n        "
        if img.is_default_anchor() and img.rotation == 0:
            anchorstr = ""
        else:
            anchorstr = f", {img.xanchor}, {img.yanchor}"
        if img.rotation == 0:
            rotatestr = ""
        else:
            rotatestr = f", {img.rotation}"
        imgtype = img.get_type()
        if imgtype == 'p':
            imgstr += f"(Composite((610, 410), (0, 0), f\"{{sh_path}}/gui/journal/dropshadow.png\", (5, 5), f\"{{sh_path}}/gui/journal/{img.image}.png\"), {xoff+img.xpos}, {img.ypos}{anchorstr}{rotatestr})"
        elif imgtype == 'd':
            imgstr += f"(Image(f\"{{sh_path}}/gui/journal/{img.image}.png\"), {xoff+img.xpos}, {img.ypos}{anchorstr}{rotatestr})"
        elif imgtype == 't':
            imgstr += f"(Text(\"{img.text}\", color=\"#000\"), {xoff+img.xpos}, {img.ypos}{anchorstr}{rotatestr})"
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
            img.xpos = round(0.19 + img.xpos * 0.3, 4)
            img.ypos = round(img.ypos, 4)
        if right < len(pages):
            righttext = pages[right].text.replace("\n", "\\n")
            callstr += f"\"{lefttext}\",\n    \"{righttext}\""
            rightimages = pages[right].images.copy()
            for img in rightimages:
                img.xpos = round(img.xpos * 0.3 + 0.57, 4)
                img.ypos = round(img.ypos, 4)
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


def write_script(script: str, lang: str):
    path = Path("../act2/script-ch28.rpy")
    if not path.exists():
        raise Exception(f"Script file \"{path}\" does not exist")
    newlines = []
    with path.open("r", encoding="utf-8") as file:
        in_label = False
        for line in file.readlines():
            line = line.rstrip("\r\n")
            if in_label:
                if line.startswith("label sh_ch28_journal_"):
                    in_label = False
            elif line.startswith(f"label sh_ch28_journal_{lang}:"):
                in_label = True
                newlines.append(line + "\n")
                for scriptline in script.splitlines():
                    if scriptline == "":
                        newlines.append("\n")
                    else:
                        newlines.append("    " + scriptline + "\n")
            if not in_label:
                newlines.append(line + "\n")
    with path.open("w", encoding="utf-8") as file:
        file.writelines(newlines)


def print_header(header: str):
    print("┏" + ("━" * (len(header) + 2)) + "┓")
    print("┃ " + header + " ┃")
    print("┗" + ("━" * (len(header) + 2)) + "┛")


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
        print_header(f"EXPORTING {args['lang']} JOURNAL")
        print()
        script = export_rpy(parse_journal(text, font))
        try:
            write_script(script, args["lang"])
        except Exception as e:
            print("ERROR: Could not write journal")
            print(e)
        print()
        print_header("FINISH EXPORT")
    elif args["action"] == "print":
        print_header(f"PRINTING {args['lang']} JOURNAL")
        print()
        print(export_rpy(parse_journal(text, font)))
        print()
        print_header("FINISH PRINT")
    else:
        print_header(f"VERIFYING {args['lang']} JOURNAL")
        print()
        print("\n".join(verify_pages(parse_journal(text, font), font)))
        print()
        print_header("FINISH VERIFY")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-a", "--action", choices=["export", "print", "verify"], default="export")
    parser.add_argument("-f", "--font", choices=["common", "zh", "jp"], default="common")
    parser.add_argument("-l", "--lang", default="en")
    main(vars(parser.parse_args(sys.argv[1:])))
