
define chap_index = 0
define p_point = 0
define x_point = 0

label start:

    window hide
    show screen chap_interval(chap_index) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto

    call prologue

    $ chap_index = 1
    $ quick_menu = False
    window hide
    scene bg_black with Dissolve(0.4)
    show intro with fade
    pause
    show screen chap_interval(chap_index) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    $ quick_menu = True
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

    call chapter3

    $ chap_index = 4
    window hide
    show bg_black with dissolve
    show screen chap_interval(chap_index) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto
    
    call chapter4

    $ chap_index = 5
    window hide
    show bg_black with dissolve
    show screen chap_interval(chap_index) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto
    
    call chapter5

    $ chap_index = 6
    window hide
    show bg_black with dissolve
    show screen chap_interval(chap_index,route) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto
    
    call chapter6 

    $ chap_index = 7
    window hide
    show bg_black with dissolve
    show screen chap_interval(chap_index,route) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto

    call chapter7

    $ chap_index = 8
    window hide
    show bg_black with dissolve
    show screen chap_interval(chap_index,route) with Fade(0.5,1,0.5)
    pause 4
    hide screen chap_interval with fade
    window auto
    
    return


