label sisterhood_replay_start:
    if sh_debug:
        $ _in_replay = True

    stop music fadeout 1.0

    $ renpy.transition(dissolve)
    call expression _current_replay

label sisterhood_start:
    stop music fadeout 1.0
    
    scene black
    with config.game_main_transition
    pause 2.0

    call sh_ch1
    call sh_ch2
    call sh_ch3
    call sh_ch4
    call sh_ch5
    call sh_ch0
    call sh_ch6
    call sh_ch7
    call sh_ch8
    call sh_ch9
    call sh_ch10
    call sh_ch11
    call sh_ch12
    call sh_ch13
    call sh_ch14
    call sh_ch15
    call sh_ch16
    call sh_ch17
    call sisterhood_credits
    call sisterhood_postcredits
    #call sisterhood_ch17alt

    return

label sisterhood_timeskip:
    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    pause 2.0

    play music music_timeskip

    show shlogo quill at Transform(xalign=0.5, yalign=0.5)
    with CropMove(2.0, "wipedown")

    show shlogo title at Transform(xalign=0.5, yalign=0.5)
    with CropMove(2.0, "wiperight")

    pause 2.0

    stop music fadeout 2.0

    scene black
    with erase

    pause 2.0

    return

label sisterhood_credits:
    $ config.skipping = False

    stop music
    stop ambient

    scene black
    show credits mask
    with Dissolve(2.0)

    play music music_bloom noloop

    show sh_credits behind credits at Transform(xalign=0.5, yalign=0.0)
    show sh_credits_overlay behind sh_credits
    with Dissolve(2.0)

    pause 1.0

    show sh_credits behind credits:
        xalign 0.5 yalign 0.0
        acdc20_warp 93.0 yalign 1.0
    
    pause 11.0

    show ev wheatfield_dreamy behind sh_credits_overlay:
        subpixel True pos (-618, 285)
        linear 10.0 pos (-775, 126)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev funindark_hug_rest behind sh_credits_overlay:
        subpixel True pos (64, 298)
        linear 10.0 pos (-222, 147)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev hotel_layontop behind sh_credits_overlay:
        subpixel True pos (-195, 94)
        linear 10.0 pos (-394, 230)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev ballroomdance_smile_normal behind sh_credits_overlay:
        subpixel True pos (-438, 289)
        linear 10.0 pos (-260, 241)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev rainyroad behind sh_credits_overlay:
        subpixel True pos (-317, 286)
        linear 10.0 pos (-317, 111)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev rooftopkiss_normal behind sh_credits_overlay:
        subpixel True pos (-260, 263)
        linear 10.0 pos (-445, 193)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev caress_normal behind sh_credits_overlay:
        subpixel True pos (-527, 262)
        linear 10.0 pos (-349, 193)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    pause 12.0

    hide sh_credits
    scene black
    with Dissolve(5.0)
    stop music

    return

label sisterhood_postcredits:

    $ config.skipping = False

    scene black
    show expression Text(_("To be continued..."), text_align=1.0, size=32) zorder 999 at Transform(xalign=0.92, yalign=0.92)
    with Dissolve(2.0)

    pause 5.0

    scene black
    with Dissolve(5.0)
