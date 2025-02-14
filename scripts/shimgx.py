from PIL import Image, ImageFilter
from pathlib import Path
import math
import argparse
import sys

sh_path = None
ks_path = None

def _update_paths(args):
    global sh_path
    global ks_path
    if "shdir" in args and args["shdir"] is not None:
        sh_path = Path(args["shdir"])
    else:
        sh_path = Path(__file__).parent.parent
    ks_path = sh_path.parent.parent
    print(f"sh_path: {sh_path}")
    print(f"ks_path: {ks_path}")

def resolve_path(plainpath):
    # paths that start with a tilde (~) should be in reference to the katawa shoujo game directory
    if len(plainpath) > 0 and plainpath[0] == "~":
        return Path(ks_path, plainpath[1:])
    # otherwise, by default, paths will be in reference to the sisterhood directory
    else:
        return Path(sh_path, plainpath)

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
            return img.filter(ImageFilter.GaussianBlur(radius))
        elif algorithm == "box":
            return img.filter(ImageFilter.BoxBlur(radius))
        elif algorithm == "default":
            return img.filter(ImageFilter.BLUR)
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
    
    def transform(self, img: Image):
        return img.convert(mode=self.mode)

class CheckSizeTransformation(ImageTransformation):
    def __init__(self, minwidth: int = -1, minheight: int = -1):
        super().__init__("verifysize")
        self.minwidth = minwidth
        self.minheight = minheight
    
    def transform(self, img: Image):
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

class CompositeTransformation(ImageTransformation):
    def __init__(self, layers: list[tuple[int, int, str]]):
        super().__init__("composite")
        self.layers = layers
    
    def transform(self, img: Image):
        for layer in self.layers:
            x = layer[0]
            y = layer[1]
            toppath = layer[2]
            with Image.open(resolve_path(toppath)) as topimg:
                img.paste(topimg, (x, y), topimg.convert("RGBA"))
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
    # chapter 5
    ("reference/wheatfield ev/HanakoxHisao2_2.png", "event/wheatfield/wheatfield_smile.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_awkward.png", "event/wheatfield/wheatfield_awkward.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_dreamy.png", "event/wheatfield/wheatfield_dreamy.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_talk.png", "event/wheatfield/wheatfield_talk.jpg", [RESIZE_1080P]),
    # chapter 6
    ("reference/funindark cgs/hug1_clip.png", "event/funindark/funindark_hug_rest_large.jpg"),
    ("reference/funindark cgs/hug1_clip.png", "event/funindark/funindark_hug_rest.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug2.png", "event/funindark/funindark_hug_neck.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug3.png", "event/funindark/funindark_hug_cheek.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug4.png", "event/funindark/funindark_hug_kiss.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug5_clip.png", "event/funindark/funindark_hug_look.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/hug6_clip.png", "event/funindark/funindark_hug_awkward.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap1.png", "event/funindark/funindark_naked_touch.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap1.png", "event/funindark/funindark_naked_touch_close.jpg", [crop(0, 0, 1920, 1080)]),
    ("reference/funindark cgs/fap2.png", "event/funindark/funindark_naked_hand.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap2.png", "event/funindark/funindark_naked_hand_close.jpg", [crop(0, 0, 1920, 1080)]),
    ("reference/funindark cgs/fap3.png", "event/funindark/funindark_naked_breast_large.jpg"),
    ("reference/funindark cgs/fap3.png", "event/funindark/funindark_naked_breast.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap4.png", "event/funindark/funindark_naked_grab.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap4.png", "event/funindark/funindark_naked_grab_close.jpg", [crop(0, 0, 1920, 1080)]),
    ("reference/funindark cgs/fap5.png", "event/funindark/funindark_naked_masturbate.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap6.png", "event/funindark/funindark_naked_climax_close.jpg", [crop(0, 0, 1920, 1080)]),
    ("reference/funindark cgs/fap6.png", "event/funindark/funindark_naked_climax.jpg", [RESIZE_1080P]),
    # chapter 9
    ("reference/hotel cgs 2/Hisao_straddles_Hanako_1.png", "event/hotel/hotel_onhanako_large.jpg"),
    ("reference/hotel cgs 2/Hisao_straddles_Hanako_1.png", "event/hotel/hotel_onhanako.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_on_top_of_Hisao_1.png", "event/hotel/hotel_onhisao_large.jpg"),
    ("reference/hotel cgs 2/Hanako_on_top_of_Hisao_1.png", "event/hotel/hotel_onhisao.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_mirror_1.png", "event/hotel/hotel_mirror.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_on_top_of_Hisao_oiled_1.png", "event/hotel/hotel_layontop.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_on_top_thighjob-1-1.png", "event/hotel/hotel_thigh_large.jpg"),
    ("reference/hotel cgs 2/Hanako_on_top_thighjob-1-1.png", "event/hotel/hotel_thigh.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_on_top_thighjob-2-1.png", "event/hotel/hotel_thigh_climax.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Masturnation_1-1.png", "event/hotel/hotel_masturbate.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Masturnation_2-1.png", "event/hotel/hotel_masturbate_climax.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/missionary_sex_1-1.png", "event/hotel/hotel_bed.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/missionary_sex_2-1.png", "event/hotel/hotel_bed_climax.jpg", [RESIZE_1080P]),
    # chapter 11
    ("reference/dance cgs/HanakoLillyDanceFinal2.png", "event/ballroomdance/ballroomdance_emb_large.jpg"),
    ("reference/dance cgs/HanakoLillyDanceFinal2.png", "event/ballroomdance/ballroomdance_emb_normal.jpg", [RESIZE_1080P]),
    ("reference/dance cgs/HanakoLillyDanceFinal1.png", "event/ballroomdance/ballroomdance_smile_large.jpg"),
    ("reference/dance cgs/HanakoLillyDanceFinal1.png", "event/ballroomdance/ballroomdance_smile_normal.jpg", [RESIZE_1080P]),
    # chapter 13
    ("reference/road cgs/Whizvox_CG2_HisaoxHanako_F1.jpg", "event/rainyroad/rainyroad_a.jpg", [crop(0, 268, 7880, 4700), RESIZE_1080P]),
    ("reference/road cgs/Whizvox_CG2_HisaoxHanako_F2.jpg", "event/rainyroad/rainyroad_b.jpg", [crop(0, 268, 7880, 4700), RESIZE_1080P]),
    # chapter 16
    ("reference/rooftop ev/RooftopKissCGFinal.png", "event/rooftopkiss/rooftopkiss_normal.jpg", [RESIZE_1080P]),
    # chapter 17
    ("~bgs/school_dormhisao.jpg", "vfx/hanako_dormhisao_blur.jpg", [CompositeTransformation([(606, 0, "~sprites/hanako/close/hanako_emb_emb_close.png")]), blur(5)]),
    ("reference/Whizvox_KS_CG1_Hanako_Lily_CG_WIP_13.jpg", "event/caress/caress_large.jpg", [crop(0, 0, 8031, 4518)]),
    ("reference/Whizvox_KS_CG1_Hanako_Lily_CG_WIP_13.jpg", "event/caress/caress_normal.jpg", [crop(0, 0, 8031, 4518), RESIZE_1080P])
)

def main(args):
    _update_paths(args)
    force = False
    if "force" in args:
        force = args["force"]
    images_to_process: list[ImageProcess] = []
    for entry in JPEGS:
        transforms = []
        if len(entry) == 3:
            transforms = entry[2]
        inpath = resolve_path(entry[0])
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