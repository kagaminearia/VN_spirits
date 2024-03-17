## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    tag menu
    use game_menu(_("About"))
    style_prefix 'about'
    vbox:
        xalign 0.25
        yalign 0.25
        spacing 45
        vbox:
            spacing 18
            vbox:
                text _("剧本·美术·程序") size 35
                text _("可食用蓝墨水") 
            vbox:
                text _("音乐·音效") size 35
                text _("akagi · 可食用蓝墨水") 
            # vbox:
            #     text _("测试") size 40
            #     text _("akagi · HydrogenRb · 可食用蓝墨水 · makimeo") 
            vbox:
                text _("特别感谢") size 35
                text _("akagi") 

        vbox:
            spacing 13
            text _("参考·素材·资源") size 35
            text _("游戏引擎：{a=https://www.renpy.org/}Ren'Py{/a}")
            text _("音乐：{a=https://www.FesliyanStudios.com}FesliyanStudios{/a}，{a=https://amachamusic.chagasi.com}Amachamusic{/a}，{a=https://pixabay.com}Pixabay{/a}") 
            text _("音效：{a=https://pixabay.com}Pixabay{/a}") 
            text _("场景图片：{a=https://unsplash.com/}Unsplash{/a}") 
            text _("图形素材：{a=https://siyokoy.itch.io/astrology-renpy-gui-kit}Astrology Ren'Py GUI{/a} by Siyokoy")
            text _("视频素材：{a=https://www.videvo.net/#rs=videvo-logo}Videvo{/a}")
            text _("代码·水波效果：{a=https://wattson.itch.io/renpy-wave-shader}Ren'py Wave Shader{/a} by Wattson")
            text _("代码·立绘强调：{a=https://wattson.itch.io/renpy-auto-highlight}Renpy Auto Highlight{/a} by Wattson")
            text _("代码·界面模板：{a=https://feniksdev.itch.io/easy-renpy-gui}Easy Ren'Py GUI{/a} by Feniks")
            
style about_label_text:
    size 35

style about_text:
    font gui.interface_text_font
    size 25
    color gui.dark_grey

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu
    default device = "keyboard"
    # add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever
    use game_menu(_("Help"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "help"
        spacing 23

        hbox:

            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            # if GamepadExists():
            #     textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        # elif device == "gamepad":
        #     use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


# screen gamepad_help():

#     hbox:
#         label _("Right Trigger\nA/Bottom Button")
#         text _("Advances dialogue and activates the interface.")

#     hbox:
#         label _("Left Trigger\nLeft Shoulder")
#         text _("Rolls back to earlier dialogue.")

#     hbox:
#         label _("Right Shoulder")
#         text _("Rolls forward to later dialogue.")


#     hbox:
#         label _("D-Pad, Sticks")
#         text _("Navigate the interface.")

#     hbox:
#         label _("Start, Guide, B/Right Button")
#         text _("Accesses the game menu.")

#     hbox:
#         label _("Y/Top Button")
#         text _("Hides the user interface.")

#     textbutton _("Calibrate") action GamepadCalibrate()


style help_button:
    xmargin 12

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    xalign 1.0
    textalign 1.0
