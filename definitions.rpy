init python:

    ta = Character(_("Takawa"), who_color="#f3ccff")
    na = Character(_("Naomi"), who_color="#ad4545")
    nt = Character(_("Natsume"), who_color="#a57d33")
    ka = Character(_("Karla"), who_color="#dfc46d")

    schar = Character(who_color="#FFFFFF") # small-role character, given white character name
    re = Character(_("Receptionist"), kind=schar)
    om = Character(_("Old man"), kind=schar)
    dc = Character(_("Doctor"), kind=schar)
    mom = Character(_("Mom"), kind=schar)
    dad = Character(_("Dad"), kind=schar)
    kam = Character(_("Mother"), kind=ka) # Karla ("Mother", from Lilly's POV)

    nchar = Character(kind=n, who_suffix=" ", what_prefix=_("“"), what_suffix=_("”")) # NVL character
    nhi = Character(_("Hisao"), kind=nchar, who_color="#629276")
    nha = Character(_("Hanako"), kind=nchar, who_color="#897CBF")

    # unknown characters
    ta_ = Character(_("Old Woman"), who_color="#f3ccff")

    # preferences
    # 0 = skip, 1 = text w/ black cg, 2 = text w/ blurred cg, 3 = show all
    sh_r18_level = 3

    # for chapter in sisterhood_chapters:
    #     scene_labels[chapter[1]] = (__("[Sisterhood] ") + __(chapter[0]), chapter[1], __(chapter[2]))

    sh_path = "mods/sisterhood"
    sh_bgs = sh_path + "/bgs"

    def sh_sprites(char, variants):
        for variant in variants:
            imgpath = f"{sh_path}/sprites/{char}/{char}_{variant.replace(' ', '_')}.png"
            closeimgpath = f"{sh_path}/sprites/{char}/close/{char}_{variant.replace(' ', '_')}_close.png"
            if renpy.loadable(imgpath):
                renpy.image(char + " " + variant, imgpath)
                renpy.image(char + " " + variant + "_ss", sp_sunset(imgpath))
                renpy.image(char + " " + variant + "_ni", sp_night(imgpath))
                renpy.image(char + " " + variant + "_rn", sp_rain(imgpath))
            else:
                renpy.log("[SISTERHOOD] Could not load sprite: " + imgpath)
            if renpy.loadable(closeimgpath):
                renpy.image(char + " " + variant + "_close", closeimgpath)
                renpy.image(char + " " + variant + "_close_ss", sp_sunset(closeimgpath))
                renpy.image(char + " " + variant + "_close_ni", sp_night(closeimgpath))
                renpy.image(char + " " + variant + "_close_rn", sp_rain(closeimgpath))
            else:
                renpy.log("[SISTERHOOD] Could not load close-up sprite: " + closeimgpath)

    def phonebox_sprites(char, variants, vanilla=True, xoff=0, yoff=0, cropxoff=0, cropyoff=0):
        for variant in variants:
            imgpath = f"sprites/{char}/{char}_{variant.replace(' ', '_')}.png"
            if not vanilla:
                imgpath = f"{sh_path}/{imgpath}"
            renpy.image(char + " " + variant + "_phone", Composite(
                (436, 436),
                (0, 0), f"{sh_path}/gui/phonebox.png",
                (30 + xoff, 30 + yoff), Crop((20 + cropxoff, 107 + cropyoff, 405, 402), char + " " + variant)
            ))

    def sh_sfx(name):
        return sh_path + "/sfx/" + name + ".ogg"

    # def sh_event(name, variants):
    #     for variant in variants:
    #         imgpath = f"{sh_path}/event/{name}/{name}_{variant}.png"
    #         if renpy.loadable(imgpath):
    #             renpy.image("ev " + name + "_" + variant, imgpath)
    
    def sh_fireflies():
        for i in range(0, 15):
            imgpath = f"{sh_path}/vfx/fireflies/ff{i:02}.png"
            if renpy.loadable(imgpath):
                renpy.image(f"firefly b{i}", imgpath)
            else:
                renpy.log(f"[SISTERHOOD] Could not load firefly image: {imgpath}")
    
    def randpair():
        return (random.random(), random.random())
        
    
    # CHARACTERS
    
    sh_sprites("takawa", ["serious", "smile", "happy", "worried", "calculating", "stern"])
    sh_sprites("hanako", ["basic_bashful_clip", "basic_distant_clip"])
    sh_sprites("hisao", ["neutral", "smile", "grin"])
    sh_sprites("naomi", ["neutral", "smile", "laugh", "shock"])
    sh_sprites("natsume", ["neutral", "smile"])
    sh_sprites("mishashort", ["sign_sad_cas"])
    sh_sprites("lilly", ["cane_sad_close"])
    #sh_event("wheatfield", ["smile"])
    phonebox_sprites("akira", ["basic_smile", "basic_annoyed", "basic_resigned", "basic_laugh", "basic_lost", "basic_boo"])
    phonebox_sprites("hanagown", ["worry", "distant", "irritated", "normal"])
    phonebox_sprites("lilly", ["basic_smile", "basic_concerned", "basic_sad", "basic_displeased", "cane_oops", "basic_reminisce"], cropyoff=-40)
    sh_fireflies()

    persistent.sh_nsfwlevel = 0


