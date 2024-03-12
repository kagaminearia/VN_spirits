
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background = im.Scale("gui/main_menu.png",1920,1080)
image main_title = im.Alpha(im.Scale("gui/main_title.png",1920,1080),0.5)


screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

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

        vbox:
            xalign 0
            spacing 45
            textbutton _("ABOUT") action ShowMenu("about")
            textbutton _("HELP") action ShowMenu("help")
            textbutton _("EXTRA") action ShowMenu("gallery")
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
