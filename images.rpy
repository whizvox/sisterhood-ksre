init 1 python:
    def sh_image_variants(base_path, base_name, variants, on_find, file_ext="jpg"):
        for variant in variants:
            imgpath = f"{base_path}/{base_name}/{base_name}_{variant}.{file_ext}"
            if renpy.loadable(imgpath):
                on_find(variant, imgpath)
            else:
                renpy.log("[SISTERHOOD] Could not load image: " + imgpath)

    def sh_sprites(char, faces, poses=None, outfits=None):
        if poses is None:
            poses = [""]
        if outfits is None:
            outfits = [""]
        for pose in poses:
            for face in faces:
                for outfit in outfits:
                    variant = ""
                    if pose != "":
                        variant += pose + "_"
                    variant += face
                    if outfit != "":
                        variant += "_" + outfit
                    imgpath = f"{sh_path}/sprites/{char}/{char}_{variant}.png"
                    if renpy.loadable(imgpath):
                        renpy.image(f"{char} {variant}", imgpath)
                        renpy.image(f"{char} {variant}_ss", sp_sunset(imgpath))
                        renpy.image(f"{char} {variant}_ni", sp_night(imgpath))
                        renpy.image(f"{char} {variant}_rn", sp_rain(imgpath))
                    closeimgpath = f"{sh_path}/sprites/{char}/close/{char}_{variant}_close.png"
                    if renpy.loadable(closeimgpath):
                        renpy.image(f"{char} {variant}_close", closeimgpath)
                        renpy.image(f"{char} {variant}_close_ss", sp_sunset(closeimgpath))
                        renpy.image(f"{char} {variant}_close_ni", sp_night(closeimgpath))
                        renpy.image(f"{char} {variant}_close_rn", sp_rain(closeimgpath))
                    supercloseimgpath = f"{sh_path}/sprites/{char}/superclose/{char}_{variant}_superclose.png"
                    if renpy.loadable(supercloseimgpath):
                        renpy.image(f"{char} {variant}_superclose", supercloseimgpath)
                        renpy.image(f"{char} {variant}_superclose_ss", sp_sunset(supercloseimgpath))
                        renpy.image(f"{char} {variant}_superclose_ni", sp_night(supercloseimgpath))
                        renpy.image(f"{char} {variant}_superclose_rn", sp_rain(supercloseimgpath))

    def phonebox_sprites(char, variants, vanilla=True, xoff=0, yoff=0, cropxoff=0, cropyoff=0):
        for variant in variants:
            imgpath = f"sprites/{char}/{char}_{variant.replace(' ', '_')}.png"
            if not vanilla:
                imgpath = f"{sh_path}/{imgpath}"
            renpy.image(char + " " + variant + "_phone", Composite(
                (436, 436),
                (0, 0), DynamicDisplayable(_sh_get_phonebox_bg),
                (30 + xoff, 30 + yoff), Crop((20 + cropxoff, 107 + cropyoff, 405, 402), char + " " + variant)
            ))
    
    def sh_bg(base_name):
        return f"{sh_path}/bgs/{base_name}.jpg"
    
    def sh_bgs(category, locations):
        for location in locations:
            renpy.image(f"bg {category}_{location}", sh_bg(category + "_" + location))

    def sh_event(base_name, variants, mark_adult=False):
        sh_image_variants(sh_path + "/event", base_name, variants, lambda variant, path: renpy.image(f"ev {base_name}_{variant}", adult(path) if mark_adult else path))
    
    def sh_fireflies():
        for i in range(0, 15):
            imgpath = f"{sh_path}/vfx/fireflies/ff{i:02}.png"
            if renpy.loadable(imgpath):
                renpy.image(f"firefly b{i}", imgpath)
            else:
                renpy.log(f"[SISTERHOOD] Could not load firefly image: {imgpath}")

    sh_sprites("takawa", ["serious", "smile", "happy", "worried", "calculating", "stern"])
    # takawa blurred sprites
    for face in ("smile", "serious"):
        for i in range(1, 3):
            renpy.image(f"takawa {face}_close_blur{i}", im.Blur(f"{sh_path}/sprites/takawa/close/takawa_{face}_close.png", i))
    sh_sprites("akira", ["angry", "cheerful", "depressed", "peaceful", "pleased", "ponder", "sad", "sheepish", "smug", "sweet", "wistful", "distant"], poses=["basic"])
    sh_sprites("hanako", ["bashful", "distant", "downsmile", "emb", "worry"], poses=["basic", "emb"], outfits=["clip"])
    sh_sprites("hanako", ["blushtimid", "downsmile", "downtimid", "emb", "sad", "smile", "worry", "bashful"], poses=["emb", "basic", "cover"], outfits=["cas_clip", "cas_nohat_clip"])
    sh_sprites("hanagown", ["worry_blush_close"])
    sh_sprites("hisao", ["annoy", "bashful", "blush", "frown", "grin", "smile", "neutral", "pout", "speak", "worry", "neutralblush", "sweet"], poses=["basic", "cross"], outfits=["uni", "swt", "polo", "bath", "nak"])
    sh_sprites("naomi", ["focus", "grin", "laugh", "neutral", "shock", "smile", "wink"], poses=["basic", "bend"])
    sh_sprites("natsume", ["cheerful", "neutral", "smile"], poses=["basic", "hands"])
    sh_sprites("misha", ["sign_sad_cas"])
    sh_sprites("lilly", ["basic_cheerful_close", "cane_sad_close", "cane_cry", "cane_cry_close", "basic_satisfied", "cane_satisfied_cas", "cane_offended_cas_close", "cane_sad_cas_close"])
    sh_sprites("doctor", ["bigsmile"])
    sh_sprites("kenji", ["happy", "neutral", "tsun"], outfits=["gym"])

    phonebox_sprites("akira", ["basic_smile", "basic_annoyed", "basic_resigned", "basic_laugh", "basic_lost", "basic_boo", "basic_cheerful", "basic_lost", "basic_angry"])
    phonebox_sprites("hanako", ["basic_worry", "def_worry"], xoff=-45)
    phonebox_sprites("hanako", ["emb_smile", "emb_timid", "emb_blushing"])
    phonebox_sprites("hanagown", ["worry", "distant", "irritated", "normal"])
    phonebox_sprites("lilly", ["basic_smile", "basic_concerned", "basic_sad", "basic_displeased", "cane_oops", "basic_reminisce"], cropyoff=-40)
    phonebox_sprites("karla", ["basic_smile_cas", "basic_sheepish_cas", "basic_ponder_cas", "basic_distant_cas", "basic_lost_cas", "basic_resigned_cas", "basic_wistful_cas", "basic_cheerful_cas", "basic_sweet_cas"], vanilla=False)
    phonebox_sprites("hisao", ["basic_worry_polo", "basic_speak_polo", "basic_neutral_polo", "basic_sweet_polo"], cropxoff=95, cropyoff=-90)

    sh_event("wheatfield", ["smile", "talk", "dreamy", "awkward"])
    sh_event("funindark", ["hug_rest", "hug_rest_large", "hug_neck", "hug_cheek", "hug_kiss", "hug_look", "hug_awkward"])
    sh_event("funindark", ["naked_touch", "naked_touch_close", "naked_hand", "naked_hand_close", "naked_breast", "naked_breast_large", "naked_grab", "naked_grab_close", "naked_masturbate", "naked_climax", "naked_climax_close"], mark_adult=True)
    sh_event("hotel", ["onhanako", "onhanako_large", "onhisao", "onhisao_large", "mirror", "layontop", "thigh", "thigh_large", "thigh_climax", "masturbate", "masturbate_climax", "bed", "bed_climax"], mark_adult=True)
    sh_event("ballroomdance", ["emb_large", "emb_normal", "smile_large", "smile_normal"])
    sh_event("rooftopkiss", ["normal"])
    sh_event("caress", ["normal", "large"])
    sh_event("withoutthinking", ["lilly", "crowd", "cpr", "nohisao"])
    sh_event("bedridden", ["akira_provoke", "akira_angry", "akira_shout", "akira_distant", "akhiha_look", "akhiha_focus", "akhiha_open", "akhiha_talk", "akhiha_phone", "akhiha_smile"])

    sh_fireflies()

    sh_bgs("inverness", ["shore", "street", "pubdoor", "pubback", "pubbilliards", "field", "culloden", "tree"])
    sh_bgs("satou", ["patio", "entrance", "entrance_blur", "grounds", "livingroom", "livingroom_ni", "stairs", "stairs_blur", "guestroom", "kitchen", "kitchen_ni", "bathroom", "study", "study_blur", "changingroom", "guestroom_ni", "guest2"])
    sh_bgs("school", ["staircase3", "hallway4", "therapist", "newspaper", "firstaidclass"])
    sh_bgs("hok", ["field_ni", "houseext_ni", "bedroom", "newspaper"])
    sh_bgs("arcade", ["airhockey", "fightgame", "shooter", "floor", "crane", "bike"])
    sh_bgs("city", ["coffeeshop"])
    sh_bgs("hotel", ["bathroom", "room"])
    sh_bgs("fanres", ["entrance", "table"])
    sh_bgs("hosp", ["hallway", "office"])
    sh_bgs("airport", ["coffeeshop", "baggageclaim", "inverness"])
    sh_bgs("plane", ["cabin", "seat", "window_runway", "window_city", "window_clouds", "bathroom"])
    sh_bgs("raigmore", ["ambulance", "ambulance_blur", "elevator", "entrance", "hallway", "office", "room", "waitroom", "waitcard"])
    sh_bgs("smt", ["reception", "office"])
    sh_bgs("akira", ["car"])