init:
    $ mods["sisterhood"] = "Sisterhood"
    $ mods_with_menus["sisterhood"] = True

    define sisterhood_chapters = [
        (_("Chapter 1"), "sisterhood_ch1", _("Lilly and Akira discuss the future from Inverness."), "lilly"),
        (_("Chapter 2"), "sisterhood_ch2", _("Hisao recounts his relationship with Hanako as he and Emi run on the track."), "hisao"),
        (_("Chapter 3"), "sisterhood_ch3", _("Hisao is introduced to someone special by the nurse."), "hisao"),
        (_("Chapter 4"), "sisterhood_ch4", _("Hisao and Hanako welcome Lilly and Akira back to Japan."), "hisao"),
        (_("Chapter 5"), "sisterhood_ch5", _("Hisao, Hanako, and Lilly take a trip to Hokkaido."), "hisao"),
        (_("Chapter 0"), "sisterhood_ch0", _("Hanako has a personal conversation with Miss Yumi."), "hanako"),
        (_("Chapter 6"), "sisterhood_ch6", _("Hanako and Hisao spend the night in Hokkaido together."), "hanako"),
        (_("Chapter 7"), "sisterhood_ch7", _("Hanako helps with a favor from Naomi and Natsume."), "hanako"),
        (_("Chapter 8"), "sisterhood_ch8", _("Hanako and Hisao go to the arcade."), "hanako"),
        (_("Chapter 9"), "sisterhood_ch9", _("Hanako and Hisao spend the night in a fancy hotel."), "hanako"),
        (_("Chapter 10"), "sisterhood_ch10", _("Hisao and Hanako learn of Lilly's summons."), "hisao"),
        (_("Chapter 11"), "sisterhood_ch11", _("Hanako and Lilly have a memorable night at a fancy restaurant."), "hanako"),
        (_("Chapter 12"), "sisterhood_ch12", _("Lilly makes a difficult decision."), "lilly"),
        (_("Chapter 13"), "sisterhood_ch13", _("Hanako and Lilly make preparations for Lilly's going-away party."), "hanako"),
        (_("Chapter 14"), "sisterhood_ch14", _("Hisao wakes up to an unfamiliar yet familiar ceiling."), "hisao"),
        (_("Chapter 15"), "sisterhood_ch15", _("Hisao is determined to reconcile with Hanako."), "hisao"),
        (_("Chapter 16"), "sisterhood_ch16", _("Hanako meets Hisao on the rooftop of Yamaku."), "hanako"),
        (_("Chapter 17"), "sisterhood_ch17", _("Lilly and Hanako talk it out."), "lilly")
    ]

    # TRANSFORMS

    #define charamoveslow = MoveTransition(1.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    transform phonebox:
        xanchor 1.0 xpos 0.95 yanchor 1.0 ypos 0.81
    transform sittingpos:
        xpos 0.5 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform twoleft_sittingpos:
        xpos 0.3 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform tworight_sittingpos:
        xpos 0.7 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    #define chchange = charachange #charachangealways
    #define chchangefast = charachangefast #Dissolve(0.2)
    define chchange = charachangealways
    define chchangefast = Dissolve(0.2)
    define ffp = 0.4
    define fftr = Dissolve(ffp)

    # LOGOS

    image shlogo quill = f"{sh_path}/logo/logo_quill.png"
    image shlogo title = f"{sh_path}/logo/logo_title.png"

    # BACKGROUNDS

    image bg inverness_backyard = f"{sh_bgs}/backyard.jpg"
    image bg inverness_shore = f"{sh_bgs}/shore_2.png"
    image bg inverness_house_front = f"{sh_bgs}/house_front.png"
    image bg therapist_office = f"{sh_bgs}/therapist_office.jpg"
    image bg hok_field_ni = f"{sh_bgs}/hok_field_ni.jpg"
    image bg hok_houseext_ni = f"{sh_bgs}/hok_houseext_ni.jpg"
    image bg hok_bedroom = f"{sh_bgs}/hok_bedroom.jpg"
    image bg newspaper_club = f"{sh_bgs}/newspaper_club.jpg"
    image bg hotel_bathroom = f"{sh_bgs}/hotel_bathroom.jpg"
    image bg hotel_room = f"{sh_bgs}/hotel_room.jpg"
    image bg fanres_entrance = f"{sh_bgs}/fanres_entrance.jpg"
    image bg fanres_table = f"{sh_bgs}/fanres_table.jpg"
    image bg hotel_hallway = f"{sh_bgs}/hotel_hallway.jpg"
    image bg hotel_room2 = f"{sh_bgs}/hotel_room2.jpg"
    image bg suburb_roadcenter_blur_rn = rain(f"{sh_bgs}/suburb_roadcenter_blur.jpg")
    image rainmemory = Composite(
        (1920, 1080),
        (0, 0), "bg suburb_roadcenter_rn",
        (0, 0), "rain normal"
    )

    image ev wheatfield = f"{sh_path}/event/wheatfield/wheatfield_smile.png"

    # VFX

    image go_board = f"{sh_path}/vfx/go_board.png"

    # BGM

    define music_waltz = f"{sh_path}/bgm/Waltz_in_A_Minor.ogg"

    # SOUND EFFECTS

    define sfx_nature = sh_sfx("nature")
    define sfx_waves = sh_sfx("waves")
    define sfx_rockskip = sh_sfx("rockskip")
    define sfx_rockskip_fail = sh_sfx("rockskip_fail")
    define sfx_rocksplash = sh_sfx("rocksplash")
    define sfx_phonedial = sh_sfx("phonedial")
    define sfx_crickets = sh_sfx("crickets")
    define sfx_gostone_soft = sh_sfx("gostone_soft")
    define sfx_gostone = sh_sfx("gostone_medium")
    define sfx_gostone_hard = sh_sfx("gostone_hard")
    define sfx_gostone_soft_stress1 = sh_sfx("gostone_soft_stress1")
    define sfx_gostone_soft_stress2 = sh_sfx("gostone_soft_stress2")
    define sfx_gostone_stress1 = sh_sfx("gostone_medium_stress1")
    define sfx_gostone_stress2 = sh_sfx("gostone_medium_stress2")
    define sfx_bedsheets = sh_sfx("bedsheets")
    define sfx_shower = sh_sfx("shower")
    define sfx_taps1 = sh_sfx("taps1")
    define sfx_taps2 = sh_sfx("taps2")
    define sfx_taps3 = sh_sfx("taps3")
    define sfx_taps4 = sh_sfx("taps4")
    define sfx_lightswitch_on = sh_sfx("lightswitch_on")
    define sfx_lightswitch_off = sh_sfx("lightswitch_off")
    define sfx_cellphonering = sh_sfx("cellphonering")
    define sfx_hospital = sh_sfx("hospital")

    define config.font_name_map["pixel"] = f"{sh_path}/font/Quinquefive-ALoRM.ttf"
