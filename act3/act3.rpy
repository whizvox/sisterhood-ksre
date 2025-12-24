init 30:
    transform showertext(x, y, rotation_start, rotation_end):
        pos (x, y) anchor (0.5, 0.5) rotate rotation_start alpha 0.0
        parallel:
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.0
        parallel:
            linear 2.0 rotate rotation_end

    define hid = Character(_("Dad"), who_color="#ffffff", screen="say_sh")
    define him = Character(_("Mom"), who_color="#ffffff", screen="say_sh")

    image shrdraw_heart = Text(_("{image=mods/sisterhood/vfx/shrdraw/heart.png}"))
    image shrdraw_plus1 = Text(_("{image=mods/sisterhood/vfx/shrdraw/heart.png}{size=133} + 1"))
    image shrdraw_plus2 = Text(_("{image=mods/sisterhood/vfx/shrdraw/heart.png}{size=133} + 2"))
    image shrdraw_times10 = Text(_("{image=mods/sisterhood/vfx/shrdraw/heart.png}{size=133} x 10"))
    image shrdraw_times100 = Text(_("{image=mods/sisterhood/vfx/shrdraw/heart.png}{size=133} x 100"))
    image shrdraw_mathismypassion = Text(_("{image=mods/sisterhood/vfx/shrdraw/pi.png}{image=mods/sisterhood/vfx/shrdraw/squared.png}{size=133}! x {image=mods/sisterhood/vfx/shrdraw/heart.png}{size=133}"))
    image shrdraw_cutiepie = Text(_("{size=133}CUTIEPIE"))
    image shrdraw_honeybun = Text(_("{size=133}HONEYBUN"))
    image shrdraw_sunshine = Text(_("{size=133}SUNSHINE"))
    image shrdraw_cupcake = Text(_("{size=133}CUPCAKE"))
    image shrdraw_cuddlebug = Text(_("{size=133}CUDDLEBUG"))
    image shrdraw_sweetheart = Text(_("{size=133}SWEETHEART"))
    image shrdraw_sweetheart_big = Text(_("{size=160}SWEETHEART!!!"))
    image shrdraw_buttercup = Text(_("{size=133}BUTTERCUP"))
    image shrdraw_dumpling = Text(_("{size=133}DUMPLING"))
    image shrdraw_songbird = Text(_("{size=133}SONGBIRD"))
    image shrdraw_snugglywuggle = Text(_("{size=133}SNUGGLYWUGGLE"))
    image shrdraw_beautiful = Text(_("{size=133}BEAUTIFUL"))

init 30 python:
    sisterhood_chapters.append(
        (_("Act 3"), [
            (_("Not-Yet Familiar Ceiling"), "sh_ch35.s1", _("Hanako wakes up in Hisao's living room and catches up with Lilly.")),
            (_("Love is War"), "sh_ch35.s2", _("The lovebirds eat Hanako's home-cooked breakfast.")),
            (_("Aquatic Art Class"), "sh_ch35.s3", _("Hanako and Hisao have some fun in the shower."))
        ])
    )

    sh_sprites("hisao", ["bashful", "emb"], poses=["basic"], outfits=["bath"])

    phonebox_sprites("lilly", ["basic_smileclosed", "basic_weaksmile", "cane_satisfied", "cane_giggle", "cane_sleepy"], cropyoff=-40)

    sh_bgs("hisao", ["livingroom", "kitchen", "bedroom"])
