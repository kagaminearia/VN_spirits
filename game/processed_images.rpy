image halfblack = "#00000088" 
image halfyellow = "#45342e74" 
image halfdarkblue = "#23243e79" 
image halfwhite = "#ffffff88" 
image bg_white = "#fff"

image glitches:
    im.MatrixColor("images/glitch0.jpg",im.matrix.brightness(-0.3))
    pause 0.2
    im.MatrixColor("images/glitch1.jpg",im.matrix.brightness(-0.3))
    pause 0.2
    im.MatrixColor("images/glitch2.jpg",im.matrix.brightness(-0.3))
    pause 0.2

    repeat


screen chap_interval(index,route="n"):
    add "#fff"
    style_prefix 'chap_interval'
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            text "Chapter"
            text "[index]"
        hbox:
            if index<6:
                text c_title[index] size 40
            else:
                if route == "p":
                    text p_title[index-6] size 40
                else:
                    text x_title[index-6] size 40


style chap_interval_text:
    font "fonts/HongLeiBanShuJianTi.ttf"
    size 55
    color gui.light_blue


screen endings_screen(route="n"):
    add "#fff"
    

image intro = Movie(play="videos/intro.webm",loop=False)
image video_1 = Movie(play="videos/v1.webm")
image video_2 = Movie(play="videos/v2.webm")
image video_3 = Movie(play="videos/v3.webm")
image video_4 = Movie(play="videos/v4.webm",loop=False)
image video_5 = Movie(play="videos/v5.webm")
image video_6 = Movie(play="videos/v6.webm")
image video_7 = Movie(play="videos/v7.webm")
image video_8 = Movie(play="videos/v8.webm")

image raindrop:
    "images/rain1.webp"
    pause 0.2
    "images/rain2.webp"
    pause 0.2
    "images/rain3.webp"
    pause 0.2
    "images/rain4.webp"
    pause 0.2
    "images/rain5.webp"
    pause 0.2
    repeat

