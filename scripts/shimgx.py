from PIL import ImageFilter, Image
from pathlib import Path
import math
import argparse
import sys

sh_path: Path = Path(".")
ks_path: Path = Path(".")

def resolve_path(plainpath: str) -> Path:
    # paths that start with a tilde (~) should be in reference to the katawa shoujo game directory
    if len(plainpath) > 0 and plainpath[0] == "~":
        return Path(ks_path, plainpath[1:])
    # otherwise, by default, paths will be in reference to the sisterhood directory
    else:
        return Path(sh_path, plainpath)

class ImageTransformation:
    def __init__(self, name: str):
        self.name = name

    def transform(self, img: Image.Image) -> Image.Image:
        raise RuntimeError("Not implemented: " + self.name)

class ResizeTransformation(ImageTransformation):
    def __init__(self, targetwidth: int = -1, targetheight: int = -1):
        super().__init__("resize")
        self.targetwidth = targetwidth
        self.targetheight = targetheight

    def transform(self, img: Image.Image) -> Image.Image:
        fwidth: int = img.width
        fheight: int = img.height
        targetwidth = self.targetwidth
        targetheight = self.targetheight
        if targetwidth != -1:
            if targetheight != -1:
                fwidth, fheight = targetwidth, targetheight
            else:
                fwidth = targetwidth
                fheight = math.ceil(fheight * (targetwidth / img.width))
        elif targetheight != -1:
            fheight = targetheight
            fwidth = math.ceil(fwidth * (targetheight / img.height))
        if fwidth != img.width or fheight != img.height:
            # idk why pylance has a problem with this line
            return img.resize(size=(fwidth, fheight)) # type: ignore
        return img


class BlurTransformation(ImageTransformation):
    def __init__(self, radius: int, algorithm: str = "gaussian"):
        super().__init__("blur")
        self.radius = radius
        if algorithm.lower() not in ("gaussian", "box", "default"):
            raise Exception("Not a valid blur algorithm: " + algorithm)
        self.algorithm = algorithm.lower()
    
    def transform(self, img: Image.Image) -> Image.Image:
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
    
    def transform(self, img: Image.Image) -> Image.Image:
        return img.crop(self.box)


class ConvertTransformation(ImageTransformation):
    def __init__(self, mode: str="RGB"):
        super().__init__("convert")
        self.mode = mode

    def transform(self, img: Image.Image):
        return img.convert(mode=self.mode)


class CheckSizeTransformation(ImageTransformation):
    def __init__(self, minwidth: int = -1, minheight: int = -1):
        super().__init__("verifysize")
        self.minwidth = minwidth
        self.minheight = minheight
    
    def transform(self, img: Image.Image):
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
    
    def transform(self, img: Image.Image):
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
    def __init__(self, inpath: str | Path, outpath: str | Path, transforms: list[ImageTransformation] = [], **saveparams: any): # type: ignore
        self.inpath = inpath
        self.outpath = outpath
        self.transforms = transforms
        self.saveparams = saveparams # type: ignore
    
    def transform(self, replace: bool = False):
        inpath = Path(self.inpath)
        outpath = Path(self.outpath)
        if outpath.exists() and not replace:
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
            img.save(outpath, **self.saveparams) # type: ignore

