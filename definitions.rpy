default persistent.sh_slowtransitions = True
default persistent.sh_windowtint = True
default persistent.sh_show_disclaimer = True

init python:
    sh_path = "mods/sisterhood"
    sh_bgs = sh_path + "/bgs"
    sh_window_tint = "#FFFFFF"

    def sh_sfx(name):
        return f"{sh_path}/sfx/{name}.ogg"

    def set_window_tint(tint_color):
        store.sh_window_tint = tint_color
    
    def tint_image(image):
        if not persistent.sh_windowtint:
            return image
        return Transform(image, matrixcolor=TintMatrix(TINT_HISAO if sh_window_tint is None else sh_window_tint))

    # renpy doesnt like lambas :(

    def _sh_get_nvl_bg(st, at):
        return (tint_image("gui/bg/nvl.png"), 1.0)

    def _sh_get_phonebox_bg(st, at):
        return (tint_image(f"{sh_path}/gui/phonebox.png"), 1.0)

init 1 python:
    for act in sisterhood_chapters:
        for chapter in act[1]:
            scene_names[chapter[1]] = __("[[Sisterhood] ") + __(chapter[0])
    _tracks[f"{sh_path}/bgm/Waltz_in_A_Minor.ogg"] = _("Waltz in A Minor")

init:
    $ mods["sisterhood"] = "Sisterhood"
    $ mods_with_menus["sisterhood"] = True

    # TODO SET TO FALSE BEFORE OFFICIAL RELEASE!!!
    define sh_debug = True

    define sisterhood_chapters = [
        (_("Act 1"), [
            (_("Chapter 1"), "sh_ch1.s1", _("Still in Scotland, Lilly and Akira discuss the future."), "lilly"),
            (_("Chapter 2"), "sh_ch2.s1", _("Hisao recounts his relationship with Hanako as he and Emi run on the track."), "hisao"),
            (_("Chapter 3"), "sh_ch3.s1", _("Hisao is introduced to an unusual member of Yamaku's staff."), "hisao"),
            (_("Chapter 4"), "sh_ch4.s1", _("Hisao and Hanako welcome the Satou sisters back to Japan."), "hisao"),
            (_("Chapter 4.1"), "sh_ch4.s2", _("Hisao and Hanako are invited to the Satou's summer home."), "hisao"),
            (_("Chapter 5"), "sh_ch5.s1", _("Hisao, Hanako, and Lilly take a trip to Hokkaido."), "hisao"),
            (_("Chapter 0"), "sh_ch0.s1", _("Hanako recounts a difficult conversation with Miss Yumi."), "hanako"),
            (_("Chapter 6"), "sh_ch6.s1", _("Hanako and Hisao spend the night in Hokkaido together."), "hanako"),
            (_("Chapter 7"), "sh_ch7.s1", _("Hanako becomes acquainted with her classroom neighbors."), "hanako"),
            (_("Chapter 7.1"), "sh_ch7.s2", _("Hanako deliberates working in the newspaper club."), "hanako"),
            (_("Chapter 7.2"), "sh_ch7.s3", _("Hanako helps with a favor from the newspaper club."), "hanako"),
            (_("Chapter 8"), "sh_ch8.s1", _("Hanako and Hisao go on a date at the local arcade."), "hanako"),
            (_("Chapter 9"), "sh_ch9.s1", _("Hanako and Hisao spend an intimate night in a hotel together."), "hanako"),
            (_("Chapter 10"), "sh_ch10.s1", _("Hisao and Hanako have trouble hiding their sex life."), "hisao"),
            (_("Chapter 10.1"), "sh_ch10.s2", _("Hisao and Hanako learn of Akira's leave and Lilly's summons."), "hisao"),
            (_("Chapter 11"), "sh_ch11.s1", _("Hanako and Lilly have a memorable night at a fancy restaurant."), "hanako"),
            (_("Chapter 12"), "sh_ch11.s1", _("Akira learns of Lilly's decision."), "lilly"),
            (_("Chapter 12.1"), "sh_ch12.s2", _("Lilly announces her leave to Hisao and Hanako."), "lilly"),
            (_("Chapter 13"), "sh_ch13.s1", _("Hanako is distracted by an airheaded Naomi."), "hanako"),
            (_("Chapter 13.1"), "sh_ch13.s2", _("Hanako and Hisao head to town to prepare for Lilly's going-away party."), "hanako"),
            (_("Chapter 14"), "sh_ch14.s1", _("Hisao wakes up to an unfamiliar yet familiar ceiling."), "hisao"),
            (_("Chapter 14.1"), "sh_ch14.s2", _("The student council and Lilly visit Hisao in the hospital."), "hisao"),
            (_("Chapter 15"), "sh_ch15.s1", _("Hisao makes an effort to reconcile with Hanako."), "hisao"),
            (_("Chapter 15.1"), "sh_ch15.s2", _("Hisao is discharged from the hospital."), "hisao"),
            (_("Chapter 16"), "sh_ch16.s1", _("Hanako meets Hisao on the rooftop of Yamaku."), "hanako"),
            (_("Chapter 16.1"), "sh_ch16.s2", _("Hisao takes Hanako to meet his parents."), "hanako"),
            (_("Chapter 17"), "sh_ch17.s1", _("Lilly plays an all-too-familiar game with the student council."), "lilly"),
            (_("Chapter 17.1"), "sh_ch17.s2", _("Lilly and Hanako reach out to each other."), "lilly"),
            (_("Chapter 17.2"), "sh_ch17.s3", _("Lilly and Hanako share a special connection with each other."), "lilly")
        ]),
        (_("Act 2"), [
            (_("Operation Distraction"), "sh_ch17alt.s1", _("Hisao keeps Kenji busy on the track."), "hisao"),
            (_("Convergence"), "sh_ch17alt.s2", _("Hisao reconvenes with Miss Takawa."), "hisao"),
            (_("A Second Sister"), "sh_ch18.s1", _("Akira expresses her gratitude to Hanako."), "hanako"),
            (_("Invitation"), "sh_ch18.s2", _("Hanako and Hisao receive a surprising offer from Lilly."), "hanako"),
            (_("Chapter 19.1"), "sh_ch19.s1", _("Hanako attends her first day of first aid training."), "hanako"),
            (_("Chapter 19.2"), "sh_ch19.s2", _("Hanako returns from her first day of first-aid training."), "hanako")
        ])
    ]

    # TRANSFORMS

    transform phonebox:
        xanchor 1.0 xpos 0.95 yanchor 1.0 ypos 0.81
    transform sittingpos:
        xpos 0.5 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform twoleft_sittingpos:
        xpos 0.3 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform tworight_sittingpos:
        xpos 0.7 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    define chchange = charachangealways if persistent.sh_slowtransitions else charachange
    define chchangefast = Dissolve(0.2) if persistent.sh_slowtransitions else charachangefast
    define nextchapter = Dissolve(2.0)
    define endchapter = Dissolve(3.0)
    define mediumflash = Fade(1, 0, 1, color="#FFF")

    define erase = ImageDissolve(f"{sh_path}/gui/trans/erase.png", 2.0)

    # TINT COLORS

    define TINT_HISAO = "#FFFFFF"
    define TINT_HANAKO = "#897CBF"
    define TINT_LILLY = "#fffc60"
    define TINT_AKIRA = "#c56060"
    define TINT_UNKNOWN = "#8d8d8d"

    # MISCELANEOUS

    define config.font_name_map["pixel"] = f"{sh_path}/font/Quinquefive-ALoRM.ttf"

