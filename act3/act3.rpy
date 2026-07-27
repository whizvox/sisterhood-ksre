init 30:
    transform showertext(x, y, rotation_start, rotation_end):
        pos (x, y) anchor (0.5, 0.5) rotate rotation_start alpha 0.0
        parallel:
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.0
        parallel:
            linear 2.0 rotate rotation_end

    transform sh_drizzle_tf(my_offset, my_xzoom, my_yzoom):
        xalign 0.5 yalign 0.5 xzoom my_xzoom yzoom my_yzoom
        my_offset
        block:
            choice:
                f"{sh_path}/vfx/drizzle/drizzle1.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle2.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle3.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle4.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle5.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle6.png" with Dissolve(0.1)
                0.2
            repeat

    transform sh_fadebottomenter:
        ypos 1.2 alpha 0.0
        ease 1.0 ypos 1.0 alpha 1.0

    transform sh_fadebottomexit:
        ease 1.0 ypos 1.2 alpha 0.0

    transform sh_carbob:
        truecenter ypos 0.52
        block:
            ease 2.0 ypos 0.48
            ease 2.0 ypos 0.52
            repeat

    define clockwipefast = ImageDissolve(Tile("gui/trans/clockwipe.png"), 1.0, 8)

    define hid = Character(_("Dad"), who_color="#ffffff", screen="say_sh")
    define him = Character(_("Mom"), who_color="#ffffff", screen="say_sh")
    define yui = Character(_("Yuichi"), who_color="#b37b7b")
    define iwa_ = Character(_("Girl"), who_color="#ffffff")

    image naomi bend_laugh_superclose = f"{sh_path}/sprites/naomi/superclose/naomi_bend_laugh_superclose.png"

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

    image newclassphoto = sh_vfx("newclassphoto")
    image teddybear = sh_vfx("teddybear")
    image carseats = sh_vfx("carseats", boxstrip=False)
    image hankerchief = sh_vfx("hankerchief")
    image aedunit = sh_vfx("aed")
    image adoptionpapers1 = sh_vfx("adoptionpapers1", boxstrip=False)

    image bg kasshoku_grounds_ss = sunset(sh_bg("kasshoku_grounds"))
    image bg kasshoku_entrance_ss = sunset(sh_bg("kasshoku_entrance"))

    define config.font_name_map["symbols"] = f"{sh_path}/font/Symbols.ttf"

init 31:
    # credit: Marius Oberholster of Pixabay
    image drizzle = Composite(
        (1920, 1080),
        (0, 0), sh_drizzle(),
        (0, 0), sh_drizzle(0.1, -1.2, 1.2)
    )

