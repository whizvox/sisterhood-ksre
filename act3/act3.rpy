init:
    init offset = 30

    define hid = Character(_("Dad"), who_color="#ffffff", screen="say_sh")
    define him = Character(_("Mom"), who_color="#ffffff", screen="say_sh")


init 30 python:
    sisterhood_chapters.append(
        (_("Act 3"), [
            (_("Chapter 35"), "sh_ch35.s1", _("Hanako wakes up in Hisao's living room and catches up with Lilly.")),
            (_("Chapter 35.2"), "sh_ch35.s2", _("???"))
        ])
    )

    sh_sprites("hisao", ["bashful", "emb"], poses=["basic"], outfits=["bath"])

    phonebox_sprites("lilly", ["basic_smileclosed", "basic_weaksmile", "cane_satisfied", "cane_giggle", "cane_sleepy"], cropyoff=-40)

    sh_bgs("hisao", ["livingroom", "kitchen", "bedroom"])
