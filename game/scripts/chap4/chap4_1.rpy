label chap4_1:
    stop music fadeout 0.5
    scene bg_black with fade
    mei "事情并没有朝我期望的方向发展。{p}不过，这也正常，我早就习惯这种感觉了。习惯期望落空的感觉。"
    show movie_side
    show video_6 behind movie_side with dissolve
    $ renpy.sound.play(sound.thunder, channel="nature", loop=False)
    $ renpy.sound.play(sound.rain_on_window, channel="sound", loop=True)
    mei "我是被突然的响声吵醒的，像震天的爆炸在耳边炸开，惊得我下意识打了个寒颤。{p}睁开眼，才发现是瞬间迸发的闪电。"
    na "轰隆！！"
    mei_speaking "啊……噫！"
    mei "我还没回过神，又是一声巨响。{p}刺眼的白光闪烁，照亮了整个房间，一瞬亮如白昼，而后又再次归于黑暗。"

    scene bg_emptyroom with fade
    show halfblack
    show pengimg shirt o behind halfblack at char_right with dissolve
    peng_speaking "你醒了？"
    show meiimg shirt eye_shock o behind halfblack at char_left with dissolve
    mei_speaking "诶？！"
    hide meiimg
    show meiimg shirt behind halfblack at char_left
    $ renpy.music.play(music.calming_piano, channel="music", loop=True, fadein=0.5)
    mei "我揉揉眼睛，重新适应黑暗后才发现彭江丽醒着。她已经坐起来，正定定地看着我。{p}而另一边，原本是向夏睡的地方却空了出来。"
    hide meiimg
    show meiimg shirt o behind halfblack at char_left
    mei_speaking "……她呢？"
    hide pengimg
    show pengimg shirt eye_care o behind halfblack at char_right 
    peng_speaking "什么？哦，你说……向夏？她好像之前出去了。\n你怎么醒了，是不是有哪里不舒服？"
    mei_speaking "没，我是自然醒。几点了？"
    hide pengimg
    show pengimg shirt o behind halfblack at char_right 
    peng_speaking "不知道，之前问是四点，现在可能四点半吧。"
    mei "果然还很早，难怪会感觉有点头晕……{p}不过，她们这是都没睡吗……"
    
