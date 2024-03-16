
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    # add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Preferences"))

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 50
        hbox:
            box_wrap True

            if renpy.variant("pc") or renpy.variant("web"):
                # Only need fullscreen/windowed on desktop and web builds

                vbox:
                    style_prefix "radio"
                    label _("屏幕显示")
                    textbutton _("窗口"):
                        # Ensures this button is selected when
                        # not in fullscreen.
                        selected not preferences.fullscreen
                        action Preference("display", "window")
                    textbutton _("全屏"):
                        action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                label _("跳过")
                textbutton _("未读文本"):
                    action Preference("skip", "toggle")
                textbutton _("在选项后继续"):
                    action Preference("after choices", "toggle")
                textbutton _("转场"):
                    action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.


        hbox:
            style_prefix "slider"
            box_wrap True

            vbox:

                label _("文字速度")
                bar value Preference("text speed")

                label _("自动文字速度")
                bar value Preference("auto-forward time")

            vbox:

                if config.has_music:
                    label _("音乐音量")
                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:
                    label _("音效音量")
                    hbox:
                        bar value Preference("sound volume")
                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    label _("声音音量")
                    hbox:
                        bar value Preference("voice volume")
                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height 15
                    textbutton _("全部静音"):
                        style_prefix "check"
                        action Preference("all mute", "toggle")

### PREF
style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    color gui.dark_grey
    hover_color gui.light_grey

style radio_vbox:
    is pref_vbox
    spacing 0

style radio_button:
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (35, 6, 6, 6)

## CHECK
style check_label:
    is pref_label
style check_label_text:
    # is pref_label_text
    color gui.dark_grey

style check_vbox:
    is pref_vbox
    spacing 0

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding (35, 6, 6, 6)

## SLIDER
style slider_label:
    is pref_label

style slider_label_text:
    # is pref_label_text
    color gui.dark_grey

style slider_slider:
    xsize 525

style slider_button:
    yalign 0.5
    left_margin 15

style slider_vbox:
    is pref_vbox
    xsize 675

