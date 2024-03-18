image halfblack = "#00000088" 
image halfyellow = "#45342e74" 
image halfdarkblue = "#23243e79" 

image glitches:
    im.MatrixColor("images/glitch0.jpg",im.matrix.brightness(-0.3))
    pause 0.2
    im.MatrixColor("images/glitch1.jpg",im.matrix.brightness(-0.3))
    pause 0.2
    im.MatrixColor("images/glitch2.jpg",im.matrix.brightness(-0.3))
    pause 0.2

    repeat


screen chap_interval(index):
    add "#fff"
    style_prefix 'chap_interval'
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        text "Chapter"
        text "[index]"


style chap_interval_text:
    font "fonts/瑞美加张清平硬笔楷书.ttf"
    size 45
    color gui.light_blue


image video_1 = Movie(play="videos/v1.webm")
image video_2 = Movie(play="videos/v2.webm")

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

