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
    define iwa_ = Character(_("Girl"), who_color="#ffffff")

    image shrdraw_heart = Text(_("{size=133}{font=symbols}♡"))
    image shrdraw_plus1 = Text(_("{size=133}{font=symbols}♡{/font} + 1"))
    image shrdraw_plus2 = Text(_("{size=133}{font=symbols}♡{/font} + 2"))
    image shrdraw_times10 = Text(_("{size=133}{font=symbols}♡{/font} x 10"))
    image shrdraw_times100 = Text(_("{size=133}{font=symbols}♡{/font} x 100"))
    image shrdraw_mathismypassion = Text(_("{size=133}{font=symbols}π²{/font}! x {font=symbols}♡"))
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

    define config.font_name_map["symbols"] = f"{sh_path}/font/Symbols.ttf"

init 30 python:
    sisterhood_chapters.append(
        (_("Act 3"), [
            (_("Week at Hisao's"), "sh_ch35.s1", _("Hanako wakes up in Hisao's home and catches up with Lilly.")),
            (_("Love is War"), "sh_ch35.s2", _("The lovebirds eat Hanako's home-cooked breakfast.")),
            (_("Aquatic Artplay"), "sh_ch35.s3", _("Hanako and Hisao have some fun in the shower.")),
            (_("A Blast from his Past"), "sh_ch36.s1", _("Hanako has an unexpected encounter during a karaoke date with Hisao.")),
            (_("Lady of the House"), "sh_ch37.s1", _("Lilly looks after her father in her mother's absence."), "lilly"),
            (_("Through Your Eyes"), "sh_ch37.s2", _("Lilly and her father start bonding with one another."), "lilly")
        ])
    )

    sh_sprites("hisao", ["bashful", "emb", "smileclosed"], poses=["basic"], outfits=["bath", "polo"])
    sh_sprites("hiroyuki", ["smileclosed"])

    phonebox_sprites("akira", ["basic_smug", "basic_sweet"])
    phonebox_sprites("lilly", ["basic_smileclosed", "basic_weaksmile", "cane_satisfied", "cane_giggle", "cane_sleepy"], cropyoff=-40)

    sh_bgs("hisao", ["livingroom", "kitchen", "bedroom"])
    sh_bgs("city", ["karaokebooth"])
    sh_bgs("satou", ["masterbed_ni"])

    sh_event("bedside", ["headsets", "papers", "sit", "soup", "wine"])

    sh_register_sfx([
        # credit: Universfield of Pixabay
        "winecork"
    ])
