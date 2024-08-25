default persistent.pNE = 0
default persistent.xNE = 0
default persistent.pBE = 0
default persistent.xBE = 0
default persistent.pHE = 0
default persistent.xHE = 0
default persistent.NE = 0


screen ending_menu:
    tag menu
    key "mouseup_3" action Return()
    add "#fff"
    add "gui/starlight_2.png"
    add "gui/border.png"
    hbox:
        xalign 0.5
        yalign 0.0
        yoffset 15
        text _("ENDINGS") style "game_menu_button_text"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        hbox:
            spacing 20
            if persistent.pNE == 1:
                imagebutton:
                    idle "gui/extra/img_pNE.jpg"
                    hover "gui/extra/img_pNE.jpg"
                    action Replay("pNE")
                    tooltip "回放"
            else:
                add "gui/extra/img_edlock.jpg"
            
            if persistent.xNE == 1:
                imagebutton:
                    idle "gui/extra/img_xNE.jpg"
                    hover "gui/extra/img_xNE.jpg"
                    action Replay("xNE")
                    tooltip "回放"
            else:
                add "gui/extra/img_edlock.jpg"
        hbox:
            spacing 20
            if persistent.pBE == 1:
                imagebutton:
                    idle "gui/extra/img_pBE.jpg"
                    hover "gui/extra/img_pBE.jpg"
                    action Replay("pBE")
                    tooltip "回放"
            else:
                add "gui/extra/img_edlock.jpg"
            
            if persistent.xNE == 1:
                imagebutton:
                    idle "gui/extra/img_xBE.jpg"
                    hover "gui/extra/img_xBE.jpg"
                    action Replay("xBE")
                    tooltip "回放"
            else:
                add "gui/extra/img_edlock.jpg"

        hbox:
            spacing 20
            if persistent.pHE == 1:
                imagebutton:
                    idle "gui/extra/img_pHE.jpg"
                    hover "gui/extra/img_pHE.jpg"
                    action Replay("pHE")
                    tooltip "回放"
            else:
                add "gui/extra/img_edlock.jpg"
            
            if persistent.xHE == 1:
                imagebutton:
                    idle "gui/extra/img_xHE.jpg"
                    hover "gui/extra/img_xHE.jpg"
                    action Replay("xHE")
                    tooltip "回放"
            else:
                add "gui/extra/img_edlock.jpg"
        
        if persistent.NE == 1:
                imagebutton:
                    idle "gui/extra/img_NE.jpg"
                    hover "gui/extra/img_NE.jpg"
                    action Replay("NE")
                    tooltip "回放"
        else:
            add "gui/extra/img_edlock.jpg"



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
            action ShowMenu("extra_menu")