JPEGS: list[tuple[str, str, list[ImageTransformation]]] = [
    # chapter 5
    ("reference/wheatfield ev/HanakoxHisao2_2.png", "event/wheatfield/wheatfield_smile.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_awkward.png", "event/wheatfield/wheatfield_awkward.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_dreamy.png", "event/wheatfield/wheatfield_dreamy.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_talk.png", "event/wheatfield/wheatfield_talk.jpg", [RESIZE_1080P]),
    # chapter 6
    ("reference/funindark cgs/hug1_clip.png", "event/funindark/funindark_hug_rest_large.jpg", []),
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
    ("reference/funindark cgs/fap3.png", "event/funindark/funindark_naked_breast_large.jpg", []),
    ("reference/funindark cgs/fap3.png", "event/funindark/funindark_naked_breast.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap4.png", "event/funindark/funindark_naked_grab.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap4.png", "event/funindark/funindark_naked_grab_close.jpg", [crop(0, 0, 1920, 1080)]),
    ("reference/funindark cgs/fap5.png", "event/funindark/funindark_naked_masturbate.jpg", [RESIZE_1080P]),
    ("reference/funindark cgs/fap6.png", "event/funindark/funindark_naked_climax_close.jpg", [crop(0, 0, 1920, 1080)]),
    ("reference/funindark cgs/fap6.png", "event/funindark/funindark_naked_climax.jpg", [RESIZE_1080P]),
    # chapter 9
    ("reference/hotel cgs 2/Hisao_straddles_Hanako_1.png", "event/hotel/hotel_onhanako_large.jpg", []),
    ("reference/hotel cgs 2/Hisao_straddles_Hanako_1.png", "event/hotel/hotel_onhanako.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_on_top_of_Hisao_1.png", "event/hotel/hotel_onhisao_large.jpg", []),
    ("reference/hotel cgs 2/Hanako_on_top_of_Hisao_1.png", "event/hotel/hotel_onhisao.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_mirror_1.png", "event/hotel/hotel_mirror.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_on_top_of_Hisao_oiled_1.png", "event/hotel/hotel_layontop.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_on_top_thighjob-1-1.png", "event/hotel/hotel_thigh_large.jpg", []),
    ("reference/hotel cgs 2/Hanako_on_top_thighjob-1-1.png", "event/hotel/hotel_thigh.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Hanako_on_top_thighjob-2-1.png", "event/hotel/hotel_thigh_climax.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Masturnation_1-1.png", "event/hotel/hotel_masturbate.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/Masturnation_2-1.png", "event/hotel/hotel_masturbate_climax.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/missionary_sex_1-1.png", "event/hotel/hotel_bed.jpg", [RESIZE_1080P]),
    ("reference/hotel cgs 2/missionary_sex_2-1.png", "event/hotel/hotel_bed_climax.jpg", [RESIZE_1080P]),
    # chapter 11
    ("reference/dance cgs/HanakoLillyDanceFinal2.png", "event/ballroomdance/ballroomdance_emb_large.jpg", []),
    ("reference/dance cgs/HanakoLillyDanceFinal2.png", "event/ballroomdance/ballroomdance_emb_normal.jpg", [RESIZE_1080P]),
    ("reference/dance cgs/HanakoLillyDanceFinal1.png", "event/ballroomdance/ballroomdance_smile_large.jpg", []),
    ("reference/dance cgs/HanakoLillyDanceFinal1.png", "event/ballroomdance/ballroomdance_smile_normal.jpg", [RESIZE_1080P]),
    # chapter 13
    ("reference/road cgs/Whizvox_CG2_HisaoxHanako_F1.jpg", "event/rainyroad/rainyroad_a.jpg", [crop(0, 268, 7880, 4700), RESIZE_1080P]),
    ("reference/road cgs/Whizvox_CG2_HisaoxHanako_F2.jpg", "event/rainyroad/rainyroad_b.jpg", [crop(0, 268, 7880, 4700), RESIZE_1080P]),
    # chapter 16
    ("reference/rooftop ev/RooftopKissCGFinal.png", "event/rooftopkiss/rooftopkiss_normal.jpg", [RESIZE_1080P]),
    # chapter 17
    ("~bgs/school_dormhisao.jpg", "vfx/hanako_dormhisao_blur.jpg", [CompositeTransformation([(606, 0, "~sprites/hanako/close/hanako_emb_emb_close.png")]), blur(5)]),
    ("reference/Whizvox_KS_CG1_Hanako_Lily_CG_WIP_13.jpg", "event/caress/caress_large.jpg", [crop(0, 0, 8031, 4518)]),
    ("reference/Whizvox_KS_CG1_Hanako_Lily_CG_WIP_13.jpg", "event/caress/caress_normal.jpg", [crop(0, 0, 8031, 4518), RESIZE_1080P]),
    # chapter 21
    ("reference/plane ride cgs/Sisterhood_Hanako_x_Lilly_plane_00.png", "event/planeride/planeride_bliss.jpg", [crop(0, 400, 3840, 2560), RESIZE_1080P]),
    ("reference/plane ride cgs/Sisterhood_Hanako_x_Lilly_plane_00.png", "event/planeride/planeride_bliss_large.jpg", []),
    ("reference/plane ride cgs/Sisterhood_Hanako_x_Lilly_plane_01.png", "event/planeride/planeride_pout.jpg", [crop(0, 400, 3840, 2560), RESIZE_1080P]),
    ("reference/plane ride cgs/Sisterhood_Hanako_x_Lilly_plane_02.png", "event/planeride/planeride_blanket.jpg", [crop(0, 400, 3840, 2560), RESIZE_1080P]),
    ("reference/plane ride cgs/Sisterhood_Hanako_x_Lilly_plane_03.png", "event/planeride/planeride_listen.jpg", [crop(0, 400, 3840, 2560), RESIZE_1080P]),
    ("reference/plane ride cgs/Sisterhood_Hanako_x_Lilly_plane_04.png", "event/planeride/planeride_frown.jpg", [crop(0, 400, 3840, 2560), RESIZE_1080P]),
    ("reference/plane ride cgs/Sisterhood_Hanako_x_Lilly_plane_05.png", "event/planeride/planeride_weaksmile.jpg", [crop(0, 400, 3840, 2560), RESIZE_1080P])
]

