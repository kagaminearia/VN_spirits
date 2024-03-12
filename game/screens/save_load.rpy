## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 400
define config.thumbnail_height = 300
define gui.file_slot_cols = 1
define gui.file_slot_rows = 3
define slot_verticle_spacing = 120
define slot_x_size = 600
define slot_y_size = 160


screen save():

    tag menu

    # add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use file_slots(_("Save"))


screen load():

    tag menu

    # add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"), auto=_("Automatic saves"),
        quick=_("Quick saves"))

    use game_menu(title)

    fixed:
        xalign 0.5 
        yalign 0.5
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on it.
        ## This can be pretty easily removed if you want.
        ## Don't forget to also remove the `default` at the top if so.

        side "c":
            area (150, 180, 2000, 2000)
            viewport id "slot":
                grid gui.file_slot_cols gui.file_slot_rows:
                    xalign 1.0 yalign 0.5 spacing slot_verticle_spacing
                    for i in range(gui.file_slot_rows):
                        grid 2 1:
                            style_prefix "slot"
                            spacing 50

                            python:
                                slot = i * 2 + 1
                                name_to_save = ""
                                strip = lambda string : string \
                                    if len(string) <= 25 \
                                    else string[: 25] + "……"

                                if len(_history_list) != 0:
                                    if type(_history_list[-1].who) is NoneType:
                                        name_to_save = strip(_history_list[-1].what)
                                    else: 
                                        name_to_save = (
                                            "【" + _history_list[-1].who + "】 "
                                            + strip(_history_list[-1].what)
                                        )
                            
                            button:
                                action [
                                    SetVariable("save_name", name_to_save),
                                    FileAction(slot)
                                ]

                                hbox:
                                    spacing 10
                                    if FileTime(slot):
                                        add FileScreenshot(slot) align(0.1, 0.1) zoom 0.6
                                        vbox:
                                            xalign 0.1 yalign 0.1 spacing 10
                                            text "{color=#000000}%s{/color}" % FileTime(slot, format=_("{#file_time}%Y/%m/%d %H:%M")):
                                                style "slot_time_text"
                                            text FileSaveName(slot):
                                                style "slot_name_text"
                                    else:
                                        image "gui/button/slot_idle_background.png" zoom 0.6
                                        hbox:
                                            text "{color=#000000}%s{/color}" % "尚无记录":
                                                style "slot_name_text"
                            
                            python:
                                slot = slot + 1
                                name_to_save = ""
                                strip = lambda string : string \
                                    if len(string) <= 25 \
                                    else string[: 25] + "……"
                                    
                                if len(_history_list) != 0:
                                    if type(_history_list[-1].who) is NoneType:
                                        name_to_save = strip(_history_list[-1].what)
                                    else: 
                                        name_to_save = (
                                            "【" + _history_list[-1].who + "】 "
                                            + strip(_history_list[-1].what)
                                        )
                                        
                            button:
                                action [
                                    SetVariable("save_name", name_to_save),
                                    FileAction(slot)
                                ]

                                hbox:
                                    spacing 10
                                    if FileTime(slot):
                                        add FileScreenshot(slot) align(0.1, 0.1) zoom 0.6
                                        vbox:
                                            xalign 0.1 yalign 0.1 spacing 10
                                            text "{color=#000000}%s{/color}" % FileTime(slot, format=_("{#file_time}%Y/%m/%d %H:%M")):
                                                style "slot_time_text"
                                            
                                            text FileSaveName(slot):
                                                style "slot_name_text"
                                    else:
                                        image "gui/button/slot_idle_background.png" zoom 0.6
                                        vbox:
                                            text "{color=#000000}%s{/color}" % "尚无记录":
                                                style "slot_name_text"

                                key "save_delete" action FileDelete(slot) 

        ## Buttons to access other pages.
        vbox:
            style_prefix "page"
            hbox:
                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

            # if config.has_sync:
            #     if CurrentScreenName() == "save":
            #         textbutton _("Upload Sync"):
            #             action UploadSync()
            #     else:
            #         textbutton _("Download Sync"):
            #             action DownloadSync()


style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color '#ff8335'

style slot_grid:
    xalign 0.5
    yalign 0.5
    spacing 15

style slot_time_text:
    size 21
    xalign 0.5

style slot_name_text:
    size 21
    xalign 0.5

style slot_vbox:
    spacing 12

style slot_button:
    xysize (slot_x_size, slot_y_size)
    padding (15, 15, 15, 15)
    # background "gui/button/slot_[prefix_]background.png"

style slot_button_text:
    size 21
    xalign 0.5
    idle_color '#aaaaaa'
    hover_color '#ff8335'
    selected_idle_color '#ffffff'

style page_hbox:
    xalign 0.5
    spacing 5

style page_vbox:
    xalign 0.5
    yalign 1.0
    spacing 5

style page_button:
    padding (15, 6, 15, 6)
    xalign 0.5

