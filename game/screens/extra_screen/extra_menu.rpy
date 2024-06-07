screen extra_menu:
    tag menu
    key "mouseup_3" action Return()
    add "#fff"
    add "gui/starlight_2.png"
    add "gui/border.png"

    hbox:
        xalign 0.5
        yalign 0.0
        yoffset 15
        text _("EXTRA") style "game_menu_button_text"

    vbox:
        style_prefix "extra"
        xalign 0.5
        yalign 0.5
        spacing 40
        textbutton _("CG画廊") action ShowMenu("gallery_menu")
        textbutton _("结局列表") action ShowMenu("ending_menu")

    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -15
        textbutton _("RETURN"):
            text_font gui.main_menu_font 
            text_size 60
            text_color gui.light_blue
            text_hover_color "#fff"
            text_selected_color "#fff"
            text_outlines[(2,"#fff")]
            action Return()

style extra_button:
    xysize (350, 80)
    background gui.light_blue
    hover_background "#fff"

style extra_button_text:
    xalign 0.5
    yalign 0.5
    font gui.interface_text_font
    color gui.light_grey
    hover_color gui.light_blue