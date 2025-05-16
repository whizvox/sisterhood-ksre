init 1 python:
    def sh_register_sfx(names):
        for name in names:
            store.__setattr__(f"sfx_{name}", f"{sh_path}/sfx/{name}.ogg")
    
    sh_register_sfx([
        # arcade
        "airhockey_rally", "airhockey_score1", "airhockey_score2", "airport_ambience", "arcade_ambience", "gameover",
        "hadouken", "yogafire",
        # kitchen
        "boilingwater_pour", "boilingwater", "cuttingboard", "ovenbeep", "whisking",
        # go
        "gostone_hard", "gostone_stress1", "gostone_stress2", "gostone", "gostone_soft_stress1", "gostone_soft_stress2",
        "gostone_soft",
        # phone
        "phonering", "phonedial", "phonenotif", "phonepickup",
        # plane
        "plane_aftertakeoff", "plane_beforetakeoff", "plane_dingdong", "plane_inflight", "plane_waiting",
        # pub
        "applause", "billiards_blunder",
        # nature
        "bushes", "crickets", "nature", "waves",
        # cars
        "car_driveup", "cars_ambience",
        # rock skipping
        "rockskip_fail", "rockskip", "rocksplash",
        # lightswitch
        "lightswitch_off", "lightswitch_on",
        # tapping on door
        "taps1", "taps2", "taps3", "taps4",
        # misc ambience
        "bikeride", "hospital_ambience", "ticktock", "windy",
        # other
        "alarmbeep", "bedsheets", "bicyclecrash", "camerashutter", "chairscrape", "clap", "collapse", "metalclink",
        "shower", "teacup_loudclink"
    ])

init:
    # BGM

    define music_waltz = f"{sh_path}/bgm/Waltz_in_A_Minor.ogg"
    define music_bloom = f"{sh_path}/bgm/Bloom.ogg"

    # SPECIAL SOUND EFFECTS

    define sfx_plane_takeoff = "<loop 59.055>" + sh_sfx("plane_takeoff")
