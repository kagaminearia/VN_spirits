label chap1_2:
    scene bg_store1 with pixellate
    $ renpy.sound.play(sound.buzz, channel="sound", relative_volume=0.3, fadein=0.5)
    mei "白黄色的灯泡偶尔闪烁，似乎隐约有微小的滋啦声响从头顶传来。\n也许是因为超市里的人少，这些动静显得格外明显。"
    mei "我摇摇头，把注意转移到眼前的货架上。除了人少，面积不大，这里和其他超市没有什么区别。"
    stop sound fadeout 0.5
