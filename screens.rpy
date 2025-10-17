init python:
    def sh_should_show_disclaimer():
        return persistent.sh_show_disclaimer and not renpy.seen_label("a4_hanako.adulthood")

    def sh_update_sprite_transitions():
        if persistent.sh_slowtransitions:
            store.chchange = store.charachangealways
            store.chchangefast = Dissolve(0.2)
        else:
            store.chchange = store.charachange
            store.chchangefast = store.charachangefast

screen sisterhood():
    tag menu
    style_prefix "pxt"
    if main_menu:
        add "main_menu_bg"
    add "blind"

    frame:
        style_suffix "interface"
        has vbox

        text _("Mods > Sisterhood"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:
                textbutton _("Start") action If(main_menu, true=If(sh_should_show_disclaimer(), true=ShowMenu("sisterhood_disclaimer"), false=Start("sisterhood_start")), false=None)

            vbox:
                textbutton _("Options") action ShowMenu("sisterhood_options")

            vbox:
                textbutton _("About") action ShowMenu("sisterhood_about")

            vbox:
                textbutton _("Chapter Select") action If(main_menu, true=ShowMenu("sisterhood_chapter_select"), false=None)
            
            vbox:
                textbutton _("Credits") action If(main_menu, true=Start("sisterhood_credits"), false=None)
        
        textbutton _("Return"):
            style "return_button"
            action ShowMenu("mods")

    key "game_menu" action ShowMenu("mods")

screen sisterhood_disclaimer():
    tag menu
    style_prefix "pxt"
    if main_menu:
        add "main_menu_bg"
    add "blind"

    frame:
        style_suffix "interface"
        xsize 1200
        has vbox

        text _("{b}Attention!{/b}\n\nSisterhood is meant to be experienced after reading through Hanako's good ending. Do you wish to proceed?\n")

        frame:
            xalign 0.5
            has hbox

            textbutton _("No") action ShowMenu("sisterhood"):
                right_padding 36

            textbutton _("Yes") action [
                SetVariable("persistent.sh_show_disclaimer", False),
                Start("sisterhood_start")
            ]

screen sisterhood_options():
    tag menu
    style_prefix "prefs"
    if main_menu:    
        add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)

        has vbox

        spacing 6

        text _("Mods > Sisterhood > Options"):
            bold True
            size bold_size

        frame:
            left_margin 8
            size_group "prefs"

            has vbox

            spacing 6

            vbox:
                style_prefix "check"

                textbutton _("Slow sprite transitions") action [
                    ToggleVariable("persistent.sh_slowtransitions", True, False),
                    Function(sh_update_sprite_transitions)
                ]
            
            vbox:
                style_prefix "check"

                textbutton _("Tinted textboxes") action ToggleVariable("persistent.sh_windowtint", True, False)
            
        textbutton _("Return"):
            style "return_button"

            top_margin 20

            action ShowMenu("sisterhood")

    key "game_menu" action ShowMenu("sisterhood")


screen sisterhood_chapter_select(page=0):
    tag menu
    style_prefix "library"
    add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    default current_desc = None

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)
        has vbox

        text _("Mods > Sisterhood > Chapter Select"):
            bold True
            size bold_size

        null height 8

        frame:
            has hbox
            spacing 40

            for i, act in enumerate(sisterhood_chapters):
                textbutton act[0]:
                    if page == i:
                        text_insensitive_color "#000"
                    else:
                        action ShowMenu("sisterhood_chapter_select", i)
        
        null height 5

        frame:
            left_margin 8
            has hbox

            viewport id "sisterhood_chapter_select_" + str(page):
                mousewheel True
                draggable True
                xysize 705, 500

                vbox:
                    for chapter in sisterhood_chapters[page][1]:
                        if renpy.seen_label(chapter[1]) or sh_debug:
                            textbutton chapter[0]:
                                left_margin 30
                                action [
                                    SetVariable("_current_replay", chapter[1]),
                                    SetVariable("current_scene", chapter[1]),
                                    Start("sisterhood_replay_start")
                                ]
                                hovered SetScreenVariable("current_desc", chapter[2])
                                unhovered SetScreenVariable("current_desc", None)
                        else:
                            textbutton _("???") action None:
                                left_margin 30

            null width 25

            vbar value YScrollValue("sisterhood_chapter_select_" + str(page)) style "vslider"

        null height 16

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("sisterhood")

    if current_desc:
        text current_desc:
            color "#fff"
            size 36
            xalign 0.5
            yalign 1.0

    key "game_menu" action ShowMenu("sisterhood")