PHOTOGRAPHS: list[tuple[str, str, list[ImageTransformation]]] = [
    # chapter 28
    ("event/planeride/planeride_bliss.jpg", "gui/journal/p01.jpg", [crop(300, 0, 1920, 1080), resize(525, 350)]),
    ("bgs/inverness_street.jpg", "gui/journal/p02.jpg", [CompositeTransformation([(700, 0, "~sprites/hanako/hanako_emb_smile.png"), (300, 0, "sprites/hisao/hisao_cross_smile_polo.png")]), crop(150, 0, 1770, 1080), resize(525, 350)]),
    ("bgs/inverness_tree.jpg", "gui/journal/p03.jpg", [CompositeTransformation([(384, 0, "~sprites/lilly/lilly_basic_cheerful_cas.png"), (1074, 30, "~sprites/hanako/hanako_basic_bashful_cas.png"), (692, 30, "sprites/hisao/hisao_basic_smile_polo.png")]), crop(162, 0, 1782, 1080), resize(525, 350)]),
    ("reference/bgs/cawthorn.jpg", "gui/journal/p07.jpg", [CompositeTransformation([(338, 50, "sprites/hisao/hisao_basic_grin_swt.png")]), resize(525, 350)]),
    ("reference/journal/photos/p10.jpg", "gui/journal/p10.jpg", [CompositeTransformation([(793, 200, "~sprites/lilly/lilly_cane_giggle_cas.png"), (1199, 200, "sprites/akira/akira_basic_cheerful.png")]), crop(165, 220, 1756, 1280), resize(525, 350)]),
    ("reference/journal/photos/p11.jpg", "gui/journal/p11.jpg", [crop(0, 46, 1000, 712), resize(525, 350)]),
    ("reference/bgs/urquhart castle.jpg", "gui/journal/p12.jpg", [resize(525, 350)]),
    ("reference/bgs/dolphin and seal centre.jpg", "gui/journal/p13.jpg", [crop(0, 8, 1024, 691), resize(525, 350)]),
    ("reference/journal/doodles/IMG_2054.png", "gui/journal/d01.png", [crop(185, 401, 2074, 1214), resize(targetheight=100)]),
    ("reference/journal/doodles/IMG_2055.png", "gui/journal/d02.png", [crop(885, 45, 1357, 1407), resize(targetheight=200)]),
    ("reference/journal/doodles/IMG_2056.png", "gui/journal/d03.png", [crop(709, 63, 1358, 1323), resize(targetheight=160)]),
    ("reference/journal/doodles/IMG_2057.png", "gui/journal/d04.png", [crop(223, 118, 1982, 1325), resize(targetheight=170)]),
    ("reference/journal/doodles/IMG_2058.png", "gui/journal/d05.png", [crop(339, 112, 1797, 1323), resize(targetheight=200)]),
    ("reference/journal/doodles/IMG_2059.png", "gui/journal/d06.png", [crop(289, 33, 1917, 1502), resize(targetheight=185)]),
    ("reference/journal/doodles/IMG_2060.png", "gui/journal/d07.png", [crop(117, 228, 2044, 1400), resize(targetheight=220)]),
    ("reference/journal/doodles/IMG_2061.png", "gui/journal/d08.png", [crop(324, 0, 2160, 1485), resize(targetheight=210)]),
    ("reference/journal/doodles/IMG_2062.png", "gui/journal/d09.png", [crop(500, 202, 1697, 1426), resize(targetheight=250)]),
    ("reference/journal/doodles/IMG_2063.png", "gui/journal/d10.png", [crop(435, 111, 1770, 1620), resize(targetheight=230)]),
    ("reference/journal/doodles/IMG_2063_nt.png", "gui/journal/d10nt.png", [crop(435, 111, 1770, 1620), resize(targetheight=230)]),
    ("reference/journal/doodles/IMG_2064.png", "gui/journal/d11.png", [crop(781, 118, 1368, 1438), resize(targetheight=250)]),
    ("reference/journal/doodles/IMG_2065.png", "gui/journal/d12.png", [crop(265, 99, 1908, 1525), resize(targetheight=240)]),
    ("reference/journal/doodles/IMG_2066.png", "gui/journal/d13.png", [crop(197, 113, 1986, 1621), resize(targetheight=240)]),
    ("reference/journal/doodles/IMG_2066_nt.png", "gui/journal/d13nt.png", [crop(617, 317, 1511, 1621), resize(targetheight=220)]),
    ("reference/journal/doodles/IMG_2067.png", "gui/journal/d14.png", [crop(100, 165, 2160, 1297), resize(targetheight=200)]),
    ("reference/journal/doodles/IMG_2068.png", "gui/journal/d15.png", [crop(797, 86, 1365, 1510), resize(targetheight=200)]),
    ("reference/journal/doodles/IMG_2069.png", "gui/journal/d28.png", [crop(0, 103, 2027, 1620), resize(targetheight=250)]),
    ("reference/journal/doodles/IMG_2070.png", "gui/journal/d19.png", [crop(586, 369, 1458, 1460), resize(targetheight=180)])
]


class Arguments:
    shdir: str
    ksdir: str
    replace: bool


def _update_paths(args: Arguments):
    global sh_path
    global ks_path
    sh_path = Path(args.shdir)
    ks_path = Path(args.ksdir)


def main(args: Arguments):
    _update_paths(args)
    images_to_process: list[ImageProcess] = []
    for entry in JPEGS + PHOTOGRAPHS:
        transforms = []
        if len(entry) == 3:
            transforms = entry[2]
        inpath = resolve_path(entry[0])
        outpath = Path(sh_path, entry[1]) # type: ignore
        if entry in JPEGS:
            transforms.append(CHECK_1080P)
            transforms.append(convert_rgb())
        images_to_process.append(ImageProcess(inpath, outpath, transforms, quality=90))
    for process in images_to_process:
        process.transform(args.replace)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sisterhood image export tool"
    )
    parser.add_argument("-s", "--shdir", required=True, help="location of Sisterhood project directory")
    parser.add_argument("-k", "--ksdir", required=True, help="location of Katawa Shoujo: Re-Engineered project directory")
    parser.add_argument("-r", "--replace", action="store_true", default=False, help="whether to replace pre-existing image files")
    main(parser.parse_args(sys.argv[1:], namespace=Arguments()))