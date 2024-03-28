screen gallery_menu:
    tag menu
    key "mouseup_3" action Return()

    add "#fff"
    add "gui/starlight_2.png"
    add "gui/border.png"

    hbox:
        xalign 0.5
        yalign 0.0
        yoffset 15
        text _("GALLERY") style "game_menu_button_text"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        imagebutton:
            idle im.Scale("gui/extra/gal_btn_p.png",400,400)
            hover im.Scale("gui/extra/gal_btn_p_hover.png",400,400)
            action NullAction()
        imagebutton:
            idle im.Scale("gui/extra/gal_btn_m.png",400,400)
            hover im.Scale("gui/extra/gal_btn_m_hover.png",400,400)
            action ShowMenu('gallery_m')
        imagebutton:
            idle im.Scale("gui/extra/gal_btn_x.png",400,400)
            hover im.Scale("gui/extra/gal_btn_x_hover.png",400,400)
            action NullAction()
        
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