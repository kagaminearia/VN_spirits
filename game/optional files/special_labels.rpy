## Special Labels ##############################################################
##
## These are special labels that Ren'Py automatically recognizes if they
## are included with the game. Read more here:
## https://www.renpy.org/doc/html/label.html#special-labels
##

## Splash Screen ###############################################################
##
## Put the splash screen code here. It runs when the game is launched.
##

# add splashscreen before main menu
# and it only shows once 
default persistent.sp = 0
image ink = "gui/ink.png"

label splashscreen():
    if persistent.sp == 0:
        $ persistent.sp = 1
        scene bg_grey
        show ink at cg_0 with dissolve
        pause 1.5
        hide ink with dissolve
        show text _p("""
                        本故事纯属虚构\n
                        与真实世界的一切无关
                        """) with dissolve
        pause 2
        hide text with dissolve
    else:
        return

    return

## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return
