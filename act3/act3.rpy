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
    define yui = Character(_("Yuichi"), who_color="#b37b7b")
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

    image shlogotext = f"{sh_path}/logo/logo_text.png"
    image shlogo brokenquill = f"{sh_path}/logo/logo_brokenquill.png"

    image ev pillowtalk dark2 = f"{sh_path}/event/pillowtalk/pillowtalk_dark2.png"
    image pillowtalkhanako up dark2 = f"{sh_path}/event/pillowtalk/pillowtalk_hanako_up_dark2.png"
    image pillowtalkhanako down dark2 = f"{sh_path}/event/pillowtalk/pillowtalk_hanako_down_dark2.png"

    define config.font_name_map["symbols"] = f"{sh_path}/font/Symbols.ttf"

init 30 python:
    sisterhood_chapters.append(
        (_("Act 3"), [
            (_("Week at Hisao's"), "sh_ch35.s1", _("Hanako wakes up in Hisao's home and catches up with Lilly.")),
            (_("Love is War"), "sh_ch35.s2", _("The lovebirds eat Hanako's home-cooked breakfast.")),
            (_("Aquatic Artplay"), "sh_ch35.s3", _("Hanako and Hisao have some fun in the shower.")),
            (_("A Blast from his Past"), "sh_ch36.s1", _("Hanako has an unexpected encounter during a karaoke date with Hisao.")),
            (_("Lady of the House"), "sh_ch37.s1", _("Lilly looks after her father in her mother's absence."), "lilly"),
            (_("Through Your Eyes"), "sh_ch37.s2", _("Lilly and her father start bonding with one another."), "lilly"),
            (_("Second Homecoming"), "sh_ch38.s1", _("Hanako and Hisao welcome Lilly back to Japan... again."), "hanako"),
            (_("Life Choices"), "sh_ch38.s2", _("Hanako has tea with Lilly and Karla and is let in on some surprising news."), "hanako"),
            (_("Answering the Muse's Call"), "sh_ch39.s1", _("Hanako lets Lilly and Karla in on the establishment of a new writing club"), "hanako"),
            (_("The Quill is Mightier than the Sword"), "sh_ch39.s2", _("Hanako attends the first meeting of the club."), "hanako"),
            (_("Perspective Shift"), "sh_ch39.s3", _("Hanako and Jun reflect on the evening's events."), "hanako"),
            (_("Just Friends"), "sh_ch40.s1", _("While visiting Japan, Akira has dinner with her former boyfriend."), "akira"),
            (_("Just Friends?"), "sh_ch40.s2", _("Akira and her ex discuss office politics and inheritance."), "akira")
        ])
    )

    sh_sprites("jun", ["confused", "disturbed", "sadclosed", "sheepish", "smileclosed"], poses=["basic"])
    sh_sprites("karla", ["sad", "smileclosed", "wut"], poses=["basic", "cross"], outfits=["cas"])
    sh_sprites("lilly", ["displeased", "emb", "overjoyed"], poses=["basic", "cane"], outfits=["cas"])
    sh_sprites("hiroyuki", ["awkward", "smileclosed"])
    sh_sprites("hisao", ["bashful", "emb", "smileclosed"], poses=["basic"], outfits=["bath", "polo"])
    sh_sprites("naomi", ["annoyed", "confused", "grinclosed", "seizure"], poses=["basic"])
    sh_sprites("shizu", ["evil"], poses=["adjust"])

    phonebox_sprites("akira", ["basic_smug", "basic_sweet"])
    phonebox_sprites("lilly", ["basic_cheerful_sum", "basic_smileclosed", "basic_smileclosed_sum", "basic_smile_sum", "basic_reminisce_sum", "basic_weaksmile", "basic_weaksmile_sum", "cane_satisfied", "cane_satisfied_sum", "cane_giggle", "cane_sleepy"], cropyoff=-40)

    sh_bgs("hisao", ["livingroom", "kitchen", "bedroom"])
    sh_bgs("city", ["karaokebooth"])
    sh_bgs("satou", ["masterbed_ni"])
    # credit: Loyola University Maryland
    sh_bgs("school", ["dormkitchen", "dormnaomi"])
    # credit: japan-property.jp and Tokyo Furnished LLC
    sh_bgs("yuichi", ["intercom", "genkan", "dining"])
    # credit: OMOSHIRO RENT-A-CAR
    sh_bgs("misc", ["car_ss"])

    sh_event("bedside", ["headsets", "papers", "sit", "soup", "wine"])

    sh_register_sfx([
        # credit: Universfield of Pixabay
        "winecork"
    ])

label sisterhood_timeskip_broken:
    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    pause 2.0

    play music music_timeskip

    show shlogo brokenquill at Transform(xalign=0.5, yalign=0.5)
    with CropMove(2.0, "wipedown")

    show shlogotext at Transform(xalign=0.5, yalign=0.5)
    with CropMove(2.0, "wiperight")

    pause 2.0

    stop music fadeout 2.0

    scene black
    with erase

    pause 2.0

    return