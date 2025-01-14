from PIL import Image
import os

RESAMPLE_METHOD = Image.BICUBIC

def crop_and_resize_image(input_path: str,
                  output_path: str,
                  replace: bool = False,
                  crop: tuple[int, int] | None = None,
                  target_width: int | None = None,
                  target_height: int | None = None):
    if os.path.exists(output_path) and not replace:
        return
    try:
        im = Image.open(input_path)
    except:
        print(f"(ERROR) Could not process image: {input_path}")
        return
    print(f"Processing <{input_path}>, exporting to <{output_path}>")
    if crop is not None:
        im = im.crop(crop)
    new_width = 0
    new_height = 0
    if target_width is not None:
        if target_height is not None:
            new_width = target_width
            new_height = target_height
        else:
            new_width = target_width
            new_height = int((target_width / im.width) * im.height)
    else:
        if target_height is not None:
            new_width = int((target_height / im.height) * im.width)
            new_height = target_height
        else:
            new_width = im.width
            new_height = im.height
    if im.width != new_width or im.height != new_height:
        im = im.resize((new_width, new_height), resample=RESAMPLE_METHOD)
    parent_dir = os.path.dirname(output_path)
    if not os.path.isdir(parent_dir):
        os.mkdir(os.path.dirname(output_path))
    im.save(output_path)

hisao = [
    # Uniform
    ("sprites2/Re Hisao Nakai/Uniform/Uni Annoy", "basic_annoy_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uni Blush", "basic_blush_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uni Frown", "basic_frown_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uni Grin", "basic_grin_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uni Happy-Smile", "basic_smile_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uni Neutral", "basic_neutral_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uni Pout", "basic_pout_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uni Speak", "basic_speak_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uni Worry", "basic_worry_uni"),
    ("sprite edits/hisao/Uni Neutral-Blush", "basic_neutralblush_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Annoy", "cross_annoy_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Blush", "cross_blush_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Frown", "cross_frown_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Grin", "cross_grin_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Happy-Smile", "cross_smile_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Neutral", "cross_neutral_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Pout", "cross_pout_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Speak", "cross_speak_uni"),
    ("sprites2/Re Hisao Nakai/Uniform/Uniform Crossed/UCrossed-Worry", "cross_worry_uni"),
    # Polo
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Annoy", "basic_annoy_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Blush", "basic_blush_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Frown", "basic_frown_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Grin", "basic_grin_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Smile-Happy", "basic_smile_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Neutral", "basic_neutral_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Pout", "basic_pout_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Speak", "basic_speak_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo-Worry", "basic_worry_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Annoy", "cross_annoy_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Blush", "cross_blush_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Frown", "cross_frown_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Grin", "cross_grin_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Happy-Smile", "cross_smile_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Neutral", "cross_neutral_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Pout", "cross_pout_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Speak", "cross_speak_polo"),
    ("sprites2/Re Hisao Nakai/Polo Shirt/Polo Crossed/PCrossed-Worry", "cross_worry_polo"),
    # Sweater Vest
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Annoy", "basic_annoy_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Blush", "basic_blush_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Frown", "basic_frown_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Grin", "basic_grin_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Smile-Happy", "basic_smile_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Neutral", "basic_neutral_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Pout", "basic_pout_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Speak", "basic_speak_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/Sweater-Worry", "basic_worry_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Annoy", "cross_annoy_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Blush", "cross_blush_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Frown", "cross_frown_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Grin", "cross_grin_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Happy", "cross_smile_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Neutral", "cross_neutral_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Pout", "cross_pout_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Speak", "cross_speak_swt"),
    ("sprites2/Re Hisao Nakai/Sweater/S Crossed/SCrossed-Worry", "cross_worry_swt"),
    # Bathrobe
    ("sprites/Hisao Nakai/Bathrobe/Bathrb-Blush", "basic_blush_bath"),
    ("sprites/Hisao Nakai/Bathrobe/Bathrb-Grin", "basic_grin_bath"),
    ("sprites/Hisao Nakai/Bathrobe/Bathrb-Neutral", "basic_neutral_bath"),
    ("sprites/Hisao Nakai/Bathrobe/Bathrb-Smile-Happy", "basic_smile_bath"),
    ("sprites/Hisao Nakai/Bathrobe/Bathrb-Speak", "basic_speak_bath"),
    # Naked
    ("sprites/Hisao Nakai/Naked/Naked-Blush", "basic_blush_nak"),
    ("sprites/Hisao Nakai/Naked/Naked-Frown", "basic_frown_nak"),
    ("sprites/Hisao Nakai/Naked/Naked-Grin", "basic_grin_nak"),
    ("sprites/Hisao Nakai/Naked/Naked-Neutral", "basic_neutral_nak"),
    ("sprites/Hisao Nakai/Naked/Naked-Smile-Happy", "basic_smile_nak"),
    ("sprites/Hisao Nakai/Naked/Naked-Speak", "basic_speak_nak"),
    ("sprites/Hisao Nakai/Naked/Naked-Worry", "basic_worry_nak")
]

