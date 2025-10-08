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
    ("sprite edits/hisao/Uni Sweet", "basic_sweet_uni"),
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
    ("sprites2/Re Hisao Nakai/Nak Revised/REV3-Blush", "basic_blush_nak"),
    ("sprites2/Re Hisao Nakai/Nak Revised/REV4-Frown", "basic_frown_nak"),
    ("sprites2/Re Hisao Nakai/Nak Revised/REV5-Grin", "basic_grin_nak"),
    ("sprites2/Re Hisao Nakai/Nak Revised/REV1-Neutral", "basic_neutral_nak"),
    ("sprites2/Re Hisao Nakai/Nak Revised/REV6-Smile-Happy", "basic_smile_nak"),
    ("sprites2/Re Hisao Nakai/Nak Revised/REV2-Speak", "basic_speak_nak"),
    ("sprites2/Re Hisao Nakai/Nak Revised/REV7-Worry", "basic_worry_nak"),
    ("sprite edits/hisao/Nak Sweet", "basic_sweet_nak")
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
    ("sprites2/Naomi Inoue/Naomi bend wink", "bend_wink"),
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

jun = [
    # basic
    ("act 2 sprites/jun revised/basic/1 JUN'S SMILE", "basic_smile"),
    ("act 2 sprites/jun revised/basic/2 JUN'S HAPPY", "basic_happy"),
    ("act 2 sprites/jun revised/basic/3 JUN'S SAD", "basic_sad"),
    ("act 2 sprites/jun revised/basic/4 JUN'S SERIOUS", "basic_serious"),
    ("act 2 sprites/jun revised/basic/5 JUN'S EYEROLL", "basic_pout"),
    ("act 2 sprites/jun revised/basic/6 JUN'S SPEAK", "basic_speak"),
    ("act 2 sprites/jun revised/basic/7 JUN'S SMUG", "basic_smug"),
    ("act 2 sprites/jun revised/basic/8 JUN'S LAUGH", "basic_laugh"),
    ("act 2 sprites/jun revised/basic/9 JUN'S WEAK SMILE", "basic_weaksmile"),
    ("act 2 sprites/jun revised/basic/10 JUN'S ANNOYED", "basic_angry"),
    ("act 2 sprites/jun adjust/basic annoyed", "basic_annoyed"),
    ("act 2 sprites/jun adjust/basic eyeroll", "basic_eyeroll"),
    # cast
    ("act 2 sprites/jun revised/cast/1 JUN'S SMILE", "cast_smile"),
    ("act 2 sprites/jun revised/cast/2 JUN'S HAPPY", "cast_happy"),
    ("act 2 sprites/jun revised/cast/3 JUN'S SAD", "cast_sad"),
    ("act 2 sprites/jun revised/cast/4 JUN'S SERIOUS", "cast_serious"),
    ("act 2 sprites/jun revised/cast/5 JUN'S EYEROLL", "cast_pout"),
    ("act 2 sprites/jun revised/cast/6 JUN'S SPEAK", "cast_speak"),
    ("act 2 sprites/jun revised/cast/7 JUN'S SMUG", "cast_smug"),
    ("act 2 sprites/jun revised/cast/8 JUN'S LAUGH", "cast_laugh"),
    ("act 2 sprites/jun revised/cast/9 JUN'S WEAK SMILE", "cast_weaksmile"),
    ("act 2 sprites/jun revised/cast/10 JUN'S ANNOYED", "cast_angry"),
    ("act 2 sprites/jun adjust/cast annoyed", "cast_annoyed"),
    ("act 2 sprites/jun adjust/cast eyeroll", "cast_eyeroll"),
    # raised
    ("act 2 sprites/jun revised/raised/7 JUN'S SMUG", "raise_smug"),
    ("act 2 sprites/jun revised/raised/8 JUN'S LAUGH", "raise_laugh"),
    # cast+raised
    ("act 2 sprites/jun revised/cast + raised/7 JUN'S SMUG", "castraise_smug"),
    ("act 2 sprites/jun revised/cast + raised/8 JUN'S LAUGH", "castraise_laugh")
]

