transform char_mid:
    zoom 0.5
    xalign 0.5
    yalign 0.1
    yoffset 80

transform char_right:
    zoom 0.5
    xalign 1.0
    yalign 0.1
    yoffset 80
    xoffset 100

transform char_left:
    zoom 0.5
    xalign 0.0
    yalign 0.1
    yoffset 80
    xoffset -100

transform char_c:
    zoom 0.7
    xalign 0.5
    yalign 0.1
    yoffset 100


transform cg_0:
    zoom 0.5
    xalign 0.5
    yalign 0.5

transform cg_s:
    zoom 0.4
    xalign 0.5
    yalign 0.35

transform cg_l1:
    xalign 0.5
    yalign 0.1

transform cg_l2:
    xalign 0.5
    yalign 0.2


transform cg_1:
    xalign 0.5
    yalign 0.5


init python:
    # change punch variable
    hpunch = Move((30, 0), (-30, 0), .50, bounce=True, repeat=True, delay=.275)
    vpunchs = Move((0, 10), (0, -10), 0.5, bounce=True, repeat=True, delay=.275)
    vpunchm = Move((0, 40), (0, -40), 0.8, bounce=True, repeat=True, delay=.275)
    shake = Move((70, 70), (-70, -70), 3, bounce=True, repeat=True, delay=.275)


transform shaking:
    linear 0.1 xoffset -2 yoffset 2 
    linear 0.1 xoffset 3 yoffset -3 
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0
    repeat

transform shakeonce:
    linear 0.1 xoffset -2 yoffset 2 
    linear 0.1 xoffset 3 yoffset -3 
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -2 yoffset 2 
    linear 0.1 xoffset 3 yoffset -3 
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0

transform blink:
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat