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
        xalign 0.3
        yalign 0.3
        spacing 45
        vbox:
            spacing 18
            vbox:
                text _("剧本·美术·程序") size 35
                text _("可食用蓝墨水") 
            vbox:
                text _("音乐·音效") size 35
                text _("akagi · 可食用蓝墨水") 
            vbox:
                text _("测试") size 35
                text _("akagi · 可食用蓝墨水 · yy") 
            vbox:
                text _("特别感谢") size 35
                text _("HRb · makimeo") 

        vbox:
            spacing 13
            text _("参考·素材·资源") size 35
            text _("游戏引擎：{a=https://www.renpy.org/}Ren'Py{/a}")
            text _("音乐/音效：{a=https://www.FesliyanStudios.com}FesliyanStudios{/a}，\
{a=https://amachamusic.chagasi.com}Amachamusic{/a}，\
{a=https://pixabay.com}Pixabay{/a}") 
            text _("场景素材：{a=https://unsplash.com/}Unsplash{/a}，\
{a=https://www.videvo.net/#rs=videvo-logo}Videvo{/a}，\
{a=https://www.videezy.com/abstract/42744-raindrops-falling-background}Videezy{/a}，\
{a=https://www.freepik.com/}Freepik{/a}，\
{a=https://www.youtube.com/@melvinmellow}melvinmellow{/a}") 
            text _("设计素材：{a=https://siyokoy.itch.io/astrology-renpy-gui-kit}Astrology Ren'Py GUI by Siyokoy{/a}")
            text _("代码参考：{a=https://wattson.itch.io/renpy-wave-shader}Ren'py Wave Shader by Wattson{/a}，\
{a=https://wattson.itch.io/renpy-auto-highlight}Renpy Auto Highlight by Wattson{/a}，\
{a=https://feniksdev.itch.io/easy-renpy-gui}Easy Ren'Py GUI by Feniks{/a}")
            text _("字体：Aboreto，鸿雷板书简体，仓耳舒圆体，霞鹜文楷等宽")

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
    use game_menu(_("Help"))
    style_prefix 'help'
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        hbox:
            text _("剧情前进：")
            text _("鼠标左键/鼠标滚轮下/回车/空格/PgDn")
        hbox:
            text _("剧情回退：")
            text _("PgUp")
        hbox:
            text _("游戏菜单：")
            text _("鼠标右键/Esc")
        hbox:
            text _("返回上页：")
            text _("鼠标右键")
        hbox:
            text _("历史记录：")
            text _("鼠标滚轮上")
        hbox:
            text _("跳过：")
            text _("Ctrl")
        hbox:
            text _("截图：")
            text _("键盘S")
        hbox:
            text _("隐藏界面：")
            text _("键盘H/鼠标中键")


style help_text:
    color gui.dark_grey

# screen help():

#     tag menu
#     default device = "keyboard"
#     # add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever
#     use game_menu(_("Help"))

#     viewport:
#         style_prefix 'game_menu'
#         mousewheel True draggable True pagekeys True
#         scrollbars "vertical"

#         has vbox
#         style_prefix "help"
#         spacing 23

#         hbox:

#             textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
#             textbutton _("Mouse") action SetScreenVariable("device", "mouse")

#             # if GamepadExists():
#             #     textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

#         if device == "keyboard":
#             use keyboard_help
#         elif device == "mouse":
#             use mouse_help
#         # elif device == "gamepad":
#         #     use gamepad_help


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
