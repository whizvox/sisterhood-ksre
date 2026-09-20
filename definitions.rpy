default persistent.sh_slowtransitions = True
default persistent.sh_windowtint = True
default persistent.sh_show_disclaimer = True
default persistent.sh_unlocked_acts = []

define config.default_textshader = "typewriter"

init python:
    sh_path = "mods/sisterhood"
    sh_window_tint = "#FFFFFF"

    def sh_sfx(name):
        return f"{sh_path}/sfx/{name}.ogg"

    def set_window_tint(tint_color):
        store.sh_window_tint = tint_color

    def tint_image(image):
        if not persistent.sh_windowtint:
            return image
        return Transform(image, matrixcolor=TintMatrix(TINT_HISAO if sh_window_tint is None else sh_window_tint))

    def sh_update_sprite_transitions():
        if persistent.sh_slowtransitions:
            store.chchange = store.charachangealways
            store.chchangefast = Dissolve(0.2)
        else:
            store.chchange = persistent.charachange
            store.chchangefast = persistent.charachangefast
    
    def sh_slowtype_tag(tag, argument, contents):
        if argument is None or argument == "":
            min_speed = 20
        else:
            min_speed = int(argument)
        speed = min(preferences.text_cps, min_speed)
        return [(renpy.TEXT_TAG, u"cps={}".format(speed))] + contents + [(renpy.TEXT_TAG, u"/cps")]

    config.custom_text_tags["slowtype"] = sh_slowtype_tag

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

    sh_update_sprite_transitions()