screen sisterhood_about():
    tag menu
    style_prefix "pxt_about"
    if main_menu:
        add "main_menu_bg"
    add "blind"

    frame:
        style_suffix "interface"
        xsize 1200

        has vbox

        text _("Mods > Sisterhood > About"):
            bold True
            size bold_size
        
        frame:
            has vbox

            vbox:
                text _("The first act of a visual novel adaptation of Guest Poster's fan fiction, featuring custom artwork and music.\n")
                text _("Version: 2.0-dev\n")
                text _("To learn about future updates or submit a bug report, check out the website:")
                textbutton _("https://sisterhood.whizvox.me") action OpenURL("https://sisterhood.whizvox.me"):
                    style "gui_exturl"
        
        textbutton _("Return"):
            style "return_button"
            action ShowMenu("sisterhood")

    key "game_menu" action ShowMenu("sisterhood")

screen say_sh(who, what):
    style_prefix "say"

    vbox:
        style_suffix "vbox"

        if who and who.strip():
            window id "namebox":
                at colorblind(persistent.colorblind)
                background tint_image(Frame("gui/bg/namebox.png"))
                style_suffix "namebox"
                text who id "who"
        else:
            null height 145

        window id "window":
            background tint_image(Frame("gui/bg/saybox.png"))
            text what id "what"

screen sh_doublespeak(c1, t1, c2, t2):
    style_prefix "doublespeak"

    frame id "namebox1":
        at colorblind(persistent.colorblind)
        background tint_image(Frame("gui/bg/namebox.png"))
        style_suffix "namebox1"
        text ("{color=" + c1.who_args["color"] + "}" + renpy.translate_string(c1.name) + "{/color}") id "who1":
            size 40
            bold True

    frame id "window1":
        at colorblind(persistent.colorblind)
        background tint_image(Frame("gui/bg/saybox.png"))
        style_suffix "window1"
        text t1 id "what1"

    frame id "namebox2":
        at colorblind(persistent.colorblind)
        background tint_image(Frame("gui/bg/namebox.png"))
        style_suffix "namebox2"
        text ("{color=" + c2.who_args["color"] + "}" + renpy.translate_string(c2.name) + "{/color}") id "who2":
            size 40
            bold True

    frame id "window2":
        at colorblind(persistent.colorblind)
        background tint_image(Frame("gui/bg/saybox.png"))
        style_suffix "window2"
        text t2 id "what2"

    image "icon_ctc" as ctc1:
        xpos 0.473
    image "icon_ctc" as ctc2:
        xpos 0.974

    key ["dismiss", "skip"] action Return()

    on "show" action If(renpy.is_skipping(), Return())

screen sh_journal(left_dialogue, right_dialogue=None, images=None):
    style_prefix "shdiary"

    window id "window":
        at colorblind(persistent.colorblind)

        frame:
            text left_dialogue id "diary_left"

        if right_dialogue is not None:
            frame:
                xpos 0.57
                text right_dialogue id "diary_right"

    if images is not None:
        for entry in images:
            image entry[0]:
                xpos entry[1] ypos entry[2]

    #use ctc

    key ["dismiss", "skip"] action Return()

    on "show" action If(renpy.is_skipping(), Return(), Play("sound", "sfx/paper.ogg"))
