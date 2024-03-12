
define chap_index = 0
label start:

    call prologue
    $ chap_index = 1
    # waiting for opening video
    window hide
    show screen chap_interval(chap_index) with Fade(0.5,0.5,0.5)
    pause

    return


