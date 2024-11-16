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

    return

label sisterhood_timeskip:
    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    pause 2.0

    play music music_timeskip

    show shlogo quill at Transform(xalign=0.5, yalign=0.5)
    with clockwipe

    scene black
    show shlogo title at Transform(xalign=0.5, yalign=0.5)
    with clockwipe

    pause 2.0

    stop music fadeout 2.0

    scene black
    with clockwipe

    pause 2.0

    return