takawa = [
    ("sprites/Yumi Takawa fixed/takawa_calculating", "calculating"),
    ("sprites/Yumi Takawa fixed/takawa_happy", "happy"),
    ("sprites/Yumi Takawa fixed/takawa_serious", "serious"),
    ("sprites/Yumi Takawa fixed/takawa_smile", "smile"),
    ("sprites/Yumi Takawa fixed/takawa_stern", "stern"),
    ("sprites/Yumi Takawa fixed/takawa_worried", "worried"),
]

naomi = [
    ("sprites2/Naomi Inoue/Naomi bend grin", "bend_grin"),
    ("sprites2/Naomi Inoue/Naomi bend laugh", "bend_laugh"),
    ("sprites2/Naomi Inoue/Naomi bend smile", "bend_smile"),
    ("sprites2/Naomi Inoue/Naomi focused", "basic_focus"),
    ("sprites2/Naomi Inoue/Naomi grin", "basic_grin"),
    ("sprites2/Naomi Inoue/Naomi laugh", "basic_laugh"),
    ("sprites2/Naomi Inoue/Naomi neutral", "basic_neutral"),
    ("sprites2/Naomi Inoue/Naomi shocked", "basic_shock"),
    ("sprites2/Naomi Inoue/Naomi smile", "basic_smile"),
]

natsume = [
    ("sprites2/Ooe Natsume/Natsume b cheerful", "basic_cheerful"),
    ("sprites2/Ooe Natsume/Natsume b neutral", "basic_neutral"),
    ("sprites2/Ooe Natsume/Natsume b smile", "basic_smile"),
    ("sprites2/Ooe Natsume/Natsume h cheerful", "hands_cheerful"),
    ("sprites2/Ooe Natsume/Natsume h neutral", "hands_neutral"),
    ("sprites2/Ooe Natsume/Natsume h smile", "hands_smile"),
]

hanako = [
    ("hanako sprites upscaled/mednoise/hanako_basic_bashful_clip", "basic_bashful_clip"),
    ("hanako sprites upscaled/mednoise/hanako_basic_distant_clip", "basic_distant_clip"),
    ("hanako sprites upscaled/mednoise/hanako_basic_worry_clip", "basic_worry_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_blushtimid_cas_clip", "emb_blushtimid_cas_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_blushtimid_cas_nohat_clip", "emb_blushtimid_cas_nohat_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_downsmile_cas_clip", "emb_downsmile_cas_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_downsmile_cas_nohat_clip", "emb_downsmile_cas_nohat_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_downsmile_clip", "emb_downsmile_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_downtimid_cas_nohat_clip", "emb_downtimid_cas_nohat_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_emb_cas_clip", "emb_emb_cas_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_emb_cas_nohat_clip", "emb_emb_cas_nohat_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_emb_clip", "emb_emb_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_sad_cas_clip", "emb_sad_cas_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_sad_cas_nohat_clip", "emb_sad_cas_nohat_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_smile_cas_clip", "emb_smile_cas_clip"),
    ("hanako sprites upscaled/mednoise/hanako_emb_smile_cas_nohat_clip", "emb_smile_cas_nohat_clip"),
]

def main():
    import sys

    replace = []

    for arg in sys.argv:
        if arg.startswith("--replace="):
            chars = arg[10:].lower()
            if chars == "all":
                replace.extend(["hisao", "takawa", "naomi", "natsume", "hanako"])
            else:
                replace.extend(chars.split(","))
    
    replace_hisao = "hisao" in replace
    replace_takawa = "takawa" in replace
    replace_naomi = "naomi" in replace
    replace_natsume = "natsume" in replace
    replace_hanako = "hanako" in replace

    for entry in hisao:
        if "Naked" not in entry[0]:
            crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/hisao/hisao_{entry[1]}.png", replace=replace_hisao, crop=(0, 0, 1350, 2325), target_height=1080)
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/hisao/close/hisao_{entry[1]}_close.png", replace=replace_hisao, crop=(0, 0, 1350, 1650), target_height=1080)
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/hisao/superclose/hisao_{entry[1]}_superclose.png", replace=replace_hisao, crop=(0, 0, 1350, 1312), target_height=1080)

    for entry in takawa:
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/takawa/takawa_{entry[1]}.png", replace=replace_takawa, crop=(0, 0, 1350, 2295), target_height=935)
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/takawa/close/takawa_{entry[1]}_close.png", replace=replace_takawa, crop=(0, 0, 1350, 2062), target_height=1080)

    for entry in naomi:
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/naomi/naomi_{entry[1]}.png", replace=replace_naomi, target_height=1000)
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/naomi/close/naomi_{entry[1]}_close.png", replace=replace_naomi, crop=(0, 0, 1350, 1800), target_height=1080)
    
    for entry in natsume:
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/natsume/natsume_{entry[1]}.png", replace=replace_natsume, target_height=950)
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/natsume/close/natsume_{entry[1]}_close.png", replace=replace_natsume, crop=(0, 0, 1350, 1800), target_height=1030)

    for entry in hanako:
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/hanako/close/hanako_{entry[1]}_close.png", replace=replace_hanako, crop=(0, 272, 878, 1614), target_height=1080)
    
if __name__ == "__main__":
    main()