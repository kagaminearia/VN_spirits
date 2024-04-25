label chap4_x1:
    mei_speaking "要去睡会吗？"
    peng_speaking "啊？你说我吗？"
    hide meiimg
    show meiimg shirt behind halfblack at char_left
    mei_speaking "嗯。"
    mei "见她面露疑惑，我想了想，还是解释了一下。"
    mei_speaking "你应该没休息好吧，我不打扰你。"
    hide pengimg
    show pengimg shirt eye_care o behind halfblack at char_right 
    peng_speaking "其实……还好。\n不过，如果你这么说的话……"
    hide pengimg
    show pengimg shirt eye_care smile behind halfblack at char_right 
    peng_speaking "那我，现在就睡啦？"
    hide meiimg
    show meiimg shirt o behind halfblack at char_left
    mei_speaking "啊……嗯。"
    hide pengimg with dissolve
    mei "总觉得她这话有些怪怪的……但我还是点了点头。{p}彭江丽似乎有些犹豫，但还是顺应我的话躺下了。"
    mei "我安静地坐在旁边，看着她的呼吸慢慢变得平稳。{p}而后，我小心地重新打开小夜灯，拿在手里，套上外套，从房间里走出去。"
    stop music fadeout 0.5

    scene cg_x40 at cg_0 with fade
    $ renpy.sound.play(sound.wind, channel="nature", loop=True, fadein=0.5)
    mei "不出意外，向夏站在房间外的走廊尽头。{p}她靠在窗边，从我这个角度，只能看到她落在暗处的背影以及窗外那仍不止歇的暴雨。"
    scene cg_x40 at cg_l2 with dissolve
    mei "水珠不断落下的声音和冷风呼啸的声音应该是很吵，我在这个瞬间却只感受到平静和安宁，甚至，有些不忍心打扰她。"
    scene cg_x41 at cg_l2 with dissolve
    xiang_speaking "嗯？"
    mei_speaking "咦？"
    mei "正想着，不远处的人似乎是感受到什么动静。{p}她转过身来，于是我们毫无防备地对上视线。"

    scene bg_meicorridor with fade
    show halfblack
    show xiangimg fist eye_still smile behind halfblack at char_right with dissolve
    $ renpy.music.set_volume(0.5, 0, channel="sound")
    $ renpy.music.set_volume(0.5, 0, channel="nature")
    $ renpy.music.play(music.xiang_rainy_talk, channel="music", loop=True, fadein=0.5, relative_volume=1.5)
    xiang_speaking "嗯嗯……你醒啦？"
    show meiimg behind halfblack at char_left with dissolve
    mei_speaking "……\n啊，嗯。"
    mei "看到我之后，向夏马上换上笑容，好像刚刚的那一瞥只是我的错觉。{p}可我并不如她反应迅速，因而仍然呆呆地站在原地。"
    hide xiangimg
    show xiangimg fist eye_still behind halfblack at char_right
    xiang_speaking "……"
    hide xiangimg
    show xiangimg fist smile behind halfblack at char_right
    xiang_speaking "我记得，你平时好像都睡得挺久的啊，今天怎么醒了？好像没睡多久吧。"
    hide meiimg
    show meiimg behind halfblack at char_left  
    mei_speaking "啊……应该，被吵醒了。"
    hide xiangimg
    show xiangimg fist eye_shock o behind halfblack at char_right
    xiang_speaking "啊？！不会吧，难道我在这也吵到你了？"
    hide meiimg
    show meiimg eye_wacky o behind halfblack at char_left 
    mei_speaking "……哈？"
    hide meiimg
    show meiimg eye_wacky smile behind halfblack at char_left 
    mei_speaking "当然不是，你怎么会这么想。"
    hide meiimg
    show meiimg behind halfblack at char_left 
    mei "虽然没搞懂她的想法，但看到向夏大惊失色的表情，我实在没忍住，笑了出来"
    hide xiangimg
    show xiangimg fist o behind halfblack at char_right
    xiang_speaking "哦，对，也是哦，我脑子糊涂了，哈哈……"
    hide meiimg
    show meiimg o behind halfblack at char_left 
    mei_speaking "所以……？"
    xiang_speaking "我睡觉一半不太安稳，容易吵别人，所以我下意识以为我是跟你睡觉吵了你。"
    hide xiangimg
    show xiangimg fist smile behind halfblack at char_right
    xiang_speaking "那你还这么一脸不开心的样子，我还以为你是被我吵醒，来找我要个说法呢。"
    hide meiimg
    show meiimg behind halfblack at char_left 
    mei_speaking "哦……"
    hide meiimg
    show meiimg o behind halfblack at char_left 
    mei_speaking "没事，是雷声吵。"
    mei_speaking "你不睡觉，是因为这个？"
    xiang_speaking "那倒也没有……\n可能是被鬼故事吓得睡不着吧，嘿嘿。"
    mei_speaking "啊？"
    mei "我没想到她真的害怕到这种程度，现在问完倒是尴尬的不知道说什么了。"
    hide meiimg
    show meiimg eye_still o behind halfblack at char_left 
    mei_speaking "抱歉……嗯，我不知道，会这样。"
    hide xiangimg
    show xiangimg fist eye_still smile behind halfblack at char_right
    xiang_speaking "没事没事啦——我那是随便说的，睡不着不是很正常嘛。"
    hide meiimg
    show meiimg eye_still behind halfblack at char_left 
    mei_speaking "噢……"
    mei "随便说的吗……我简直不知道该露出什么样的表情。{p}但……事实上，我分辨不出来她哪句话是真的，只好将话题停留在此。"
    mei "我们面对面停在原地，一时间也没有更多的对话，只是大眼瞪小眼。"
    hide xiangimg
    show xiangimg fist eye_still behind halfblack at char_right
    xiang_speaking "……"
    hide meiimg
    show meiimg eye_still behind halfblack at char_left 
    mei_speaking "……"

    hide xiangimg
    show xiangimg fist smile behind halfblack at char_right
    xiang_speaking "哦，对了，你站着不累吗？不嫌脏的话，要不过来一起坐这？"
    mei "她拍拍腿，在靠窗的地方直接坐下。{p}我犹豫片刻，也向前两步，提起裙摆平铺在地上。"
    hide meiimg
    show meiimg behind halfblack at char_left
    mei_speaking "要留着灯吗？会不会有点亮。"
    hide xiangimg
    show xiangimg fist o behind halfblack at char_right
    xiang_speaking "啊？看你呗，我无所谓。"
    mei "我的手顿了顿，仍然只是把打开的小夜灯轻轻放在窗台旁边。{p}淡淡的光线在满是雨点的窗玻璃上映出人脸，散发冰冷的气息。"
    stop music fadeout 0.5

    scene bg_black with fade
    show movie_side
    show video_7 behind movie_side
    show halfdarkblue
    $ renpy.music.set_volume(1.0, 0, channel="sound")
    $ renpy.music.set_volume(1.0, 0, channel="nature")
    mei "风声和雨声交叠，落在窗上，在寂静的夜晚声音格外突出。{p}这个时候，是不是该说点什么……我莫名有些失措，下意识朝着向夏的方向转头。"
    mei "向夏没有说话，甚至没有注意到我。{p}她只是望着窗外的方向，十分安静，仿佛整个人彻底消融在夜色和暴雨之中。"
    mei "于是，我终于能够确认，刚到走廊时看到她的那一瞬，并不是幻觉。"
    mei "我忽然后知后觉，平时和向夏聊天的轻松氛围，完全来自于她本身。而如果……{p}如果她没有这种想法，我似乎完全无法接近她。"
    show xiangimg fist eye_still o behind halfdarkblue at char_right with dissolve
    $ renpy.music.play(music.xiang_crush_talk, channel="music", loop=True, fadein=0.5, relative_volume=1.2)
    $ renpy.music.set_volume(0.5, 0, channel="sound")
    $ renpy.music.set_volume(0.5, 0, channel="nature")
    xiang_speaking "怎么了？我脸上现在可没有贴胶带啊。"
    show meiimg eye_still behind halfdarkblue at char_left with dissolve
    mei_speaking "……没。"
    hide xiangimg
    show xiangimg fist eye_still smile behind halfdarkblue at char_right
    xiang_speaking "好吧，看来是我自己想多了。"
    mei "她突然笑了，又变回了平时的向夏。{p}但即使如此，明明那是已经变得熟悉的表情，我却忽然摸不准是什么意思。"
    hide meiimg
    show meiimg o behind halfdarkblue at char_left
    mei_speaking "你……没想多，我刚刚的确，是在看你。"
    mei "不知道为何，我添了这一句毫无必要的话。{p}以至于，向夏似乎都惊讶了一刻。"
    hide xiangimg
    show xiangimg fist o behind halfdarkblue at char_right
    xiang_speaking "……\n哇哦，原来真是你啊。"
    hide xiangimg
    show xiangimg fist smile behind halfdarkblue at char_right
    xiang_speaking "所以你看我干什么？"
    hide meiimg
    show meiimg behind halfdarkblue at char_left
    mei_speaking "呃……"
    mei "前面那句话说的很顺畅，到这句就完全卡壳了。{p}因为我也确实没法解释……"
    xiang_speaking "看我好看？"
    hide meiimg
    show meiimg o behind halfdarkblue at char_left
    mei_speaking "嗯，看你好看。"
    hide xiangimg
    show xiangimg fist eye_still smile behind halfdarkblue at char_right
    xiang_speaking "噗……\n你真有意思。"
    hide meiimg
    show meiimg eye_still smile behind halfdarkblue at char_left
    mei_speaking "是吗。"
    mei "我们都忍不住轻轻笑了。笑这没头没尾的，无厘头的，没人会相信的对话。"
    hide meiimg
    show meiimg eye_close behind halfdarkblue at char_left
    mei "……"
    hide meiimg
    show meiimg behind halfdarkblue at char_left
    mei_speaking "这样，会不会显得，很无聊？"
    hide xiangimg
    show xiangimg fist behind halfdarkblue at char_right
    xiang_speaking "什么意思？"
    hide xiangimg
    show xiangimg fist o behind halfdarkblue at char_right
    xiang_speaking "你是说，坐着、看雨、发呆吗。"
    hide meiimg
    show meiimg o behind halfdarkblue at char_left
    mei_speaking "啊……{p}差不多吧。"
    xiang_speaking "不无聊啊。"
    hide meiimg
    show meiimg behind halfdarkblue at char_left
    mei_speaking "……"
    mei "她的语气斩钉截铁，不像是在说想法，而像是在说一个事实。{p}没来由的，我忽然就觉得心情平静了一些。"
    mei "……还真是奇怪。"
    
    scene bg_black with fade
    show movie_side
    show video_7 behind movie_side
    mei "我尝试舒缓紧绷的身体，扭过头看向窗外。{p}玻璃水雾后，漆黑的幕布里混杂无数透明的水珠，像照片上不和谐的噪点，却似乎让深不可见的黑夜更加深邃。"
    mei "当然，一切都是我的过度联想。{p}但，像这样放空，只是听着雨声和风声，竟然意外地令人感到安宁。"
    mei "明明骤雨和暴风晃动着空气和大地，连窗框都隐隐颤抖，可屋内仍然被屏障挡住一切混乱。\n像风暴中心的平静点，感受周围的一切，却不被侵蚀。"
    mei "余光瞥见与我分享这同一景色的人，我不可抑制地继续遐想。{p}她到底是没睡还是醒了，在这里停留了多长时间，现在……又在想些什么？"
    mei "我认识向夏不久，自然算不上很熟悉。{p}然而，瞥向她毫无起伏的侧脸，我却忽然觉得，今天好像又重新认识了她一次。"
    mei "或许是因为，这一刻的她，比任何时候都让我感到陌生。"
    stop music fadeout 0.5
    stop sound
    stop nature
    $ renpy.music.set_volume(1.0, 0, channel="sound")
    $ renpy.music.set_volume(1.0, 0, channel="nature")
    