label sisterhood_start:
    stop music fadeout 1.0
    
    scene black
    with config.game_main_transition
    pause 2.0

    call sisterhood_ch1
    call sisterhood_ch2
    call sisterhood_ch3
    call sisterhood_ch4
    call sisterhood_ch5
    call sisterhood_ch0
    call sisterhood_ch6
    call sisterhood_ch7
    call sisterhood_ch8
    call sisterhood_ch9
    call sisterhood_ch10
    call sisterhood_ch11
    call sisterhood_ch12
    call sisterhood_ch13
    call sisterhood_ch14
    call sisterhood_ch15
    call sisterhood_ch16
    call sisterhood_ch17
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
    $ config.allow_skipping = False

    stop music
    stop ambient

    scene black
    show credits mask
    with Dissolve(2.0)

    play music music_bloom noloop

    show sh_credits behind credits at Transform(xalign=0.5, yalign=0.0)
    with Dissolve(2.0)

    pause 1.0

    show sh_credits behind credits:
        xalign 0.5 yalign 0.0
        acdc20_warp 93 yalign 1.0
    
    pause 93

    hide sh_credits
    scene black
    with Dissolve(5.0)
    stop music

    $ config.allow_skipping = True

    return

label sisterhood_postcredits:

    $ config.skipping = False
    $ config.allow_skipping = False

    scene black
    show expression Text(_("To be continued..."), text_align=1.0, size=32) zorder 999 at Transform(xalign=0.92, yalign=0.92)
    with Dissolve(2.0)

    pause 5.0

    scene black
    with Dissolve(5.0)

    $ config.allow_skipping = True