init 1:
    # backgrounds
    image bg school_therapist_blur1 = im.Blur(sh_bg("school_therapist"), 1)
    image bg school_therapist_blur2 = im.Blur(sh_bg("school_therapist"), 2)
    image bg school_road_run_rn = rain(sh_bg("school_road_run"))
    image bg suburb_roadcenter_run_rn = rain(sh_bg("suburb_roadcenter_run"))
    image bg hosp_room2_blur = im.Blur("bgs/hosp_room2.jpg", 2)
    image bg hosp_ceiling_blur = im.Blur("bgs/hosp_ceiling.jpg", 2)
    image bg satou_entrance_blur_ss = sunset(sh_bg("satou_entrance_blur"))
    image bg raigmore_entrance_ss = sunset(sh_bg("raigmore_entrance"))

    # special events
    image ev rainyroad:
        block:
            rain(f"{sh_path}/event/rainyroad/rainyroad_a.jpg") with Dissolve(0.5)
            0.5
            rain(f"{sh_path}/event/rainyroad/rainyroad_b.jpg") with Dissolve(0.5)
            0.5
            repeat
    image rainmemory = Composite(
        (1920, 1080),
        (0, 0), "bg suburb_roadcenter_rn",
        (0, 0), "rain normal"
    )

    # vfx
    image go_board = f"{sh_path}/vfx/go_board.png"
    image hisao_roof_blur = f"{sh_path}/vfx/hisao_roof_blur.png"
    image bouquet = f"{sh_path}/vfx/bouquet.png"
    image hanako_dormhisao_blur = f"{sh_path}/vfx/hanako_dormhisao_blur.jpg"
    image hanako_hairclip = f"{sh_path}/vfx/hanako_hairclip.png"
    image niji_plush = f"{sh_path}/vfx/niji_plush.png"
    image hanako_camera = f"{sh_path}/vfx/hanako_camera.png"
    image darkness:
        block:
            f"{sh_path}/vfx/darkness/darkness_1.jpg" with dissolve
            0.5
            f"{sh_path}/vfx/darkness/darkness_2.jpg" with dissolve
            0.5
            repeat

    # logos
    image shlogo quill = f"{sh_path}/logo/logo_quill.png"
    image shlogo title = f"{sh_path}/logo/logo_title.png"
    image shlogo quill_outline = f"{sh_path}/logo/logo_quill_outline.png"
    image shlogo title_outline = f"{sh_path}/logo/logo_text_outline.png"

    # extra gui
    image white_vignette = f"{sh_path}/gui/white_vignette.png"

    # credits
    image sh_credits_overlay = f"{sh_path}/gui/credits/vignette_overlay.png"

    image sh_credits_text = Text(_("""
    {b}Backgrounds{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    Francis York Media Inc.
    deemur on Pixabay
    Zencare Group Inc.
    Jeremy Bishop on Unsplash
    StockSnap on Pixabay
    TUS PRESS
    Drobot Dean
    Harris' The San Francisco Steak Restaurant
    Christina Mueller
    B Lucava on Flickr
    Visit Inverness Loch Ness
    Highland News and Media Ltd.
    kanagawa-hotels.com
    TillTheMoneyRunsOut.com
    legendarysoulII
    Firefall
    whizvox
    \n\n
    {b}Sound Effects{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    EmpressKathryne on Pixabay
    CaganCelik on FreeSound
    bevibeldesign on FreeSound
    Kraftaggregat on FreeSound
    ShidenBeatsMusic on Pixabay
    leonelmail on FreeSound
    ellie.vanderlip on FreeSound
    Kelieon on YouTube
    Yuval on FreeSound
    Pagey1969
    USBMED Ambiences Sound Library on FreeSound
    Ataraxy ASMR on YouTube
    Super Street Figher II
    Halo: Combat Evolved
    G.Lamont on FreeSound
    amszala on FreeSound
    Adam_Joseph on FreeSound
    PNMCarrieRailfan on FreeSound
    Juan_Merie_Venter on FreeSound
    plivesey on FreeSound
    mrrap4food on FreeSound
    megashroom on FreeSound
    aUREa on FreeSound
    yake01 on FreeSound
    theplax on FreeSound
    tim.kahn on FreeSound
    kwahmah_02 on FreeSound
    Robinhood76 on FreeSound
    magedu on FreeFound
    Eryliaa on Pixabay
    whizvox
    \n\n
    {b}Fonts{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    “QuinqueFive” by GGBotNet
    “Newsreader” by Production Type
    \n\n
    {b}Additional Writing{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    Guest Poster
    Celestial Caesar
    \n\n
    {b}Background Music{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    “Waltz in A Minor” by CalvinClavier on Pixabay
    \n\n
    {b}End Credits Song{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    {size=+10}Bloom{/size}
    Composed and Arranged by Castillerian
    \n\n
    {b}Event Art{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    ZenMaruki
    PrinceG07
    Likhos
    legendarysoulII
    \n\n
    {b}Sprite Art{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    DIZZEN
    \n\n
    {b}Additional Art{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    nijo
    GoodFreePhotos.com
    \n\n
    {b}Sprite Edits{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    nijo
    Celestial Caesar
    Guest Poster
    whizvox
    \n\n
    {b}Beta Testing{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    Guest Poster
    Celestial Caesar
    Melad
    ZenMaruki
    \n\n
    {b}Special Thanks{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    Celestial Caesar
    Ikariya
    Vladimir Hodakov
    nijo
    Grayest
    EurobeatJester
    Fleeting Heartbeat Studios
    Four Leaf Studios
    The Katawa Shoujo Community
    \n\n\n\n
    """), color="#FFF", text_align=0.5, xalign=0.9, size=42)

    image sh_credits_end = Text(_("""
    {b}Original Work{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    “Sisterhood” by Guest Poster
    \n\n\n\n
    {b}Directing, Engineering, Administration{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    whizvox
    \n\n\n\n
    """), color="#FFF", text_align=0.5, xalign=0.5, size=42)

    image sh_credits = VBox(f"{sh_path}/logo/logo_title_credits.png", "sh_credits_text", "sh_credits_end")