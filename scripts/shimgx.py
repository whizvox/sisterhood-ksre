from PIL import ImageFilter, Image
from pathlib import Path
import math
import argparse
import sys
import random
import string
import subprocess
from sishoodutil import add_arguments, update_paths, relative_to_sh_path, resolve_path

waifu2x_path: Path = Path(".")

def random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# def resolve_path(plainpath: str) -> Path:
#     # paths that start with a tilde (~) should be in reference to the katawa shoujo game directory
#     if len(plainpath) > 0 and plainpath[0] == "~":
#         return Path(ks_path, "game", plainpath[1:])
#     # otherwise, by default, paths will be in reference to the sisterhood directory
#     else:
#         #return Path(sh_path, plainpath)
#         return resolve_path(plainpath)

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

class UpscaleTransformation(ImageTransformation):
    def __init__(self, scale: int = 2, noise: int = 2):
        super().__init__("upscale")
        self.scale = scale
        self.noise = noise

    def transform(self, img: Image.Image):
        # need to save, upscale, and load the resulting image
        input = Path("tmp/pre_upscale.png")
        input.parent.mkdir(exist_ok=True)
        img.save(input)
        output = Path("tmp/post_upscale.png")
        input_str = str(input.resolve())
        output_str = str(output.resolve())
        s = subprocess.check_output([str(waifu2x_path), "-i", input_str, "-o", output_str, "-s", str(self.scale), "-n", str(self.noise)])
        print(s.decode("utf-8"))
        with Image.open(output) as outimg:
            return outimg.copy()

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

def upscale(scale: int = 2, noise: int = 2):
    return UpscaleTransformation(scale, noise)

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
            return
        if not inpath.exists():
            print(f"[WARNING] Skipping non-existant input image: {inpath}")
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

