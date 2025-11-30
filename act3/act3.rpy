init:
    init offset = 30

    define hid = Character(_("Dad"), who_color="#ffffff")
    define him = Character(_("Mom"), who_color="#ffffff")


init 30 python:
    sisterhood_chapters.append(
        (_("Act 3"), [
            (_("Chapter 35"), "sh_ch35.s1", _("???"))
        ])
    )

    sh_bgs("hisao", ["livingroom", "kitchen", "bedroom"])
