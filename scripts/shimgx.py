from PIL import Image
from pathlib import Path
import math
import argparse
import sys

class ImageTransformation:
    def __init__(self, name: str):
        self.name = name
    
    def transform(self, img: Image) -> Image:
        raise RuntimeError("Not implemented: " + self.name)

class ResizeTransformation(ImageTransformation):
    def __init__(self, targetwidth: int = -1, targetheight: int = -1):
        super().__init__("resize")
        self.targetwidth = targetwidth
        self.targetheight = targetheight

    def transform(self, img: Image) -> Image:
        fwidth = img.width
        fheight = img.height
        targetwidth = self.targetwidth
        targetheight = self.targetheight
        if targetwidth != -1:
            if targetheight != -1:
                fwidth, fheight = targetwidth, targetheight
            else:
                fwidth = targetwidth
                fheight *= targetwidth / img.width
        elif targetheight != -1:
            fheight = targetheight
            fwidth *= targetheight / img.height
        if fwidth != img.width or fheight != img.height:
            return img.resize((math.ceil(fwidth), math.ceil(fheight)))
        return img

class BlurTransformation(ImageTransformation):
    def __init__(self, radius: int, algorithm: str = "gaussian"):
        super().__init__("blur")
        self.radius = radius
        if algorithm.lower() not in ("gaussian", "box", "default"):
            raise Exception("Not a valid blur algorithm: " + algorithm)
        self.algorithm = algorithm.lower()
    
    def transform(self, img: Image) -> Image:
        radius = self.radius
        algorithm = self.algorithm
        if algorithm == "gaussian":
            return img.filter(Image.ImageFilter.GaussianBlur(radius))
        elif algorithm == "box":
            return img.filter(Image.ImageFilter.BoxBlur(radius))
        elif algorithm == "default":
            return img.filter(Image.ImageFilter.BLUR)
        else:
            raise RuntimeError("Unknown blur algorithm: " + algorithm)

class CropTransformation(ImageTransformation):
    def __init__(self, box: tuple[float, float, float, float]):
        super().__init__("crop")
        self.box = box
    
    def transform(self, img: Image) -> Image:
        return img.crop(self.box)

class ConvertTransformation(ImageTransformation):
    def __init__(self, mode="RGB"):
        super().__init__("convert")
        self.mode = mode
    
    def transform(self, img):
        return img.convert(mode=self.mode)

class CheckSizeTransformation(ImageTransformation):
    def __init__(self, minwidth: int = -1, minheight: int = -1):
        super().__init__("verifysize")
        self.minwidth = minwidth
        self.minheight = minheight
    
    def transform(self, img):
        minwidth = self.minwidth
        minheight = self.minheight
        check = True
        if minwidth != -1:
            if minheight != -1:
                check = img.width >= minwidth and img.height >= minheight
            else:
                check = img.width >= minwidth
        elif minheight != -1:
            check = img.height >= minheight
        if not check:
            minwidthstr = "any" if minwidth == -1 else str(minwidth)
            minheightstr = "any" if minheight == -1 else str(minheight)
            raise Exception(f"Image does not meet valid size requirements! minimum={minwidthstr}x{minheightstr}, actual={img.width}x{img.height}")
        return img

def resize(targetwidth: int = -1, targetheight: int = -1):
    return ResizeTransformation(targetwidth, targetheight)

RESIZE_1080P = ResizeTransformation(targetheight=1080)

def blur(radius: int, algorithm: str = "gaussian"):
    return BlurTransformation(radius, algorithm)

def gaussian_blur(radius: int):
    return blur(radius)

def crop(left: float, upper: float, right: float, lower: float):
    return CropTransformation((left, upper, right, lower))

def convert(mode: str = "RGB"):
    return ConvertTransformation(mode)

def convert_rgb():
    return convert()

def check_size(minwidth: int = -1, minheight: int = -1):
    return CheckSizeTransformation(minwidth, minheight)

CHECK_1080P = CheckSizeTransformation(1920, 1080)

class ImageProcess:
    def __init__(self, inpath, outpath, transforms: list[ImageTransformation] = [], **saveparams: any):
        self.inpath = inpath
        self.outpath = outpath
        self.transforms = transforms
        self.saveparams = saveparams
    
    def transform(self, force: bool = False):
        inpath = Path(self.inpath)
        outpath = Path(self.outpath)
        if outpath.exists() and not force:
            print(f"Skipping already existing image at {outpath}")
            return
        outpath.parent.mkdir(exist_ok=True)
        transforms = self.transforms
        print(f"Transforming image <{inpath}>")
        with Image.open(inpath) as img:
            for transform in transforms:
                print(f"\tApplying {transform.name} transformation")
                img = transform.transform(img)
            print(f"\tSaving image to <{outpath}>")
            img.save(outpath, **self.saveparams)

