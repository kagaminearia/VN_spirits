
define chap_index = 0
define p_point = 0
define x_point = 0

label start:

    call prologue

    $ chap_index = 1
    # waiting for opening video
    window hide
    show bg_black with dissolve
    show screen chap_interval(chap_index) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto

    call chapter1

    $ chap_index = 2
    window hide
    show bg_black with dissolve
    show screen chap_interval(chap_index) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto
    
    call chapter2

    $ chap_index = 3
    window hide
    show bg_black with dissolve
    show screen chap_interval(chap_index) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto
    return


