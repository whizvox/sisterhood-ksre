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
                textbutton _("Start") action If(main_menu, true=Start("sisterhood_start"), false=None)
            
            vbox:
                textbutton _("Chapter Select") action If(main_menu, true=ShowMenu("sisterhood_chapter_select"), false=None)

            vbox:
                textbutton _("About") action ShowMenu("sisterhood_about")
            
            vbox:
                textbutton _("Credits") action If(main_menu, true=Start("sisterhood_credits"), false=None)
        
        textbutton _("Return"):
            style "return_button"
            action ShowMenu("mods")

screen sisterhood_chapter_select():
    tag menu
    style_prefix "library"
    add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    default current_desc = None

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)
        has vbox

        text _("Sisterhood > Chapter Select"):
            bold True
            size bold_size

        null height 8

        frame:
            left_margin 8
            has hbox

            viewport id "sisterhood_chapter_select":
                mousewheel True
                draggable True
                xysize 705, 500

                vbox:
                    for chapter in sisterhood_chapters:
                        textbutton chapter[0]:
                            left_margin 30
                            # TODO SWAP THIS IN RELEASE. Ren'Py disables reloading in replays.
                            # action [
                            #     SetVariable("_current_replay", chapter[1]),
                            #     SetVariable("current_scene", chapter[1]),
                            #     Start("replay_start")
                            # ]
                            action [
                                SetVariable("current_scene", chapter[1]),
                                Start(chapter[1])
                            ]
                            hovered SetScreenVariable("current_desc", chapter[2])
                            unhovered SetScreenVariable("current_desc", None)
            null width 25
            vbar value YScrollValue("sisterhood_chapter_select") style "vslider"
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
                text _("A port of Guest Poster's famous fan fiction.")
                text _("Ported by whizvox")
        
        textbutton _("Return"):
            style "return_button"
            action ShowMenu("sisterhood")
