screen gallery_menu:
    tag menu
    key "mouseup_3" action Return()

    add "#fff"
    add "gui/starlight_2.png"
    add "gui/border.png"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        imagebutton:
            idle im.Scale("gui/extra/gal_x_btn_idle.png",270,480)
            hover im.Scale("gui/extra/gal_x_btn_hover.png",270,480)
            action NullAction()
        imagebutton:
            idle im.Scale("gui/extra/gal_m_btn_idle.png",270,480)
            hover im.Scale("gui/extra/gal_m_btn_hover.png",270,480)
            action NullAction()
        imagebutton:
            idle im.Scale("gui/extra/gal_p_btn_idle.png",270,480)
            hover im.Scale("gui/extra/gal_p_btn_hover.png",270,480)
            action NullAction()