init:
    init offset = 1

    define adv = ADVCharacter(kind=adv, screen="say_sh")
    define name_only = Character(kind=name_only, screen="say_sh")
    define narrator = Character(kind=narrator, screen="say_sh")
    define hi = Character(kind=hi, screen="say_sh")
    define ha = Character(kind=ha, screen="say_sh")
    define emi = Character(kind=emi, screen="say_sh")
    define li = Character(kind=li, screen="say_sh")
    define shi = Character(kind=shi, screen="say_sh")
    define mi = Character(kind=mi, screen="say_sh")
    define aki = Character(kind=aki, screen="say_sh")
    define no = Character(kind=no, screen="say_sh")
    define yu = Character(kind=yu, screen="say_sh")
    define mu = Character(kind=mu, screen="say_sh")
    define ke = Character(kind=ke, screen="say_sh")
    define mystery = Character(kind=mystery, screen="say_sh")
    define n = Character(kind=n, window_background=DynamicDisplayable(_sh_get_nvl_bg))

    define ta = Character(_("Takawa"), who_color="#f3ccff")
    define na = Character(_("Naomi"), who_color="#ad4545")
    define nt = Character(_("Natsume"), who_color="#a57d33")
    define ka = Character(_("Karla"), who_color="#dfc46d")
    define kam = Character(_("Mother"), kind=ka) # Karla ("Mother", from Lilly's POV)
    define nak = Character(_("Nakamura"), who_color="#c6ec87") # alt color: f3ccff
    define jun = Character(_("Jun"), who_color="#b37b7b")

    define dc = Character(_("Doctor"), who_color="#FFFFFF")

    # unknown characters
    define ta_ = Character(_("Old woman"), kind=ta)
    define nak_ = Character(_("Mid-thirties man"), kind=nak)