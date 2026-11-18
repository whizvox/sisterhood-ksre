init python:
    def sh_drizzle(my_offset = 0.0, my_xzoom = 1.0, my_yzoom = 1.0):
        return sh_drizzle_tf(my_offset, my_xzoom, my_yzoom)

init:
    transform phonebox:
        xanchor 1.0 xpos 0.95 yanchor 1.0 ypos 0.82
    transform centersit:
        xpos 0.5 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform twoleftsit:
        xpos 0.3 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform tworightsit:
        xpos 0.7 xanchor 0.5 ypos 1.1 yanchor 1.0 alpha 1.0
    transform leftsit:
        xpos 0.0 xanchor 0.0 ypos 1.1 yanchor 1.0 alpha 1.0
    transform rightsit:
        xpos 1.0 xanchor 1.0 ypos 1.1 yanchor 1.0 alpha 1.0

    transform displayitemshow(ya=0.5):
        truecenter
        ypos ya+0.2 alpha 0.0
        easein 1.0 alpha 1.0 ypos ya

    transform displayitem(ya=0.5):
        truecenter
        alpha 1.0 ypos ya

    transform displayitemhide(ya=0.5):
        ease 1.0 ypos ya+0.2 alpha 0.0

    transform sepia:
        matrixcolor SepiaMatrix(tint="#ffefd7")

    transform sepiamuted:
        matrixcolor TintMatrix("#ffefd7") * SaturationMatrix(0.5)

    transform nightfilter:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.92, 1.0))) * BrightnessMatrix(-0.05)

    transform soapopera_talk:
        anchor (0.5, 0.5) pos (0.5, 0.85)
    
    transform showertext(x, y, rotation_start, rotation_end):
        pos (x, y) anchor (0.5, 0.5) rotate rotation_start alpha 0.0
        parallel:
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.0
        parallel:
            linear 2.0 rotate rotation_end

    transform sh_fadebottomenter:
        ypos 1.2 alpha 0.0
        ease 1.0 ypos 1.0 alpha 1.0

    transform sh_fadebottomexit:
        ease 1.0 ypos 1.2 alpha 0.0

    transform sh_carbob:
        truecenter ypos 0.52
        block:
            ease 2.0 ypos 0.48
            ease 2.0 ypos 0.52
            repeat
    
    transform sh_drizzle_tf(my_offset, my_xzoom, my_yzoom):
        xalign 0.5 yalign 0.5 xzoom my_xzoom yzoom my_yzoom
        my_offset
        block:
            choice:
                f"{sh_path}/vfx/drizzle/drizzle1.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle2.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle3.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle4.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle5.png" with Dissolve(0.1)
                0.2
            choice:
                f"{sh_path}/vfx/drizzle/drizzle6.png" with Dissolve(0.1)
                0.2
            repeat

    define nextchapter = Dissolve(2.0)
    define endchapter = Dissolve(3.0)
    define mediumflash = Fade(1, 0, 1, color="#FFF")
    define longflash = Fade(1.5, 0, 1.5, color="#FFF")
    define easeinmove = MoveTransition(1.5, time_warp=_warper.easein)
    define easeoutmove = MoveTransition(1.5, time_warp=_warper.easeout)
    define clockwipefast = ImageDissolve(Tile("gui/trans/clockwipe.png"), 1.0, 8)

    define erase = ImageDissolve(f"{sh_path}/gui/trans/erase.png", 2.0)
