label ad:
    window hide
    $ quick_menu = False
    scene bg_black
    pause 1
    show ink at cg_s with dissolve
    pause 0.7
    hide ink at cg_s with dissolve

    scene video_m
    # show ad_bg_pink
    show meiimg shirt at ad_l with easeinleft
    pause 
    hide meiimg
    show m_bg with Dissolve(0.1) 
    show meiimg shirt o at ad_s with dissolve
    pause
    show m_4 with dissolve
    pause 
    
    scene bg_meikitc with dissolve
    show meiimg shirt at char_mid 
    mei_speaking "哦，没事。"
    scene bg_meiroom with dissolve
    show meiimg shirt eye_still at char_mid 
    mei_speaking "嗯，对不起……"
    scene bg_meiliv with dissolve
    show meiimg shirt eye_wacky at char_mid 
    mei_speaking "……你在干嘛？"
    scene bg_vil6 with dissolve
    show meiimg shirt o at char_mid 
    mei_speaking "我只是想找机会跟你说话。"


    scene video_x with dissolve
    # show ad_bg_pink
    show xiangimg fist at ad_l with easeinleft
    pause 
    hide xiangimg
    show x_bg with Dissolve(0.1) 
    show xiangimg fist smile at ad_s with dissolve
    pause
    show x_4 with dissolve
    pause 

    scene bg_station with dissolve
    show xiangimg o at char_mid
    xiang_speaking "可以帮我问一下吗？"
    scene bg_meiliv with dissolve
    show xiangimg fist eye_squint smile at char_mid
    xiang_speaking "其实，我是个很信鬼神的人哦。"
    scene bg_vil6 with dissolve
    show xiangimg fist smile at char_mid
    xiang_speaking "嗯？我没生气啊。"
    scene bg_emptyroom with fade
    show halfdarkblue
    show xiangimg fist eye_close laugh behind halfdarkblue at char_mid
    xiang_speaking "你们倒是互相关心，合着只有我当恶人。"

    scene video_p with dissolve
    show pengimg at ad_l with easeinleft
    pause 
    hide pengimg
    show p_bg with Dissolve(0.1) 
    show pengimg laugh at ad_s with dissolve
    pause
    show p_4 with dissolve
    pause 

    scene bg_vil6 with dissolve 
    show pengimg laugh at char_mid
    peng_speaking "嗯，好像是快八年了吧，没想到……"
    scene bg_vil3 with dissolve 
    show pengimg smile at char_mid
    peng_speaking "就是，嗯……关于我跟你——"
    scene bg_pengliv with dissolve 
    show pengimg shirt eye_still at char_mid
    peng_speaking "因为，我真的好担心。"
    scene bg_meihome with dissolve
    show pengimg at char_mid
    peng_speaking "所以，你们已经这么熟悉了吗？"

    return

transform ad_l:
    zoom 0.8
    yalign 0.1
    xalign 0.5

transform ad_s:
    zoom 0.45
    yalign 0.1 
    xalign 0.5
    xoffset -250
    yoffset 120

image video_m= Movie(play="videos/ad/ad_bg_blue.webm")

image video_p= Movie(play="videos/ad/ad_bg_yellow.webm")

image video_x= Movie(play="videos/ad/ad_bg_pink.webm")

screen text(inp):
    style_prefix 'tt'
    vbox:
        xalign 0.5
        yalign 0.5
        text "[inp]"

style tt_text:
    font "fonts/瑞美加张清平硬笔楷书.ttf"
    size 45
    color gui.dark_grey