IMAGES: list[tuple[str, str, list[ImageTransformation]]] = [
    # chapter 5
    ("reference/wheatfield ev/HanakoxHisao2_2.png", "event/wheatfield/wheatfield_smile.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_awkward.png", "event/wheatfield/wheatfield_awkward.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_dreamy.png", "event/wheatfield/wheatfield_dreamy.jpg", [RESIZE_1080P]),
    ("reference/wheatfield ev/wheatfield_talk.png", "event/wheatfield/wheatfield_talk.jpg", [RESIZE_1080P]),
    # chapter 0
    ("bgs/school_therapist.jpg", "bgs/school_therapist_blur1.jpg", [blur(5)]),
    ("bgs/school_therapist.jpg", "bgs/school_therapist_blur2.jpg", [blur(10)]),
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
    # chapter 10, 20, 29, and 39
    ("@Event Art/Pillow Talk/CG_SET_B1-02.png", "event/pillowtalk/pillowtalk_comfort.jpg", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/CG_SET_B1-01.png", "event/pillowtalk/pillowtalk_kiss.jpg", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/hisao grin.png", "event/pillowtalk/pillowtalk_hisao_grin.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/hisao concern.png", "event/pillowtalk/pillowtalk_hisao_concern.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/hanako grin.png", "event/pillowtalk/pillowtalk_hanako_grin.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/hanako up.png", "event/pillowtalk/pillowtalk_hanako_up.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/CG_SET_B2-01.png", "event/pillowtalk/pillowtalk_blanket.jpg", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/CG_SET_B2-02.png", "event/pillowtalk/pillowtalk_caress.jpg", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/base.png", "event/pillowtalk/pillowtalk_comfort_dark.jpg", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hisao concern.png", "event/pillowtalk/pillowtalk_hisao_concern_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hisao talk.png", "event/pillowtalk/pillowtalk_hisao_talk_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hisao grin.png", "event/pillowtalk/pillowtalk_hisao_grin_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hisao concern.png", "event/pillowtalk/pillowtalk_hisao_concern_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hisao smile.png", "event/pillowtalk/pillowtalk_hisao_smile_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/hisao upsmile.png", "event/pillowtalk/pillowtalk_hisao_upsmile.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hisao upsmile.png", "event/pillowtalk/pillowtalk_hisao_upsmile_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hanako down.png", "event/pillowtalk/pillowtalk_hanako_down_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hanako up.png", "event/pillowtalk/pillowtalk_hanako_up_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hanako grin.png", "event/pillowtalk/pillowtalk_hanako_grin_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/blanket.png",    "event/pillowtalk/pillowtalk_blanket_dark.jpg", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hanako up blush.png",  "event/pillowtalk/pillowtalk_hanako_upblush_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hanako grin blush.png",  "event/pillowtalk/pillowtalk_hanako_grinblush_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hanako smileupblush.png",  "event/pillowtalk/pillowtalk_hanako_smileupblush_dark.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/hanako smileblush.png",  "event/pillowtalk/pillowtalk_hanako_smileblush.png", [RESIZE_1080P]),
    ("@Event Art/Pillow Talk/dark/hanako smileblush.png",  "event/pillowtalk/pillowtalk_hanako_smileblush_dark.png", [RESIZE_1080P]),
    # chapter 11
    ("reference/dance cgs/HanakoLillyDanceFinal2.png", "event/ballroomdance/ballroomdance_emb_large.jpg", []),
    ("reference/dance cgs/HanakoLillyDanceFinal2.png", "event/ballroomdance/ballroomdance_emb_normal.jpg", [RESIZE_1080P]),
    ("reference/dance cgs/HanakoLillyDanceFinal1.png", "event/ballroomdance/ballroomdance_smile_large.jpg", []),
    ("reference/dance cgs/HanakoLillyDanceFinal1.png", "event/ballroomdance/ballroomdance_smile_normal.jpg", [RESIZE_1080P]),
    # chapter 13
    ("reference/road cgs/Whizvox_CG2_HisaoxHanako_F1.jpg", "event/rainyroad/rainyroad_a.jpg", [crop(0, 268, 7880, 4700), RESIZE_1080P]),
    ("reference/road cgs/Whizvox_CG2_HisaoxHanako_F2.jpg", "event/rainyroad/rainyroad_b.jpg", [crop(0, 268, 7880, 4700), RESIZE_1080P]),
    # chapter 14
    ("~bgs/hosp_ceiling.jpg", "bgs/hosp_ceiling_blur.jpg", [blur(10)]),
    ("~bgs/hosp_room2.jpg", "bgs/hosp_room2_blur.jpg", [blur(10)]),
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
    ("reference/plane ride cgs/Sisterhood_Hanako_x_Lilly_plane_05.png", "event/planeride/planeride_weaksmile.jpg", [crop(0, 400, 3840, 2560), RESIZE_1080P]),
    # chapter 24 - Cello and Wine
    ("@Event Art/Ch 24 Cello and Wine/1.1.png", "event/celloandwine/celloandwine_cello_play.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/1.2.png", "event/celloandwine/celloandwine_cello_lookup.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/2.1.png", "event/celloandwine/celloandwine_block_pout.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/2.2.png", "event/celloandwine/celloandwine_block_grin.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/3.1.png", "event/celloandwine/celloandwine_sit_tease.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/3.2.png", "event/celloandwine/celloandwine_sit_rest.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/3.3.png", "event/celloandwine/celloandwine_sit_cover.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/3.4.png", "event/celloandwine/celloandwine_sit_feel.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/3.5.png", "event/celloandwine/celloandwine_sit_clap.jpg"),
    ("@Event Art/Ch 24 Cello and Wine/3.6.png", "event/celloandwine/celloandwine_sit_kiss.jpg"),
    # chapter 34
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_01.png",     "event/hanakohistory/hanakohistory_bed.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_02.png",     "event/hanakohistory/hanakohistory_bed_pain.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_03_A.png",   "event/hanakohistory/hanakohistory_fire.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_03_B.png",   "event/hanakohistory/hanakohistory_fire_alone.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_04.png",     "event/hanakohistory/hanakohistory_urn.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_05.png",     "event/hanakohistory/hanakohistory_read.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_06.png",     "event/hanakohistory/hanakohistory_read_leave.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_06_B.png",   "event/hanakohistory/hanakohistory_read_alone.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_07.png",     "event/hanakohistory/hanakohistory_play.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_08.png",     "event/hanakohistory/hanakohistory_play_tease.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_09.png",     "event/hanakohistory/hanakohistory_bully.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_10.png",     "event/hanakohistory/hanakohistory_bully_cry.jpg"),
    ("reference/Event Art/Ch34 Hanako History/Hanako_backstory_11.png",     "event/hanakohistory/hanakohistory_gate.jpg"),
    # chapter 25
    ("bgs/satou_guestroom.jpg", "bgs/satou_guestroom_blur.jpg", [blur(8)]),
    # chapter 29 - Soap Opera
    ("@Event Art/Soap Opera Corrections/edit/hisao1_back.png",                  "event/soapopera/soapopera_hisao1_back.jpg",        [RESIZE_1080P]),
    ("@Event Art/Soap Opera Corrections/edit/hisao1_back.png",                  "event/soapopera/soapopera_hisao1_back_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hisao1_lay.png",                   "event/soapopera/soapopera_hisao1_lay.jpg",         [RESIZE_1080P]),
    ("@Event Art/Soap Opera Corrections/edit/hisao1_lay.png",                   "event/soapopera/soapopera_hisao1_lay_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hanako1_back.png",                 "event/soapopera/soapopera_hanako1_back.jpg",       [RESIZE_1080P]),
    ("@Event Art/Soap Opera Corrections/edit/hanako1_back.png",                 "event/soapopera/soapopera_hanako1_back_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hanako1_hair.png",                 "event/soapopera/soapopera_hanako1_hair_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hanako1_talk_hanako_overlay.png",  "event/soapopera/soapopera_hanako1_hairtalk_hanako.png"),
    ("@Event Art/Soap Opera Corrections/edit/hanako1_talk_hisao_overlay.png",  "event/soapopera/soapopera_hanako1_hairtalk_hisao.png"),
    ("@Event Art/Soap Opera Corrections/edit/hisao2_hug.png",                   "event/soapopera/soapopera_hisao2_hug.jpg",         [RESIZE_1080P]),
    ("@Event Art/Soap Opera Corrections/edit/hisao2_hug.png",                   "event/soapopera/soapopera_hisao2_hug_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hisao2_erection.png",              "event/soapopera/soapopera_hisao2_erection.jpg",    [RESIZE_1080P]),
    ("@Event Art/Soap Opera Corrections/edit/hisao2_erection.png",              "event/soapopera/soapopera_hisao2_erection_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hisao2_handy.png",                 "event/soapopera/soapopera_hisao2_handy_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hisao2_climax_hisao_overlay.png",  "event/soapopera/soapopera_hisao2_climax_hisao.png"),
    ("@Event Art/Soap Opera Corrections/edit/hisao2_climax.png",                "event/soapopera/soapopera_hisao2_climax_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hanako2_caress.png",               "event/soapopera/soapopera_hanako2_caress_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hanako2_spray.png",                "event/soapopera/soapopera_hanako2_spray_large.jpg"),
    ("@Event Art/Soap Opera Corrections/edit/hanako2_climax.png",               "event/soapopera/soapopera_hanako2_climax.jpg",     [RESIZE_1080P]),
    # chapter 29 - Evening Snack
    ("@Event Art/Ch29 Evening Snack/1-0_FINAL_art.png", "event/eveningsnack/eveningsnack_cuddle.jpg"),
    ("@Event Art/Ch29 Evening Snack/1_FINAL_art.png",   "event/eveningsnack/eveningsnack_cuddle_naked.jpg"),
    ("@Event Art/Ch29 Evening Snack/2_FINAL.png",       "event/eveningsnack/eveningsnack_hipamper.jpg"),
    ("@Event Art/Ch29 Evening Snack/3_FINAL.png",       "event/eveningsnack/eveningsnack_hiplay.jpg"),
    ("@Event Art/Ch29 Evening Snack/4_FINAL.png",       "event/eveningsnack/eveningsnack_bj1_look.jpg"),
    ("@Event Art/Ch29 Evening Snack/5_FINAL.png",       "event/eveningsnack/eveningsnack_bj1_lick.jpg"),
    ("@Event Art/Ch29 Evening Snack/6_FINAL.png",       "event/eveningsnack/eveningsnack_bj1_pleasure.jpg"),
    ("@Event Art/Ch29 Evening Snack/7_FINAL.png",       "event/eveningsnack/eveningsnack_bj1_awkward.jpg"),
    ("@Event Art/Ch29 Evening Snack/8_FINAL.png",       "event/eveningsnack/eveningsnack_bj2_pleasure.jpg"),
    ("@Event Art/Ch29 Evening Snack/9_FINAL.png",       "event/eveningsnack/eveningsnack_bj2_climax.jpg"),
    ("@Event Art/Ch29 Evening Snack/10_FINAL.png",      "event/eveningsnack/eveningsnack_hapamper.jpg"),
    ("@Event Art/Ch29 Evening Snack/11_FINAL.png",      "event/eveningsnack/eveningsnack_haplay.jpg"),
    ("@Event Art/Ch29 Evening Snack/12-2_FINAL.png",    "event/eveningsnack/eveningsnack_cun1_look.jpg"),
    ("@Event Art/Ch29 Evening Snack/13-3_FINAL.png",    "event/eveningsnack/eveningsnack_cun1_tounge.jpg"),
    ("@Event Art/Ch29 Evening Snack/14-2_FINAL.png",    "event/eveningsnack/eveningsnack_cun1_push.jpg"),
    ("@Event Art/Ch29 Evening Snack/15-2.png",          "event/eveningsnack/eveningsnack_cun2_pleasure.jpg"),
    ("@Event Art/Ch29 Evening Snack/16-3.png",          "event/eveningsnack/eveningsnack_cun2_eatout.jpg"),
    ("@Event Art/Ch29 Evening Snack/17.png",            "event/eveningsnack/eveningsnack_cun2_climax.jpg"),
    # chapter 30+31
    ("@Event Art/Bedridden/Whizvox_4th_CG_HOSPITAL_SET_A_FINAL_1.0.jpg", "event/bedridden/bedridden_lillyakira.jpg", [RESIZE_1080P]),
    ("@Event Art/Bedridden/Whizvox_4th_CG_HOSPITAL_SET_B_FINAL_1.1.jpg", "event/bedridden/bedridden_akira.jpg", [RESIZE_1080P]),
    ("@Event Art/Bedridden/Whizvox_4th_CG_HOSPITAL_SET_C_FINAL_1.1.jpg", "event/bedridden/bedridden_akhiha.jpg"),
    ("@Event Art/Bedridden/overlay/lilly_smile.png",            "event/bedridden/bedridden_lilly_smile_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/lilly_listen.png",           "event/bedridden/bedridden_lilly_listen_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/lilly_angry.png",            "event/bedridden/bedridden_lilly_angry_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/akira_distant.png",          "event/bedridden/bedridden_akira_distant_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/akira_glare.png",            "event/bedridden/bedridden_akira_glare_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/akira_shout.png",            "event/bedridden/bedridden_akira_shout_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/akira_stun.png",             "event/bedridden/bedridden_akira_stun_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/akira_distant.png",          "event/bedridden/bedridden_akira_distant_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/akira_frown.png",            "event/bedridden/bedridden_akira_frown_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/hanako_concern.png",         "event/bedridden/bedridden_hanako_concern_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hanako_downconcern.png",     "event/bedridden/bedridden_hanako_downconcern_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hanako_sad.png",             "event/bedridden/bedridden_hanako_sad_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hanako_downsad.png",         "event/bedridden/bedridden_hanako_downsad_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hanako_unsure.png",          "event/bedridden/bedridden_hanako_unsure_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hanako_downsmile.png",       "event/bedridden/bedridden_hanako_downsmile_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hiroyuki_angry.png",         "event/bedridden/bedridden_hiroyuki_angry_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/hiroyuki_angry.png",         "event/bedridden/bedridden_hiroyuki_angry_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hiroyuki_concern.png",       "event/bedridden/bedridden_hiroyuki_concern_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hiroyuki_content.png",       "event/bedridden/bedridden_hiroyuki_content_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hiroyuki_discomfort.png",    "event/bedridden/bedridden_hiroyuki_discomfort_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/hiroyuki_discomfort.png",    "event/bedridden/bedridden_hiroyuki_discomfort_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hiroyuki_relieved.png",      "event/bedridden/bedridden_hiroyuki_relieved_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hiroyuki_shout.png",         "event/bedridden/bedridden_hiroyuki_shout_overlay.png", [RESIZE_1080P]),
    ("@Event Art/Bedridden/overlay/hiroyuki_smile.png",         "event/bedridden/bedridden_hiroyuki_smile_overlay_large.png"),
    ("@Event Art/Bedridden/overlay/hiroyuki_listen.png",         "event/bedridden/bedridden_hiroyuki_listen_overlay_large.png"),
    # chapter 33
    ("reference/Event Art/Akira Past/akirapast_dinnerargument.jpg", "event/akirapast/akirapast_argument.jpg"),
    ("reference/Event Art/Akira Past/akirapast_elementary.jpg", "event/akirapast/akirapast_elemschool.jpg"),
    ("reference/Event Art/Akira Past/akirapast_grandparents1.jpg", "event/akirapast/akirapast_grandparents1.jpg"),
    ("reference/Event Art/Akira Past/akirapast_grandparents2.jpg", "event/akirapast/akirapast_grandparents2.jpg"),
    ("reference/Event Art/Akira Past/akirapast_middleschool.jpg", "event/akirapast/akirapast_midschool.jpg"),
    ("reference/Event Art/Akira Past/akirapast_promotion.jpg", "event/akirapast/akirapast_promotion.jpg"),
    ("reference/Event Art/Akira Past/akirapast_studying1.jpg", "event/akirapast/akirapast_study1.jpg"),
    ("reference/Event Art/Akira Past/akirapast_studying2.jpg", "event/akirapast/akirapast_study2.jpg"),
    ("reference/Event Art/Akira Past/akirapast_unfavorite.jpg", "event/akirapast/akirapast_unfavorite.jpg"),
    ("reference/Event Art/Akira Past/akirapast_vacation.jpg", "event/akirapast/akirapast_vacation.jpg"),
    # blurred sprites
    ("sprites/takawa/close/takawa_serious_close.png", "sprites/takawa/close/takawa_serious_close_blur1.png", [blur(3)]),
    ("sprites/takawa/close/takawa_serious_close.png", "sprites/takawa/close/takawa_serious_close_blur2.png", [blur(6)]),
    ("sprites/takawa/close/takawa_smile_close.png", "sprites/takawa/close/takawa_smile_close_blur1.png", [blur(3)]),
    ("sprites/takawa/close/takawa_smile_close.png", "sprites/takawa/close/takawa_smile_close_blur2.png", [blur(6)]),
    # close sprites
    ## hanako
    ("sprites/hanako/hanako_basic_bashful_sum.png",         "sprites/hanako/close/hanako_basic_bashful_sum_close.png",      [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_basic_bashful_sum_clip.png",    "sprites/hanako/close/hanako_basic_bashful_sum_clip_close.png", [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_basic_normal_sum_clip.png",     "sprites/hanako/close/hanako_basic_normal_sum_clip_close.png",  [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_basic_worry_sum.png",           "sprites/hanako/close/hanako_basic_worry_sum_close.png",        [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_basic_worry_sum_clip.png",      "sprites/hanako/close/hanako_basic_worry_sum_clip_close.png",   [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_cover_bashful_sum.png",         "sprites/hanako/close/hanako_cover_bashful_sum_close.png",      [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_cover_distant_sum.png",         "sprites/hanako/close/hanako_cover_distant_sum_close.png",      [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_cover_worry_sum.png",           "sprites/hanako/close/hanako_cover_worry_sum_close.png",        [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_defarms_worry_sum.png",         "sprites/hanako/close/hanako_defarms_worry_sum_close.png",      [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_downsmile_sum.png",         "sprites/hanako/close/hanako_emb_downsmile_sum_close.png",      [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_downsmile_sum_clip.png",    "sprites/hanako/close/hanako_emb_downsmile_sum_clip_close.png", [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_downtimid_sum.png",         "sprites/hanako/close/hanako_emb_downtimid_sum_close.png",      [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_emb_sum_clip.png",          "sprites/hanako/close/hanako_emb_emb_sum_clip_close.png",       [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_sad_sum.png",               "sprites/hanako/close/hanako_emb_sad_sum_close.png",            [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_sad_sum_clip.png",          "sprites/hanako/close/hanako_emb_sad_sum_clip_close.png",       [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_smile_sum.png",             "sprites/hanako/close/hanako_emb_smile_sum_close.png",          [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_smile_sum_clip.png",        "sprites/hanako/close/hanako_emb_smile_sum_clip_close.png",     [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_timid_sum.png",             "sprites/hanako/close/hanako_emb_timid_sum_close.png",          [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ("sprites/hanako/hanako_emb_timid_sum_clip.png",        "sprites/hanako/close/hanako_emb_timid_sum_clip_close.png",     [upscale(), resize(targetwidth=707), crop(0, 215, 707, 1296)]),
    ## lilly
    ("sprites/lilly/lilly_basic_listen_sum.png",        "sprites/lilly/close/lilly_basic_listen_sum_close.png",     [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_basic_planned_sum.png",       "sprites/lilly/close/lilly_basic_planned_sum_close.png",    [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_basic_surprised_sum.png",     "sprites/lilly/close/lilly_basic_surprised_sum_close.png",  [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_cane_listen_sum.png",         "sprites/lilly/close/lilly_cane_listen_sum_close.png",      [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_cane_smile_sum.png",          "sprites/lilly/close/lilly_cane_smile_sum_close.png",       [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_cane_smileclosed_sum.png",    "sprites/lilly/close/lilly_cane_smileclosed_sum_close.png", [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_cane_reminisce_sum.png",      "sprites/lilly/close/lilly_cane_reminisce_sum_close.png",   [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_cane_weaksmile_sum.png",      "sprites/lilly/close/lilly_cane_weaksmile_sum_close.png",   [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_cane_concerned_sum.png",      "sprites/lilly/close/lilly_cane_concerned_sum_close.png",   [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_cane_displeased_sum.png",     "sprites/lilly/close/lilly_cane_displeased_sum_close.png",  [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
    ("sprites/lilly/lilly_cane_sad_sum.png",            "sprites/lilly/close/lilly_cane_sad_sum_close.png",         [upscale(), resize(targetwidth=797), crop(0, 124, 797, 1204)]),
]

PHOTOGRAPHS: list[tuple[str, str, list[ImageTransformation]]] = [
    # chapter 28
    ("event/planeride/planeride_bliss.jpg", "gui/journal/p01.jpg", [crop(300, 0, 1920, 1080), resize(525, 350)]),
    ("bgs/inverness_street.jpg", "gui/journal/p02.jpg", [CompositeTransformation([(700, 0, "sprites/hanako/hanako_emb_smile_sum.png"), (300, 0, "sprites/hisao/hisao_cross_smile_polo.png")]), crop(150, 0, 1770, 1080), resize(525, 350)]),
    ("bgs/inverness_tree.jpg", "gui/journal/p03.jpg", [CompositeTransformation([(384, 0, "sprites/lilly/lilly_basic_cheerful_sum.png"), (1074, 30, "sprites/hanako/hanako_basic_bashful_sum.png"), (692, 30, "sprites/hisao/hisao_basic_smile_polo.png")]), crop(162, 0, 1782, 1080), resize(525, 350)]),
    ("reference/Backgrounds/cawthorn.jpg", "gui/journal/p07.jpg", [CompositeTransformation([(338, 50, "sprites/hisao/hisao_basic_grin_polo.png")]), resize(525, 350)]),
    ("reference/Journal/photos/p10.jpg", "gui/journal/p10.jpg", [CompositeTransformation([(793, 200, "sprites/lilly/lilly_cane_giggle_sum.png"), (1199, 200, "sprites/akira/akira_basic_cheerful_cas.png")]), crop(165, 220, 1756, 1280), resize(525, 350)]),
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
    ("reference/journal/doodles/IMG_2105.png", "gui/journal/d16a.png", [crop(134, 270, 644, 730), resize(targetheight=70)]),
    ("reference/journal/doodles/IMG_2105.png", "gui/journal/d16b.png", [crop(838, 139, 1388, 625), resize(targetheight=70)]),
    ("reference/journal/doodles/IMG_2105.png", "gui/journal/d16c.png", [crop(1558, 317, 2000, 836), resize(targetheight=76)]),
    ("reference/journal/doodles/IMG_2105.png", "gui/journal/d16d.png", [crop(334, 1001, 788, 1504), resize(targetheight=76)]),
    ("reference/journal/doodles/IMG_2105.png", "gui/journal/d16e.png", [crop(1442, 1021, 1880, 1525), resize(targetheight=76)]),
    ("reference/journal/doodles/IMG_2106.png", "gui/journal/d17.png", [crop(171, 112, 1806, 1593), resize(targetheight=200)]),
    ("reference/journal/doodles/IMG_2106_nt.png", "gui/journal/d17nt.png", [crop(171, 112, 1806, 1593), resize(targetheight=200)]),
    ("reference/journal/doodles/IMG_2118.png", "gui/journal/d18.png", [crop(548, 40, 1710, 1508), resize(targetheight=220)]),
    ("reference/journal/doodles/IMG_2070.png", "gui/journal/d19.png", [crop(586, 369, 1458, 1460), resize(targetheight=180)]),
    ("reference/journal/doodles/IMG_2108_v2.png", "gui/journal/d20.png", [crop(16, 112, 2450, 1468), resize(targetheight=240)]),
    ("reference/journal/doodles/IMG_2109.png", "gui/journal/d21.png", [crop(82, 120, 2060, 1424), resize(targetheight=220)]),
    ("reference/journal/doodles/IMG_2109_nt.png", "gui/journal/d21nt.png", [crop(82, 120, 2060, 1424), resize(targetheight=220)]),
    ("reference/journal/doodles/IMG_2110.png", "gui/journal/d22.png", [crop(142, 222, 2048, 1426), resize(targetheight=230)]),
    ("reference/journal/doodles/IMG_2111.png", "gui/journal/d23.png", [crop(124, 384, 2048, 1214), resize(targetheight=135)]),
    ("reference/journal/doodles/IMG_2116.png", "gui/journal/d24.png", [crop(44, 44, 2034, 1534), resize(targetheight=200)]),
    ("reference/journal/doodles/IMG_2112_nt.png", "gui/journal/d24nt.png", [crop(44, 44, 2034, 1534), resize(targetheight=200)]),
    ("reference/journal/doodles/IMG_2113.png", "gui/journal/d25.png", [crop(260, 468, 1934, 1210), resize(targetheight=150)]),
    ("reference/journal/doodles/IMG_2114.png", "gui/journal/d26.png", [crop(232, 40, 1934, 1620), resize(targetheight=210)]),
    ("reference/journal/doodles/IMG_2115.png", "gui/journal/d27.png", [crop(94, 88, 2070, 1620), resize(targetheight=260)]),
    ("reference/journal/doodles/IMG_2115_nt.png", "gui/journal/d27nt.png", [crop(94, 88, 2070, 1620), resize(targetheight=260)]),
    ("reference/journal/doodles/IMG_2069.png", "gui/journal/d28.png", [crop(0, 103, 2027, 1620), resize(targetheight=250)])
]


def main(args: dict):
    global waifu2x_path
    if "waifu2x" in args and args["waifu2x"] is not None:
        waifu2x_path = Path(args["waifu2x"])
    update_paths(args)

    images_to_process: list[ImageProcess] = []
    for entry in IMAGES + PHOTOGRAPHS:
        transforms = []
        if len(entry) == 3:
            transforms = entry[2]
        inpath = resolve_path(entry[0])
        outpath = resolve_path(entry[1])
        if entry in IMAGES and entry[1].endswith(".jpg"):
            transforms.append(CHECK_1080P)
            transforms.append(convert_rgb())
        images_to_process.append(ImageProcess(inpath, outpath, transforms, quality=90))

    for process in images_to_process:
        process.transform(args["replace"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sisterhood image export tool"
    )
    add_arguments(parser, refdir=True)
    parser.add_argument("-w", "--waifu2x", required=False, help="location of waifu2x CLI tool")
    parser.add_argument("-e", "--replace", action="store_true", default=False, help="whether to replace pre-existing image files")
    main(vars(parser.parse_args(sys.argv[1:])))