init:
    $ mods["sisterhood"] = "Sisterhood"
    $ mods_with_menus["sisterhood"] = True

    # TODO SET TO FALSE BEFORE OFFICIAL RELEASE!!!
    define sh_debug = True

    define sisterhood_chapters = [
        (_("Act 1"), [
            (_("Skipping Stones"), "sh_ch1.s1", _("Still in Scotland, Lilly and Akira discuss the future."), _("Chapter 1"), "lilly"),
            (_("Man's Oldest Motivation"), "sh_ch2.s1", _("Hisao recounts his relationship with Hanako as he and Emi run on the track."), _("Chapter 2"), "hisao"),
            (_("The Shrink in Violet"), "sh_ch3.s1", _("Hisao is introduced to an unusual member of Yamaku's staff."), _("Chapter 3"), "hisao"),
            (_("Homecoming"), "sh_ch4.s1", _("Hisao and Hanako welcome the Satou sisters back to Japan."), _("Chapter 4 p.1"), "hisao"),
            (_("Flower Girl"), "sh_ch4.s2", _("Hisao and Hanako are invited to the Satou's summer home."), _("Chapter 4 p.2"), "hisao"),
            (_("Swirling Fireflies"), "sh_ch5.s1", _("Hisao, Hanako, and Lilly take a trip to Hokkaido."), _("Chapter 5"), "hisao"),
            (_("Look Back"), "sh_ch0.s1", _("Hanako recounts a difficult conversation with Miss Yumi."), _("Chapter 0"), "hanako"),
            (_("Fun in the Dark"), "sh_ch6.s1", _("Hanako and Hisao spend the night in Hokkaido together."), _("Chapter 6"), "hanako"),
            (_("Pushing Boundaries"), "sh_ch7.s1", _("Hanako becomes acquainted with her classroom neighbors."), _("Chapter 7 p.1"), "hanako"),
            (_("Editorial Control"), "sh_ch7.s2", _("Hanako deliberates working in the newspaper club."), _("Chapter 7 p.2"), "hanako"),
            (_("Breaking the News"), "sh_ch7.s3", _("Hanako helps with a favor from the newspaper club."), _("Chapter 7 p.3"), "hanako"),
            (_("Bits and Bites"), "sh_ch8.s1", _("Hanako and Hisao go on a date at the local arcade."), _("Chapter 8"), "hanako"),
            (_("Nori"), "sh_ch9.s1", _("Hanako and Hisao spend an intimate night in a hotel together."), _("Chapter 9"), "hanako"),
            (_("Under the Collar"), "sh_ch10.s1", _("Hisao and Hanako have trouble hiding their sex life."), _("Chapter 10 p.1"), "hisao"),
            (_("Indecisiveness"), "sh_ch10.s2", _("Hisao and Hanako learn of Akira's leave and Lilly's summons."), _("Chapter 10 p.2"), "hisao"),
            (_("A Step Forward and Natural Turn"), "sh_ch11.s1", _("Hanako and Lilly have a memorable night at a fancy restaurant."), _("Chapter 11"), "hanako"),
            (_("Cutting the Knot"), "sh_ch12.s1", _("Akira learns of Lilly's decision."), _("Chapter 12 p.1"), "lilly"),
            (_("Branching Paths"), "sh_ch12.s2", _("Lilly announces her leave to Hisao and Hanako."), _("Chapter 12 p.2"), "lilly"),
            (_("Overcast"), "sh_ch13.s1", _("Hanako is distracted by an airheaded Naomi."), _("Chapter 13 p.1"), "hanako"),
            (_("Downpour"), "sh_ch13.s2", _("Hanako and Hisao head to town to prepare for Lilly's going-away party."), _("Chapter 13 p.2"), "hanako"),
            (_("An (Un)Familiar Ceiling"), "sh_ch14.s1", _("Hisao wakes up to an unfamiliar yet familiar ceiling."), _("Chapter 14 p.1"), "hisao"),
            (_("Fallout"), "sh_ch14.s2", _("The student council and Lilly visit Hisao in the hospital."), _("Chapter 14 p.2"), "hisao"),
            (_("Relationship Therapy"), "sh_ch15.s1", _("Hisao makes an effort to reconcile with Hanako."), _("Chapter 15 p.1"), "hisao"),
            (_("On the Mend"), "sh_ch15.s2", _("Hisao is discharged from the hospital."), _("Chapter 15 p.2"), "hisao"),
            (_("Rooftop Lilies"), "sh_ch16.s1", _("Hanako meets Hisao on the rooftop of Yamaku."), _("Chapter 16 p.1"), "hanako"),
            (_("A Proper Introduction"), "sh_ch16.s2", _("Hisao takes Hanako to meet his parents."), _("Chapter 16 p.2"), "hanako"),
            (_("Thicker than Water"), "sh_ch17.s1", _("Lilly plays an all-too-familiar game with the student council."), _("Chapter 17 p.1"), "lilly"),
            (_("In All but Blood"), "sh_ch17.s2", _("Lilly and Hanako reach out to each other."), _("Chapter 17 p.2"), "lilly"),
            (_("All of Me"), "sh_ch17.s3", _("Lilly and Hanako share a special connection with each other."), _("Chapter 17 p.3"), "lilly")
        ]),
        (_("Act 2"), [
            (_("Operation Distraction"), "sh_ch17alt.s1", _("Hisao keeps Kenji busy on the track."), _("Chapter 17 Alt p.1"), "hisao"),
            (_("Convergence"), "sh_ch17alt.s2", _("Hisao reconvenes with Miss Takawa."), _("Chapter 17 Alt p.2"), "hisao"),
            (_("A Second Sister"), "sh_ch18.s1", _("Akira expresses her gratitude to Hanako."), _("Chapter 18 p.1"), "hanako"),
            (_("Invitation"), "sh_ch18.s2", _("Hanako and Hisao receive a surprising offer from Lilly."), _("Chapter 18 p.2"), "hanako"),
            (_("Too Close to Home"), "sh_ch19.s1", _("Hanako attends her first day of first aid training."), _("Chapter 19 p.1"), "hanako"),
            (_("Not So Easily Broken"), "sh_ch19.s2", _("Hanako returns from her first day of first-aid training."), _("Chapter 19 p.2"), "hanako"),
            (_("Passing Marks"), "sh_ch20.s1", _("Hanako's first-aid training comes to a startling close."), _("Chapter 20 p.1"), "hanako"),
            (_("A True Scotsman"), "sh_ch20.s2", _("Hanako receives a gift from the newspaper club."), _("Chapter 20 p.2"), "hanako"),
            (_("Oxytocin Therapy"), "sh_ch20.s3", _("Hanako and Hisao prepare for the long day tomorrow."), _("Chapter 20 p.3"), "hanako"),
            (_("Airport Blues"), "sh_ch21.s1", _("Hisao and Hanako get a taste of intercontinental travel."), _("Chapter 21 p.1"), "hisao"),
            (_("Roaring Engines"), "sh_ch21.s2", _("Hisao, Hanako, and Lilly take off."), _("Chapter 21 p.2"), "hisao"),
            (_("Mile High"), "sh_ch21.s3", _("Hisao catches Lilly having an intimate moment with a sleeping Hanako."), _("Chapter 21 p.3"), "hisao"),
            (_("Welcome to Inverness!"), "sh_ch21.s4", _("The trio arrive in Inverness airport."), _("Chapter 21 p.4"), "hisao"),
            (_("Guid eenin!"), "sh_ch22.s1", _("Hisao and Hanako prepare to head to dinner."), _("Chapter 22 p.1"), "hisao"),
            (_("Settling In"), "sh_ch22.s2", _("Lilly persuades Hanako and Hisao into the true Inverness experience."), _("Chapter 22 p.2"), "hisao"),
            (_("No Stripes Here"), "sh_ch23.s1", _("The Satou sisters are quizzed, Hisao and Hanako are competitive, and a special guest is introduced."), _("Chapter 23"), "hisao"),
            (_("In Vino Veritas"), "sh_ch24.s1", _("Lilly puts on a performance and the lovebirds succumb to the wine."), _("Chapter 24"), "hisao"),
            (_("Wicked Awakening"), "sh_ch25.s1", _("Hisao, Hanako, and Lilly have a less-than-pleasant waking up."), _("Chapter 25 p.1"), "hisao"),
            (_("No Rest for the Weary"), "sh_ch25.s2", _("Hanako and Lilly prepare for the upcoming picnic."), _("Chapter 25 p.2"), "hisao"),
            (_("In Tandem"), "sh_ch26.s1", _("The awkward lovebirds and Satous ride through the Scottish countryside."), _("Chapter 26"), "hisao"),
            (_("Model Maid"), "sh_ch27.s1", _("Hanako has a brief encounter with Mr. Satou."), _("Chapter 27"), "hanako"),
            (_("Journalistic Habits"), "sh_ch28.s1", _("Hanako reads from her diary at the shore of Moray Firth."), _("Chapter 28"), "hanako"),
            (_("Soap Opera"), "sh_ch29.s1", _("Hanako and Hisao take a very intimate bath."), _("Chapter 29 p.1"), "hanako"),
            (_("Shared Soak"), "sh_ch29.s2", _("Hanako and Hisao talk about their trip to Inverness."), _("Chapter 29 p.2"), "hanako"),
            (_("Evening Snack"), "sh_ch29.s3", _("Hanako and Hisao round off the night with an “evening snack”."), _("Chapter 29 p.3"), "hanako"),
            (_("Oh, the Days Ahead"), "sh_ch30.s1", _("Lilly, Hanako, and Hisao spend a peaceful evening planning the second half of their trip."), _("Chapter 30 p.1"), "lilly"),
            (_("Without Thinking"), "sh_ch30.s2", _("Lilly's worst fears are realized."), _("Chapter 30 p.2"), "lilly"),
            (_("Prayer"), "sh_ch30.s3", _("Lilly reconvenes with Akira and Hisao at the hospital."), _("Chapter 30 p.3"), "lilly"),
            (_("Playing Politics"), "sh_ch31.s1", _("Akira discusses her parents with the company's vice president."), _("Chapter 31 p.1"), "akira"),
            (_("Revelation"), "sh_ch31.s2", _("Akira and Lilly learn of their father's current and past health concerns."), _("Chapter 31 p.2"), "akira"),
            (_("Dirty Laundry"), "sh_ch31.s3", _("Akira and Lilly visit their father in the hospital."), _("Chapter 31 p.3"), "akira"),
            (_("Delivery"), "sh_ch32.s1", _("Hanako and Hisao join Akira to visit Mister Satou in the hospital."), _("Chapter 32 p.1"), "hanako"),
            (_("Poking the Bear"), "sh_ch32.s2", _("Hanako and Hisao listen in on Akira and Mister Satou."), _("Chapter 32 p.2"), "hanako"),
            (_("Looking Out for Each Other"), "sh_ch32.s3", _("Hanako opens up to Mister Satou about her and Lilly's relationship."), _("Chapter 32 p.3"), "hanako"),
            (_("Rock Skipping Again"), "sh_ch33.s1", _("Hanako and Akira open up to each other."), _("Chapter 33"), "hanako"),
            (_("Present and Past"), "sh_ch34.s1", _("Hanako and Lilly have a heart-to-heart in the bath."), _("Chapter 34 p.1"), "hanako"),
            (_("Sendoff"), "sh_ch34.s2", _("Hanako and Hisao head back home."), _("Chapter 34 p.2"), "hanako")
        ])
    ]

    # TRANSFORMS

    transform phonebox:
        xanchor 1.0 xpos 0.95 yanchor 1.0 ypos 0.82
    transform centersit:
        xpos 0.5 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform twoleftsit:
        xpos 0.3 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform tworightsit:
        xpos 0.7 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform leftsit:
        xpos 0.0 xanchor 0.0 ypos 1.1 yanchor 1.0 alpha 1.0
    transform rightsit:
        xpos 1.0 xanchor 1.0 ypos 1.1 yanchor 1.0 alpha 1.0

    transform displayitemshow(ya=0.5):
        truecenter
        ypos ya+0.2 alpha 0.0
        easein 1.0 alpha 1.0 ypos ya
    transform displayitem(ya=0.5):
        truecenter
        alpha 1.0 ypos ya
    transform displayitemhide(ya=0.5):
        ease 1.0 ypos ya+0.2 alpha 0.0
    transform sepia:
        matrixcolor SepiaMatrix(tint="#ffefd7")
    transform sepiamuted:
        matrixcolor TintMatrix("#ffefd7") * SaturationMatrix(0.5)
    transform nightfilter:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.92, 1.0))) * BrightnessMatrix(-0.05)
    transform soapopera_talk:
        anchor (0.5, 0.5) pos (0.5, 0.85)

    define nextchapter = Dissolve(2.0)
    define endchapter = Dissolve(3.0)
    define mediumflash = Fade(1, 0, 1, color="#FFF")
    define longflash = Fade(1.5, 0, 1.5, color="#FFF")
    define easeinmove = MoveTransition(1.5, time_warp=_warper.easein)
    define easeoutmove = MoveTransition(1.5, time_warp=_warper.easeout)

    define erase = ImageDissolve(f"{sh_path}/gui/trans/erase.png", 2.0)

    # TINT COLORS

    define TINT_HISAO = "#FFFFFF"
    define TINT_HANAKO = "#897CBF"
    define TINT_LILLY = "#fffc60"
    define TINT_AKIRA = "#c56060"
    define TINT_UNKNOWN = "#8d8d8d"

    # FONTS

    define config.font_name_map["pixel"] = f"{sh_path}/font/Quinquefive-ALoRM.ttf"
    define config.font_name_map["times"] = f"{sh_path}/font/Newsreader-VariableFont_opsz,wght.ttf"

    if sh_debug:
        $ config.log = "sisterhood.log"

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

    define ta = Character(_("Takawa"), who_color="#f3ccff")
    define na = Character(_("Naomi"), who_color="#ad4545")
    define nt = Character(_("Natsume"), who_color="#a57d33")
    define ka = Character(_("Karla"), who_color="#dfc46d")
    define kam = Character(_("Mother"), kind=ka) # Karla ("Mother", from Lilly's POV)
    define kamo = Character(_("Mom"), kind=ka) # Karla ("Mom", from Akira's POV)
    define nak = Character(_("Nakamura"), who_color="#c6ec87") # alt color: f3ccff
    define jun = Character(_("Jun"), who_color="#b37b7b")
    define hy = Character(_("Hiroyuki"), who_color="#c9b09b")
    define hys = Character(_("Mr. Satou"), kind=hy)
    define hyf = Character("Father", kind=hy)
    define hyd = Character("Dad", kind=hy)
    define dc = Character(_("Doctor"), who_color="#ffffff")
    define fer = Character(_("Ferguson"), who_color="#ffffff")

    # unknown characters
    define ta_ = Character(_("Old woman"), kind=ta)
    define nak_ = Character(_("Mid-thirties man"), kind=nak)
    define ka_ = Character(_("Pub patron"), kind=ka)