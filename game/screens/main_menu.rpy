
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background = im.Scale("gui/main_menu.png",1920,1080)
image main_menu_unlock = im.Scale("gui/main_unlock.jpg",1920,1080)
image main_title = im.Alpha(im.Scale("gui/main_title.png",1920,1080),0.5)


screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    if persistent.NE == 1 and persistent.xNE == 1 and persistent.xBE == 1 and persistent.xHE == 1 and persistent.pNE == 1 and persistent.pBE == 1 and persistent.pHE == 1:
        add "main_menu_unlock"
    else:
        add "main_menu_background"
    add "main_title"

    hbox:
        style_prefix "main_navigation"
        xalign 0.5
        yalign 0.5
        spacing 1300
        vbox:
            xalign 0
            spacing 45
            textbutton _("START") action Start()
            textbutton _("CONTINUE") action Continue()
            textbutton _("LOAD") action ShowMenu("load")
            textbutton _("CONFIG") action ShowMenu("preferences")
            # textbutton _("TEST") action ShowMenu("testchapter")

        vbox:
            xalign 0
            spacing 45
            textbutton _("ABOUT") action ShowMenu("about")
            textbutton _("HELP") action ShowMenu("help")
            textbutton _("EXTRA") action ShowMenu("extra_menu")
            textbutton _("EXIT") action Quit(confirm=not main_menu)

style main_navigation_button_text:
    font gui.main_menu_font
    color "#fff"
    size 48
    xalign 0
    hover_color "#a4a4a4"
    # outlines [(2, "#a4a4a4", 3, 3)]
    outlines[(1,"#e9e9e9"),(2,"#d7d7d7"),(2,"#cacaca"),(1,"#a4a4a4")]
    

style main_navigation_button is gui_button

# screen testchapter():
#     tag menu
#     key "mouseup_3" action Return()
#     add "#ffffffff"
#     add "gui/border.png"
#     vbox:
#         xalign 0.25
#         yalign 0.25
#         spacing 10
#         textbutton ("prolo") action Start("prologue")
#         textbutton ("chap1") action Start("chapter1")
#         textbutton ("chap2") action Start("chapter2")
#         textbutton ("chap3") action Start("chapter3")
#         textbutton ("chap4") action Start("chapter4")
#         textbutton ("chap6") action Start("chapter6")
#         textbutton ('chap6_x') action Start("chapter6x")
#         textbutton ('chap6_p') action Start("chapter6p")
#         textbutton ('chap7_x') action Start("chapter7_x")
#         textbutton ('chap7_p') action Start("chapter7_p")
#         textbutton ('chap8_x') action Start("chapter8x")
#         textbutton ('chap8_p') action Start("chapter8p")
#         textbutton ('chap9_x') action Start("chapter9x")
#         textbutton ('chap9_p') action Start("chapter9p")