init 30 python:
    def sh_drizzle(my_offset = 0.0, my_xzoom = 1.0, my_yzoom = 1.0):
        return sh_drizzle_tf(my_offset, my_xzoom, my_yzoom)


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
            (_("Just Friends?"), "sh_ch40.s2", _("Akira and her ex discuss office politics and inheritance."), "akira"),
            (_("Morning Practice"), "sh_ch41.s1", _("Hanako convinces Hisao to practice indoors for a change."), "hanako"),
            (_("Missing Star"), "sh_ch41.s2", _("Hanako learns that she and her club won a prize."), "hanako"),
            (_("Orientation"), "sh_ch41.s3", _("Hanako has a talk about her university applications with Mutou."), "hanako"),
            (_("The Promising Future"), "sh_ch41.s4", _("Hanako studies for the mock exams with Hisao and Lilly."), "hanako"),
            (_("Morning Prep"), "sh_ch42.s1", _("Hanako prepares to attend an open house day."), "hanako"),
            (_("Road Trip"), "sh_ch42.s2", _("Hanako and the others hit the road to Kasshoku."), "hanako"),
            (_("Kasshoku"), "sh_ch42.s3", _("Hanako checks out the journalism facility with Naomi."), "hanako"),
            (_("Time Out"), "sh_ch42.s4", _("Hanako has a quiet lunch with Naomi near the track field."), "hanako"),
            (_("Fate's Call"), "sh_ch42.s5", _("The open house day comes to a dramatic conclusion."), "hanako"),
            (_("Recriminations"), "sh_ch43.s1", _("Lilly, her father and Hisao discover what happened in the lecture hall."), "lilly"),
            (_("Hide and Seek"), "sh_ch43.s2", _("Lilly and the others set out to search for Hanako."), "lilly"),
            (_("Friend of a Friend"), "sh_ch43.s3", _("Lilly and Naomi talk about Hanako."), "lilly"),
            (_("Deliberation"), "sh_ch43.s4", _("Lilly and her father ponder on the day's events."), "lilly"),
            (_("Beyond Repair"), "sh_ch44.s1", _("An intimate moment between Hisao and Hanako ends on a sad note."), "hisao"),
            (_("Academic Anxiety"), "sh_ch44.s2", _("Hisao gets his results of the mock exams."), "hisao"),
            (_("Falling Behind"), "sh_ch44.s3", _("Hisao and Lilly visit Hanako in her room."), "hisao"),
            (_("Not Guilty!"), "sh_ch45.s1", _("Lilly has a brief talk about exam prep with Misha."), "lilly"),
            (_("The Stakes of the Game"), "sh_ch45.s2", _("Lilly and Hisao talk to Miss Takawa about Hanako."), "lilly"),
            (_("Christmas Cramming"), "sh_ch46.s1", _("Hisao and Hanako visit the Satous for Christmas... and more studying."), "hisao"),
            (_("Unwrapping the Present"), "sh_ch46.s2", _("Hisao's and Hanako's visit to the Satou residence ends with some unexpected gifts."), "hisao"),
            (_("Family Reunion"), "sh_ch47.s1", _("Akira answers her family's call for the New Year's celebrations."), "akira"),
            (_("The Fifth Wheel"), "sh_ch47.s2", _("The Satou family and Hanako visit a shrine for the New Year's celebration."), "akira"),
            (_("Grievances"), "sh_ch47.s3", _("Akira and her mother get into a harsh argument."), "akira"),
            (_("Black Sheep"), "sh_ch47.s4", _("Visiting the shrine again with Lilly and Hanako, Akira reflects on her relationship with her family."), "akira"),
        ])
    )

    sh_sprites("hanako", ["distant"], poses=["basic"], outfits=["cas_nohat"])
    sh_sprites("hanako", ["speechless", "shock", "worry"], poses=["def", "defarms"], outfits=["cas_nohat"])
    sh_sprites("hanako", ["downmeek", "downsad", "downsmile", "downtimid", "meek", "smile", "timid"], poses=["emb"], outfits=["cas_nohat"])
    sh_sprites("jun", ["confused", "disturbed", "sadclosed", "sheepish", "smileclosed"], poses=["basic"])
    sh_sprites("karla", ["confident", "pissed", "plead", "sad", "smileclosed", "wut"], poses=["basic", "cross"], outfits=["cas"])
    sh_sprites("lilly", ["displeased", "emb", "overjoyed"], poses=["basic", "cane"], outfits=["cas"])
    sh_sprites("hiroyuki", ["awkward", "smileclosed", "thinkraised"])
    sh_sprites("hisao", ["bashful", "emb", "smileclosed"], poses=["basic"], outfits=["bath", "polo", "uni"])
    sh_sprites("naomi", ["angry", "annoyed", "confused", "grinclosed", "concern", "seizure", "serious", "sheepish", "smileclosed"], poses=["basic"])
    sh_sprites("naomi", ["grinclosed"], poses=["bend"])
    sh_sprites("shizu", ["evil"], poses=["adjust"])
    sh_sprites("muto", ["eyebrow"])
    sh_sprites("hanako", ["downmeek", "downsleep", "meek"], poses=["emb"])
    sh_sprites("hanagown", ["distantmessy", "pleadmessy", "shockmessy", "worrymessy", "remorsefulmessy"])
    sh_sprites("misha", ["suspicious", "weaksmile"], poses=["perky"])
    sh_sprites("takawa", ["devious", "sweet", "weaksmile"])

    phonebox_sprites("akira", ["basic_smug", "basic_sweet"])
    phonebox_sprites("lilly", ["basic_cheerful_sum", "basic_smileclosed", "basic_smileclosed_sum", "basic_smile_sum", "basic_reminisce_sum", "basic_weaksmile", "basic_weaksmile_sum", "cane_satisfied", "cane_satisfied_sum", "cane_giggle", "cane_sleepy"], cropyoff=-40)
    phonebox_sprites("hisao", ["basic_neutral_uni", "basic_smile_uni", "basic_speak_uni", "basic_grin_swt", "basic_neutral_swt", "basic_smile_swt", "basic_sweet_swt"], cropxoff=95, cropyoff=-90)
    phonebox_sprites("naomi", ["basic_angry", "basic_annoyed", "basic_concern", "basic_serious"], xoff=-20, cropyoff=-45)
    phonebox_sprites("hiroyuki", ["speak", "serious", "thinking", "awkward", "scold", "smileclosed", "smile"], xoff=-22, cropxoff=130, cropyoff=-110, addwidth=14)

    sh_bgs("hisao", ["livingroom", "kitchen", "bedroom"])
    sh_bgs("city", ["karaokebooth"])
    sh_bgs("satou", ["masterbed_ni", "hiroyukicar"])
    # credit: japan-property.jp and SAKURA HOUSE CO., LTD.
    sh_bgs("satoujp", ["dining", "entryway", "ext", "guest", "livingroom", "stairs", "station"])
    # credit: Loyola University Maryland
    sh_bgs("school", ["dormkitchen", "dormnaomi"])
    # credit: japan-property.jp and Tokyo Furnished LLC
    sh_bgs("yuichi", ["intercom", "genkan", "dining"])
    # credit: OMOSHIRO RENT-A-CAR
    sh_bgs("misc", ["car_ss", "hiroyukicar", "hiroyukicar_ni"])
    sh_bgs("kasshoku", ["entrance", "entrance_ni", "grounds", "journalentry", "journalhall", "classroom", "bleachers", "lecturehall", "englishcafe", "grounds2_ni", "restroom"])
    sh_bgs("suburb", ["park_ni"])
    sh_bgs("school", ["teacherlounge"])
    sh_bgs("shrine", ["ema_ni", "entrance", "ext", "ext_ni", "int"])

    sh_event("bedside", ["headsets", "papers", "sit", "soup", "wine"])
    sh_event("sadspooning", ["tearoom"])

    sh_register_sfx([
        # credit: Universfield of Pixabay
        "winecork",
        "phonering3"
    ])

label sisterhood_timeskip_broken(silent=False):
    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    pause 2.0

    if not silent:
        play music music_timeskip

    show shlogo brokenquill at Transform(xalign=0.5, yalign=0.5)
    with CropMove(2.0, "wipedown")

    show shlogotext at Transform(xalign=0.5, yalign=0.5)
    with CropMove(2.0, "wiperight")

    pause 2.0

    if not silent:
        stop music fadeout 2.0

    scene black
    with erase

    pause 2.0

    return