JPEGS = (
    # chapter 6
    ("reference/funindark cgs/hug1.png", "event/funindark/funindark_hug1.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug2.png", "event/funindark/funindark_hug2.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug3.png", "event/funindark/funindark_hug3.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug4.png", "event/funindark/funindark_hug4.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug5.png", "event/funindark/funindark_hug5.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug6.png", "event/funindark/funindark_hug6.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug7.png", "event/funindark/funindark_hug7.jpg", [RESIZE_1080P]),
    # ("reference/funindark cgs/hug1.png", "event/funindark/funindark_hug1_large.jpg"),
    # ("reference/funindark cgs/hug2.png", "event/funindark/funindark_hug2_large.jpg"),
    # ("reference/funindark cgs/hug3.png", "event/funindark/funindark_hug3_large.jpg"),
    # ("reference/funindark cgs/hug4.png", "event/funindark/funindark_hug4_large.jpg"),
    # ("reference/funindark cgs/hug5.png", "event/funindark/funindark_hug5_large.jpg"),
    # ("reference/funindark cgs/hug6.png", "event/funindark/funindark_hug6_large.jpg"),
    # ("reference/funindark cgs/hug7.png", "event/funindark/funindark_hug7_large.jpg"),
    # chapter 11
    ("reference/dance cgs/HanakoLillyDanceFinal2.png", "event/ballroomdance/ballroomdance_emb_large.jpg"),
    ("reference/dance cgs/HanakoLillyDanceFinal2.png", "event/ballroomdance/ballroomdance_emb_normal.jpg", [RESIZE_1080P]),
    ("reference/dance cgs/HanakoLillyDanceFinal1.png", "event/ballroomdance/ballroomdance_smile_large.jpg"),
    ("reference/dance cgs/HanakoLillyDanceFinal1.png", "event/ballroomdance/ballroomdance_smile_normal.jpg", [RESIZE_1080P]),
    # chapter 13
    ("reference/road cgs/Whizvox_CG2_HisaoxHanako_F1.jpg", "event/rainyroad/rainyroad_a.jpg", [crop(0, 268, 7880, 4700), RESIZE_1080P]),
    ("reference/road cgs/Whizvox_CG2_HisaoxHanako_F2.jpg", "event/rainyroad/rainyroad_b.jpg", [crop(0, 268, 7880, 4700), RESIZE_1080P]),
    # chapter 17
    ("reference/Whizvox_KS_CG1_Hanako_Lily_CG_WIP_13.jpg", "event/caress/caress_large.jpg", [crop(0, 0, 8031, 4518)]),
    ("reference/Whizvox_KS_CG1_Hanako_Lily_CG_WIP_13.jpg", "event/caress/caress_normal.jpg", [crop(0, 0, 8031, 4518), RESIZE_1080P])
)

def main(args):
    sh_path = None
    ks_path = None
    if "shdir" in args and args["shdir"] is not None:
        sh_path = Path(args["shdir"])
    else:
        sh_path = Path(__file__).parent.parent
    ks_path = sh_path.parent.parent
    print(f"sh_path: {sh_path}")
    print(f"ks_path: {ks_path}")
    force = False
    if "force" in args:
        force = args["force"]
    images_to_process: list[ImageProcess] = []
    for entry in JPEGS:
        transforms = []
        if len(entry) == 3:
            transforms = entry[2]
        inpath = None
        # paths that start with a tilde (~) should be in reference to the katawa shoujo game directory
        if entry[0][0] == "~":
            inpath = Path(ks_path, entry[0][1:])
        # otherwise, by default, paths will be in reference to the sisterhood directory
        else:
            inpath = Path(sh_path, entry[0])
        outpath = Path(sh_path, entry[1])
        transforms.append(CHECK_1080P)
        transforms.append(convert_rgb())
        images_to_process.append(ImageProcess(inpath, outpath, transforms, quality=90))
    for process in images_to_process:
        process.transform(force)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="shimgx",
        description="Sisterhood image export tool"
    )
    parser.add_argument("-d", "--shdir", required=False)
    parser.add_argument("-f", "--force", action="store_true", default=False)
    main(vars(parser.parse_args(sys.argv[1:])))