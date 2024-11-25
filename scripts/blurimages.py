import os
import sys
import pathlib
from PIL import Image, ImageFilter

def blur_image(in_path: str, out_path: str, blur_radius: int = 5) -> None:
    try:
        with Image.open(in_path) as im:
            print(f"Saving image <{in_path}> as blurred variant to <{out_path}>")
            blurred = im.filter(ImageFilter.GaussianBlur(blur_radius))
            blurred.save(out_path)
    except Exception as e:
        print(e)

images = (
    "event/hotel/hotel_1_large",
    "event/hotel/hotel_1",
    "event/hotel/hotel_2_large",
    "event/hotel/hotel_2",
    "event/hotel/hotel_3",
    "event/hotel/hotel_4_large",
    "event/hotel/hotel_4",
    "event/hotel/hotel_4a",
    "event/hotel/hotel_5",
    "event/hotel/hotel_5a"
)

def get_sisterhood_directory() -> str:
    sh_dir = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
    if not os.path.isdir(os.path.join(sh_dir, "logo")) or not os.path.isfile(os.path.join(sh_dir, "script-ch1.rpy")):
        raise Exception("Could not detect sisterhood directory!")
    return sh_dir

def main():
    sh_dir = get_sisterhood_directory()
    for imgpath in images:
        in_path = pathlib.Path(sh_dir, imgpath + ".jpg")
        out_path = pathlib.Path(in_path.parent, "blur", in_path.stem + "_blur" + in_path.suffix)
        out_path.parent.mkdir(exist_ok=True)
        blur_image(in_path, out_path, blur_radius=20)
    print("Finished blurring images")

if __name__ == "__main__":
    main()