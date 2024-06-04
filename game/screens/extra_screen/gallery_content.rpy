screen gallery_m():

    tag menu
    key "mouseup_3" action Return()
    # add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    # use game_menu(_("Gallery"))
    add "#fff"
    add "gui/starlight_2.png"
    add "gui/border.png"

    hbox:
        xalign 0.5
        yalign 0.0
        yoffset 15
        text _("GALLERY") style "game_menu_button_text"

    hbox:
        yalign 0.5
        xalign 0.5
        grid 3 1:
            spacing 30
            add g.make_button("cgbtn_m1", unlocked = im.Scale("images/cg/cg_m10.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_m2", unlocked = im.Scale("images/cg/cg_m20.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_m3", unlocked = im.Scale("images/cg/cg_m30.jpg",192,108), locked = "images/lockcg.jpg")

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
            action ShowMenu("gallery_menu")

style gal_fixed:
    yfill True
    xsize config.screen_width
    align (1.0, 0.5)

style gal_grid:
    align (0.5, 0.5)
    xsize config.screen_width-420
    ysize config.screen_height-200
    spacing 50


screen gallery_p():

    tag menu
    key "mouseup_3" action Return()
    # add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    # use game_menu(_("Gallery"))
    add "#fff"
    add "gui/starlight_2.png"
    add "gui/border.png"

    hbox:
        xalign 0.5
        yalign 0.0
        yoffset 15
        text _("GALLERY") style "game_menu_button_text"
    
    hbox:
        yalign 0.5
        xalign 0.5
        grid 4 4:
            spacing 30
            add g.make_button("cgbtn_p1", unlocked = im.Scale("images/cg/cg_p10.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p2", unlocked = im.Scale("images/cg/cg_p20.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p3", unlocked = im.Scale("images/cg/cg_p30.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p4", unlocked = im.Scale("images/cg/cg_p40.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p5", unlocked = im.Scale("images/cg/cg_p50.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p6", unlocked = im.Scale("images/cg/cg_p61.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p7", unlocked = im.Scale("images/cg/cg_p71.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p8", unlocked = im.Scale("images/cg/cg_p81.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p9", unlocked = im.Scale("images/cg/cg_p91.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p10", unlocked = im.Scale("images/cg/cg_p101.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p11", unlocked = im.Scale("images/cg/cg_p111.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p12", unlocked = im.Scale("images/cg/cg_p121.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p13", unlocked = im.Scale("images/cg/cg_p131.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p14", unlocked = im.Scale("images/cg/cg_p141.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p15", unlocked = im.Scale("images/cg/cg_p151.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_p16", unlocked = im.Scale("images/cg/cg_p161.jpg",192,108), locked = "images/lockcg.jpg")

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
            action ShowMenu("gallery_menu")


screen gallery_x():

    tag menu
    key "mouseup_3" action Return()
    # add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    # use game_menu(_("Gallery"))
    add "#fff"
    add "gui/starlight_2.png"
    add "gui/border.png"

    hbox:
        xalign 0.5
        yalign 0.0
        yoffset 15
        text _("GALLERY") style "game_menu_button_text"
    
    hbox:
        yalign 0.5
        xalign 0.5
        
        vpgrid:

            cols 5
            spacing 30
            draggable True
            mousewheel True
            add g.make_button("cgbtn_x1", unlocked = im.Scale("images/cg/cg_x10.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x2", unlocked = im.Scale("images/cg/cg_x20.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x3", unlocked = im.Scale("images/cg/cg_x30.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x4", unlocked = im.Scale("images/cg/cg_x40.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x5", unlocked = im.Scale("images/cg/cg_x51.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x6", unlocked = im.Scale("images/cg/cg_x61.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x7", unlocked = im.Scale("images/cg/cg_x71.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x8", unlocked = im.Scale("images/cg/cg_x81.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x9", unlocked = im.Scale("images/cg/cg_x91.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x10", unlocked = im.Scale("images/cg/cg_x101.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x11", unlocked = im.Scale("images/cg/cg_x111.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x12", unlocked = im.Scale("images/cg/cg_x121.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x13", unlocked = im.Scale("images/cg/cg_x131.jpg",192,108), locked = "images/lockcg.jpg")
            add g.make_button("cgbtn_x14", unlocked = im.Scale("images/cg/cg_x141.jpg",192,108), locked = "images/lockcg.jpg")

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
            action ShowMenu("gallery_menu")


