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
    for chapter in sisterhood_chapters:
        scene_names[chapter[1]] = __("[[Sisterhood] ") + __(chapter[0])
    _tracks[f"{sh_path}/bgm/Waltz_in_A_Minor.ogg"] = _("Waltz in A Minor")

init:
    $ mods["sisterhood"] = "Sisterhood"
    $ mods_with_menus["sisterhood"] = True

    # TODO SET TO FALSE BEFORE OFFICIAL RELEASE!!!
    define sh_debug = False

    define sisterhood_chapters = [
        (_("Chapter 1"), "sisterhood_ch1.sh_ch1", _("Still in Scotland, Lilly and Akira discuss the future."), "lilly"),
        (_("Chapter 2"), "sisterhood_ch2.sh_ch2", _("Hisao recounts his relationship with Hanako as he and Emi run on the track."), "hisao"),
        (_("Chapter 3"), "sisterhood_ch3.sh_ch3", _("Hisao is introduced to an unusual member of Yamaku's staff."), "hisao"),
        (_("Chapter 4"), "sisterhood_ch4.sh_ch4", _("Hisao and Hanako welcome Lilly and Akira back to Japan."), "hisao"),
        (_("Chapter 5"), "sisterhood_ch5.sh_ch5", _("Hisao, Hanako, and Lilly take a trip to Hokkaido."), "hisao"),
        (_("Chapter 0"), "sisterhood_ch0.sh_ch0", _("Hanako recounts a difficult conversation with Miss Yumi."), "hanako"),
        (_("Chapter 6"), "sisterhood_ch6.sh_ch6", _("Hanako and Hisao spend the night in Hokkaido together."), "hanako"),
        (_("Chapter 7"), "sisterhood_ch7.sh_ch7", _("Hanako helps with a favor from the newspaper club."), "hanako"),
        (_("Chapter 8"), "sisterhood_ch8.sh_ch8", _("Hanako and Hisao go on a date at the local arcade."), "hanako"),
        (_("Chapter 9"), "sisterhood_ch9.sh_ch9", _("Hanako and Hisao spend an intimate night in a hotel together."), "hanako"),
        (_("Chapter 10"), "sisterhood_ch10.sh_ch10", _("Hisao and Hanako learn of Akira's leave and Lilly's summons."), "hisao"),
        (_("Chapter 11"), "sisterhood_ch11.sh_ch11", _("Hanako and Lilly have a memorable night at a fancy restaurant."), "hanako"),
        (_("Chapter 12"), "sisterhood_ch12.sh_ch12", _("Lilly makes a difficult decision."), "lilly"),
        (_("Chapter 13"), "sisterhood_ch13.sh_ch13", _("Hanako and Hisao make preparations for Lilly's going-away party."), "hanako"),
        (_("Chapter 14"), "sisterhood_ch14.sh_ch14", _("Hisao wakes up to an unfamiliar yet familiar ceiling."), "hisao"),
        (_("Chapter 15"), "sisterhood_ch15.sh_ch15", _("Hisao makes an effort to reconcile with Hanako."), "hisao"),
        (_("Chapter 16"), "sisterhood_ch16.sh_ch16", _("Hanako meets Hisao on the rooftop of Yamaku."), "hanako"),
        (_("Chapter 17"), "sisterhood_ch17.sh_ch17", _("Lilly and Hanako reach out to each other."), "lilly"),
        #(_("Chapter 17 Alt"), "sisterhood_ch17alt.sh_ch17alt", _("Hisao keeps Kenji busy before talking to Miss Takawa."), "hisao")
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
    define mystery = Character(kind=mystery, screen="say_sh")
    define n = Character(kind=n, window_background=DynamicDisplayable(_sh_get_nvl_bg))

    define ta = Character(_("Takawa"), who_color="#f3ccff")
    define na = Character(_("Naomi"), who_color="#ad4545")
    define nt = Character(_("Natsume"), who_color="#a57d33")
    define ka = Character(_("Karla"), who_color="#dfc46d")

    define schar = Character(who_color="#FFFFFF") # small-role character, given white character name
    define re = Character(_("Receptionist"), kind=schar)
    define om = Character(_("Old Man"), kind=schar)
    define dc = Character(_("Doctor"), kind=schar)
    define mom = Character(_("Mom"), kind=schar)
    define dad = Character(_("Dad"), kind=schar)
    define kam = Character(_("Mother"), kind=ka) # Karla ("Mother", from Lilly's POV)

    define nchar = Character(kind=n, who_suffix=" ", what_prefix=_("“"), what_suffix=_("”"), screen="nvl_sh") # NVL character
    define nhi = Character(_("Hisao"), kind=nchar, who_color="#629276")
    define nha = Character(_("Hanako"), kind=nchar, who_color="#897CBF")

    # unknown characters
    define ta_ = Character(_("Old woman"), who_color="#f3ccff")