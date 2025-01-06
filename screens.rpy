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

init python:
    def sh_update_sprite_transitions():
        if persistent.sh_slowtransitions:
            store.chchange = store.charachangealways
            store.chchangefast = Dissolve(0.2)
        else:
            store.chchange = store.charachange
            store.chchangefast = store.charachangefast

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
            
        textbutton _("Return"):
            style "return_button"

            top_margin 20

            action ShowMenu("sisterhood")
    

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

        text _("Mods > Sisterhood > Chapter Select"):
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
                        if renpy.seen_label(chapter[1]) or sh_debug:
                            textbutton chapter[0]:
                                left_margin 30
                                action If(sh_debug, true=[
                                    SetVariable("current_scene", chapter[1]),
                                    Start(chapter[1])
                                ], false=[
                                    SetVariable("_current_replay", chapter[1]),
                                    SetVariable("current_scene", chapter[1]),
                                    Start("replay_start")
                                ])
                                hovered SetScreenVariable("current_desc", chapter[2])
                                unhovered SetScreenVariable("current_desc", None)
                        else:
                            textbutton _("???") action None:
                                left_margin 30
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
                text _("A visual novel adaptation of Guest Poster's fan fiction, featuring custom artwork and music.\n")
                text _("Version: 0.1\n")
                text _("To learn about future updates or submit a bug report, check out the website:")
                textbutton _("https://whizvox.me/sisterhood") action OpenURL("https://whizvox.me/sisterhood"):
                    style "gui_exturl"
        
        textbutton _("Return"):
            style "return_button"
            action ShowMenu("sisterhood")