nakamura = [
    ("act 2 sprites/nakamura adjust/speak", "speak"),
    ("act 2 sprites/nakamura adjust/instruct", "instruct"),
    ("act 2 sprites/nakamura adjust/smile", "smile"),
    ("act 2 sprites/nakamura adjust/awkward", "awkward"),
    ("act 2 sprites/nakamura adjust/neutral", "neutral"),
    ("act 2 sprites/NAKAMURA/6 STRAIN", "strain"),
    ("act 2 sprites/NAKAMURA/7 BOW", "bow"),
    ("act 2 sprites/nakamura adjust/thinking", "thinking")
]

karla = [
    # suit
    ("act 2 sprites/Karla/SUIT/1 KARLA SUIT SMILE", "basic_smile"),
    ("act 2 sprites/Karla/SUIT/2 KARLA SUIT SMILE CLOSED", "basic_smileclosed"),
    ("act 2 sprites/Karla/SUIT/3 KARLA SUIT SHEEPISH", "basic_sheepish"),
    ("act 2 sprites/Karla/SUIT/4 KARLA SUIT SHEEPISH CLOSED", "basic_sheepishclosed"),
    ("act 2 sprites/Karla/SUIT/5 KARLA SUIT CHEERFUL", "basic_cheerful"),
    ("act 2 sprites/Karla/SUIT/6 KARLA SUIT SMUG", "basic_smug"),
    ("act 2 sprites/Karla/SUIT/7 KARLA SUIT TROUBLED", "basic_troubled"),
    ("act 2 sprites/Karla/SUIT/8 KARLA SUIT DISPLEASED", "basic_displeased"),
    ("act 2 sprites/Karla/SUIT/9 KARLA SUIT DISPLEASED CROSSED", "cross_displeased"),
    ("act 2 sprites/Karla/SUIT/10 KARLA SUIT ANGRY", "basic_angry"),
    ("act 2 sprites/Karla/SUIT/11 KARLA SUIT ANGRY CROSSED", "cross_angry"),
    ("act 2 sprites/Karla/SUIT/12 KARLA SUIT LAUGH", "basic_laugh"),
    ("act 2 sprites/Karla/SUIT/13 KARLA SUIT CONFUSED", "basic_confused"),
    ("act 2 sprites/Karla/SUIT/14 KARLA SUIT SERIOUS", "basic_serious"),
    ("act 2 sprites/Karla/SUIT/15 KARLA SUIT SPEAK", "basic_speak"),
    ("act 2 sprites/Karla/SUIT/16 KARLA SUIT DISTANT", "basic_distant"),
    ("act 2 sprites/Karla/SUIT/17 KARLA SUIT PONDER", "basic_ponder"),
    ("act 2 sprites/Karla/SUIT/18 KARLA SUIT PONDER CROSSED", "cross_ponder"),
    ("act 2 sprites/Karla/SUIT/19 KARLA SUIT WORRIED", "basic_worried"),
    # casual
    ("act 2 sprites/Karla/CASUAL/1 KARLA CASUAL SMILE", "basic_smile_cas"),
    ("act 2 sprites/Karla/CASUAL/2 KARLA CASUAL SMILE CLOSED", "basic_smileclosed_cas"),
    ("act 2 sprites/Karla/CASUAL/3 KARLA CASUAL SHEEPISH", "basic_sheepish_cas"),
    ("act 2 sprites/Karla/CASUAL/4 KARLA CASUAL SHEEPISH CLOSED", "basic_sheepishclosed_cas"),
    ("act 2 sprites/Karla/CASUAL/5 KARLA CASUAL CHEERFUL", "basic_cheerful_cas"),
    ("act 2 sprites/Karla/CASUAL/6 KARLA CASUAL SMUG", "basic_smug_cas"),
    ("act 2 sprites/Karla/CASUAL/7 KARLA CASUAL TROUBLED", "basic_troubled_cas"),
    ("act 2 sprites/Karla/CASUAL/8 KARLA CASUAL DISPLEASED", "basic_displeased_cas"),
    ("act 2 sprites/Karla/CASUAL/9 KARLA CASUAL DISPLEASED CROSSED", "cross_displeased_cas"),
    ("act 2 sprites/Karla/CASUAL/10 KARLA CASUAL ANGRY", "basic_angry_cas"),
    ("act 2 sprites/Karla/CASUAL/11 KARLA CASUAL ANGRY CROSSED", "cross_angry_cas"),
    ("act 2 sprites/Karla/CASUAL/12 KARLA CASUAL LAUGH", "basic_laugh_cas"),
    ("act 2 sprites/Karla/CASUAL/13 KARLA CASUAL CONFUSED", "basic_confused_cas"),
    ("act 2 sprites/Karla/CASUAL/14 KARLA CASUAL SERIOUS", "basic_serious_cas"),
    ("act 2 sprites/Karla/CASUAL/15 KARLA CASUAL SPEAK", "basic_speak_cas"),
    ("act 2 sprites/Karla/CASUAL/16 KARLA CASUAL DISTANT", "basic_distant_cas"),
    ("act 2 sprites/Karla/CASUAL/17 KARLA CASUAL PONDER", "basic_ponder_cas"),
    ("act 2 sprites/Karla/CASUAL/18 KARLA CASUAL PONDER CROSSED", "cross_ponder_cas"),
    ("act 2 sprites/Karla/CASUAL/19 KARLA CASUAL WORRIED", "basic_worried_cas")
]

