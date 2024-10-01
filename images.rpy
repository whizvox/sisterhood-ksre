init 1 python:
    def sh_image_variants(base_path, base_name, variants, on_find, file_ext="jpg"):
        for variant in variants:
            imgpath = f"{base_path}/{base_name}/{base_name}_{variant}.{file_ext}"
            if renpy.loadable(imgpath):
                on_find(variant, imgpath)
            else:
                renpy.log("[SISTERHOOD] Could not load image: " + imgpath)

    def sh_event(base_name, variants):
        sh_image_variants(sh_path + "/event", base_name, variants, lambda variant, path: renpy.image(f"ev {base_name}_{variant}", path))
    
    sh_event("wheatfield", ["smile", "talk", "dreamy", "awkward"])