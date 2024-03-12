## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

screen game_menu(title):

    add "#ffffffdb"
    add "gui/starlight_1.png"
    add "gui/border.png"
    style_prefix "game_menu"

    hbox:
        xalign 0.5
        yalign 0.0
        yoffset 15
        spacing 50

        # if main_menu:
        #     textbutton _("Start") action Start()

        if not main_menu:
            textbutton _("HISTORY") action ShowMenu("history")
            textbutton _("SAVE") action ShowMenu("save")

        textbutton _("LOAD") action ShowMenu("load")
        textbutton _("CONFIG") action ShowMenu("preferences")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("HELP") action ShowMenu("help")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("TITLE") action MainMenu()

        # if renpy.variant("pc"):
        #     textbutton _("Quit") action Quit(confirm=not main_menu)

    # textbutton _("Return"):
    #     style "return_button"
    #     action Return()

    ## Remove this line if you don't want to show the screen
    ## title text as a label (for example, if it's baked into
    ## the background image.)
    # label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    xpos 60
    yalign 1.0
    yoffset -45

style game_menu_viewport:
    xsize config.screen_width
    ysize config.screen_height
    align (0.5, 0.5)

style game_menu_side:
    yfill True
    align (1.0, 0.5)

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_label:
    padding (10, 10)

style game_menu_label_text:
    xalign 0.5 
    yalign 0.0
    size 45

style game_menu_button_text:
    font gui.main_menu_font 
    size 60
    color gui.light_blue
    hover_color "#fff"
    selected_color "#fff"
    outlines [(2,"#fff")]
