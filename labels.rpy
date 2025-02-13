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
    
    pause 10.0

    show ev wheatfield_dreamy behind sh_credits_overlay:
        subpixel True pos (64, 294) xysize (866, 493) crop (617, 0, 758, 426)
        linear 10.0 crop (1120, 246, 758, 426)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev funindark_hug_rest_large behind sh_credits_overlay:
        subpixel True pos (64, 294) xysize (866, 493) crop (0, 159, 2013, 1131)
        linear 10.0 crop (1024, 546, 2013, 1131)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev hotel_onhisao_large behind sh_credits_overlay:
        subpixel True pos (64, 294) xysize (866, 493) crop (0, 826, 1493, 840)
        linear 10.0 crop (430, 826, 1493, 840)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev ballroomdance_smile_large behind sh_credits_overlay:
        subpixel True pos (64, 294) xysize (866, 493) crop (1869, 198, 1326, 745)
        linear 10.0 crop (1263, 444, 1326, 745)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev rainyroad behind sh_credits_overlay:
        subpixel True pos (64, 294) xysize (866, 493) crop (353, 0, 866, 493)
        linear 10.0 crop (353, 294, 866, 493)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    # TODO replace with rooftop CG
    show ev rainyroad behind sh_credits_overlay:
        subpixel True pos (64, 294) xysize (866, 493) crop (353, 0, 866, 493)
        linear 10.0 crop (353, 294, 866, 493)
    with Dissolve(3.0)

    pause 4.0

    hide ev
    with Dissolve(3.0)

    show ev caress_large behind sh_credits_overlay:
        subpixel True pos (64, 294) xysize (866, 493) crop (2520, 740, 2821, 1587)
        linear 12.0 crop (1886, 383, 4089, 2301)
    with Dissolve(3.0)

    pause 6.0

    hide ev
    with Dissolve(3.0)

    pause 11.0

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
