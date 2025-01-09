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
    sh_sprites("hanako", ["bashful", "distant", "downsmile", "emb", "worry"], poses=["basic", "emb"], outfits=["clip"])
    sh_sprites("hanako", ["blushtimid", "downsmile", "downtimid", "emb", "sad", "smile"], poses=["emb"], outfits=["cas_clip", "cas_nohat_clip"])
    sh_sprites("hisao", ["annoy", "blush", "frown", "grin", "smile", "neutral", "pout", "speak", "worry", "neutralblush"], poses=["basic", "cross"], outfits=["uni", "swt", "polo", "bath", "nak"])
    sh_sprites("naomi", ["focus", "grin", "laugh", "neutral", "shock", "smile"], poses=["basic", "bend"])
    sh_sprites("natsume", ["cheerful", "neutral", "smile"], poses=["basic", "hands"])
    sh_sprites("mishashort", ["sign_sad_cas"])
    sh_sprites("lilly", ["basic_cheerful_close", "cane_sad_close"])
    sh_sprites("doctor", ["bigsmile"])
    sh_sprites("kenji", ["happy", "neutral", "tsun"], [""], ["gym"])

    phonebox_sprites("akira", ["basic_smile", "basic_annoyed", "basic_resigned", "basic_laugh", "basic_lost", "basic_boo"])
    phonebox_sprites("hanako", ["basic_worry", "def_worry"], xoff=-45)
    phonebox_sprites("hanako", ["emb_smile", "emb_timid", "emb_blushing"])
    phonebox_sprites("hanagown", ["worry", "distant", "irritated", "normal"])
    phonebox_sprites("lilly", ["basic_smile", "basic_concerned", "basic_sad", "basic_displeased", "cane_oops", "basic_reminisce"], cropyoff=-40)

    sh_event("wheatfield", ["smile", "talk", "dreamy", "awkward"])
    sh_event("funindark", ["hug_rest", "hug_neck", "hug_cheek", "hug_kiss", "hug_look", "hug_awkward"])
    sh_event("funindark", ["naked_touch", "naked_touch_close", "naked_hand", "naked_hand_close", "naked_breast", "naked_breast_large", "naked_grab", "naked_grab_close", "naked_masturbate", "naked_climax", "naked_climax_close"], mark_adult=True)
    sh_event("hotel", ["onhanako", "onhanako_large", "onhisao", "onhisao_large", "mirror", "layontop", "thigh", "thigh_large", "thigh_climax", "masturbate", "masturbate_climax", "bed", "bed_climax"], mark_adult=True)
    sh_event("ballroomdance", ["emb_large", "emb_normal", "smile_large", "smile_normal"])
    sh_event("caress", ["normal", "large"])

    sh_fireflies()

init 1:
    # backgrounds
    image bg satou_house_patio = f"{sh_bgs}/satou_house_patio.jpg"
    image bg inverness_shore = f"{sh_bgs}/shore.jpg"
    image bg satou_house_entrance = f"{sh_bgs}/satou_house_entrance.jpg"
    image bg therapist_office = f"{sh_bgs}/therapist_office.jpg"
    image bg therapist_office_blur1 = im.Blur(f"{sh_bgs}/therapist_office.jpg", 1)
    image bg therapist_office_blur2 = im.Blur(f"{sh_bgs}/therapist_office.jpg", 2)
    image bg hok_field_ni = f"{sh_bgs}/hok_field_ni.jpg"
    image bg hok_houseext_ni = f"{sh_bgs}/hok_houseext_ni.jpg"
    image bg hok_bedroom = f"{sh_bgs}/hok_bedroom.jpg"
    image bg newspaper_club = f"{sh_bgs}/newspaper_club.jpg"
    image bg arcade_airhockey = f"{sh_bgs}/arcade_airhockey.jpg"
    image bg arcade_fightgame = f"{sh_bgs}/arcade_fightgame.jpg"
    image bg arcade_shooter = f"{sh_bgs}/arcade_shooter.jpg"
    image bg arcade_floor = f"{sh_bgs}/arcade_floor.jpg"
    image bg arcade_crane = f"{sh_bgs}/arcade_crane.jpg"
    image bg arcade_bike = f"{sh_bgs}/arcade_bike.jpg"
    image bg coffeeshop = f"{sh_bgs}/coffeeshop.jpg"
    image bg hotel_bathroom = f"{sh_bgs}/hotel_bathroom.jpg"
    image bg hotel_room = f"{sh_bgs}/hotel_room3.jpg"
    image bg fanres_entrance = f"{sh_bgs}/fanres_entrance.jpg"
    image bg fanres_table = f"{sh_bgs}/fanres_table.jpg"
    image bg hotel_hallway = f"{sh_bgs}/hotel_hallway.jpg"
    image bg suburb_roadcenter_blur_rn = rain(f"{sh_bgs}/suburb_roadcenter_blur.jpg")
    image bg hosp_room2_blur = im.Blur(f"bgs/hosp_room2.jpg", 2)
    image bg hosp_ceiling_blur = im.Blur("bgs/hosp_ceiling.jpg", 2)

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

    # logos
    image shlogo quill = f"{sh_path}/logo/logo_quill.png"
    image shlogo title = f"{sh_path}/logo/logo_title.png"
    image shlogo quill_outline = f"{sh_path}/logo/logo_quill_outline.png"
    image shlogo title_outline = f"{sh_path}/logo/logo_text_outline.png"

    # extra gui
    image white_vignette = f"{sh_path}/gui/white_vignette.png"

    # credits
    image sh_credits = Text(_("""
    {image=mods/sisterhood/logo/logo_title.png}
    \n\n\n\n
    {b}Backgrounds{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    Francis York Media Inc.
    deemur on Pixabay
    Zencare Group Inc.
    Jeremy Bishop on Unsplash
    StockSnap on Pixabay
    Massachusettes College of Art and Design
    Drobot Dean
    Harris' The San Francisco Steak Restaurant
    Christina Mueller
    GoodFreePhotos.com
    LegendarySoul
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
    whizvox
    \n\n
    {b}Music{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    "Waltz in A Minor" by CalvinClavier on Pixabay
    \n\n
    {b}Event Art{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    ZenMaruki
    PrinceG07
    Likhos
    LegendarySoul
    \n\n
    {b}Sprite Art{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    DIZZEN
    \n\n
    {b}Sprite Edits{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    nijo
    Alex
    whizvox
    \n\n
    {b}Special Thanks{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    Alex
    Grayest
    Ikariya
    Faken
    Vladimir Hodakov
    EurobeatJester
    Haiti
    Fleeting Heartbeat Studios
    Four Leaf Studios
    The Katawa Shoujo Community
    \n\n\n\n
    {b}Original Work{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    "Sisterhood" by Guest Poster
    \n\n\n\n
    {b}Directing, Engineering, Administration{/b}
    {image=mods/sisterhood/gui/credits/section_underline.png}
    whizvox
    \n\n\n\n
    """), color="#FFF", text_align=0.5, xalign=0.5, size=42)