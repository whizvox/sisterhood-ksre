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

    def sh_event(base_name, variants):
        sh_image_variants(sh_path + "/event", base_name, variants, lambda variant, path: renpy.image(f"ev {base_name}_{variant}", path))
    
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
            renpy.image(f"takawa {face}_close_blur{i}", f"{sh_path}/sprites/takawa/close/takawa_{face}_close_blur{i}.png")
    sh_sprites("hanako", ["bashful", "distant", "downsmile", "emb"], poses=["basic", "emb"], outfits=["clip"])
    sh_sprites("hanako", ["blushtimid", "downsmile", "downtimid", "emb", "sad", "smile"], poses=["emb"], outfits=["cas_clip", "cas_nohat_clip"])
    sh_sprites("hisao", ["annoy", "blush", "frown", "grin", "smile", "neutral", "pout", "speak", "worry"], poses=["basic", "cross"], outfits=["uni", "swt", "polo", "bath", "nak"])
    sh_sprites("naomi", ["focus", "grin", "laugh", "neutral", "shock", "smile"], poses=["basic", "bend"])
    sh_sprites("natsume", ["cheerful", "neutral", "smile"], poses=["basic", "hands"])
    sh_sprites("mishashort", ["sign_sad_cas"])
    sh_sprites("lilly", ["basic_cheerful_close", "cane_sad_close"])
    sh_sprites("doctor", ["bigsmile"])

    phonebox_sprites("akira", ["basic_smile", "basic_annoyed", "basic_resigned", "basic_laugh", "basic_lost", "basic_boo"])
    phonebox_sprites("hanako", ["basic_worry", "def_worry"], xoff=-45)
    phonebox_sprites("hanako", ["emb_smile", "emb_timid", "emb_blushing"])
    phonebox_sprites("hanagown", ["worry", "distant", "irritated", "normal"])
    phonebox_sprites("lilly", ["basic_smile", "basic_concerned", "basic_sad", "basic_displeased", "cane_oops", "basic_reminisce"], cropyoff=-40)

    sh_event("wheatfield", ["smile", "talk", "dreamy", "awkward"])
    sh_event("hotel", ["1_large", "1", "2_large", "2", "3", "4_large", "4", "4a", "5", "5a"])
    sh_event("caress", ["1"])

    sh_fireflies()

init 1:
    # backgrounds
    image bg inverness_backyard = f"{sh_bgs}/backyard.jpg"
    image bg inverness_shore = f"{sh_bgs}/shore.jpg"
    image bg inverness_house_front = f"{sh_bgs}/house_front.png"
    image bg therapist_office = f"{sh_bgs}/therapist_office.jpg"
    image bg therapist_office_blur1 = f"{sh_bgs}/therapist_office_blur1.jpg"
    image bg therapist_office_blur2 = f"{sh_bgs}/therapist_office_blur2.jpg"
    image bg hok_field_ni = f"{sh_bgs}/hok_field_ni.jpg"
    image bg hok_houseext_ni = f"{sh_bgs}/hok_houseext_ni.jpg"
    image bg hok_bedroom = f"{sh_bgs}/hok_bedroom.jpg"
    image bg newspaper_club = f"{sh_bgs}/newspaper_club.jpg"
    image bg hotel_bathroom = f"{sh_bgs}/hotel_bathroom.jpg"
    image bg hotel_room = f"{sh_bgs}/hotel_room3.jpg"
    image bg fanres_entrance = f"{sh_bgs}/fanres_entrance.jpg"
    image bg fanres_table = f"{sh_bgs}/fanres_table.jpg"
    image bg hotel_hallway = f"{sh_bgs}/hotel_hallway.jpg"
    image bg suburb_roadcenter_blur_rn = rain(f"{sh_bgs}/suburb_roadcenter_blur.jpg")

    # special events
    image ev rainyroad:
        f"{sh_path}/event/rainyroad_a.jpg" with Dissolve(0.5)
        f"{sh_path}/event/rainyroad_b.jpg" with Dissolve(0.5)
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