hiroyuki = [
    ("act 2 sprites/HIROYUKI/BOW", "bow"),
    ("act 2 sprites/HIROYUKI/RAISED EYEBROW", "eyebrow"),
    ("act 2 sprites/HIROYUKI/SMILE", "smile"),
    ("act 2 sprites/HIROYUKI/SPEAK", "speak"),
    ("act 2 sprites/HIROYUKI/STERN", "stern"),
    ("act 2 sprites/HIROYUKI/STRAINED", "strained"),
    ("act 2 sprites/HIROYUKI/THINKING", "thinking")
]

def main():
    import sys

    replace = []

    for arg in sys.argv:
        if arg.startswith("--replace="):
            chars = arg[10:].lower()
            if chars == "all":
                replace.extend(["hisao", "takawa", "naomi", "natsume", "hanako", "jun", "nakamura", "karla", "hiroyuki"])
            else:
                replace.extend(chars.split(","))
    
    replace_hisao = "hisao" in replace
    replace_takawa = "takawa" in replace
    replace_naomi = "naomi" in replace
    replace_natsume = "natsume" in replace
    replace_hanako = "hanako" in replace
    replace_jun = "jun" in replace
    replace_nakamura = "nakamura" in replace
    replace_karla = "karla" in replace

    for entry in hisao:
        if "Nak" not in entry[0]:
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
    
    for entry in jun:
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/jun/jun_{entry[1]}.png", replace=replace_jun, crop=(127, 18, 833, 1807), target_height=1020)
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/jun/close/jun_{entry[1]}_close.png", replace=replace_jun, crop=(127, 18, 833, 1200), target_height=1080)
    
    for entry in nakamura:
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/nakamura/nakamura_{entry[1]}.png", replace=replace_nakamura, crop=(0, 108, 1200, 1690), target_height=1020)
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/nakamura/close/nakamura_{entry[1]}_close.png", replace=replace_nakamura, crop=(0, 108, 1200, 1188), target_height=1080)

    for entry in karla:
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/karla/karla_{entry[1]}.png", replace=replace_karla, crop=(0, 126, 1050, 1846), target_height=1020)
        crop_and_resize_image(f"../reference/{entry[0]}.png", f"../sprites/karla/close/karla_{entry[1]}_close.png", replace=replace_karla, crop=(0, 126, 1050, 1206), target_height=1080)

if __name__ == "__main__":
    main()