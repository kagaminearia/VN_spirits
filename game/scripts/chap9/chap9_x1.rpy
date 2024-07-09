label chap9_x1:
    # nit: delete the first scene here?
    scene bg_meiliv with fade
    $ renpy.music.play(music.slow_laugh, channel="music", loop=True, fadein=0.5,relative_volume=0.7)
    show yeimg smile at char_mid with dissolve
    ye_speaking "梅雨啊梅雨，你现在倒是真的很厉害啊，开始合伙起来骗我了是吧？"
    mei_speaking "……这个……"
    mei "我理亏地低下头，不知道该怎么回复。还好，叶成华只是知道这个计划，不知道别的……"
    mei "想到那难以启齿的“偷窥”，我只觉得脸又像被暴晒之后一样发烫。"
    show luimg laugh at char_left with dissolve
    lu_speaking "哎呀~我都说了是我的想法，小梅她们只是配合我，你别怪她啦~"
    hide yeimg
    show yeimg o at char_mid
    ye_speaking "你也是，你还好意思说，真是的。"
    hide luimg
    show luimg smile at char_left
    lu_speaking "别生气嘛~我可是恢复了哎，你不应该很高兴吗~"
    ye_speaking "是高兴，但是——哼，算了，今天不跟你计较。"
    hide yeimg
    show yeimg smile at char_mid
    ye_speaking "对了，你们怎么这么安静，不喜欢吗？"
    show xiangimg fist eye_still smile red at char_right with dissolve
    xiang_speaking "没有没有，是这顿饭太好吃了，我都只顾着吃饭了，哈哈。"
    mei_speaking "嗯，是啊……"
    hide luimg
    show luimg laugh at char_left
    lu_speaking "我看是被小叶你吓到了吧~"
    hide yeimg
    show yeimg o at char_mid
    ye_speaking "我怎么啦？还有，别叫我小叶！"
    mei_speaking "……"
    stop music fadeout 0.5
    scene bg_meiliv with dissolve
    mei "这两人在干嘛啊……"
    mei "不过，看到话题又被转走，我不动声色地松了口气。"
    mei "谁能想到……回来的路上我和向夏连一句话也没说，甚至完全没有对视，现在却要保持什么也没发生的假象。"
    mei "至少，现在不是只有我一个人如坐针毡……"
    mei "我苦中作乐地用筷子戳着碗里的菜，假装此刻它们是如此有趣，以至于我没有抬头。"

    scene bg_meiroom with fade
    mei "等我回到卧室，我才长长地吐出一口气，终于放下心来。"
    mei "说到底，我到底在心虚什么啊……"
    $ renpy.music.play(music.remember_me_peng, channel="music", loop=True, fadein=0.5,relative_volume=0.8)
    mei "窗帘没有拉紧，我能隐约从窗玻璃上看到自己的倒影，一身白衣，面无表情。"
    mei "简直像鬼一样……那时候，她看到的我也是这样的吗？那她又会怎么想我？她也会……跟我有类似的感受吗？"
    mei_speaking "……"
    mei "算了，胡思乱想什么呢。她怎么想……与我无关。"
    mei "只是……我莫名觉得有些烦闷，思来想去，想不出结果。"
    mei "去楼下拿杯水喝吧，刚好也透透气……"
    stop music fadeout 0.5

    scene bg_black with dissolve
    mei "外面没开灯，很黑，但我倒也习惯了黑暗，于是懒得开灯，慢慢从走廊上摸下去。"
    mei "夜晚很宁静，每一个动作都在我的心里敲上重重的一声。"
    mei "我摸过墙，转弯……摸到一个柔软的东西。"
    stop music
    scene bg_black with vpunchs
    mei_speaking "呃呜？！"
    unknown_speaking "哈啊？！"
    $ renpy.sound.play(sound.table_smash, channel="sound", loop=False)
    scene bg_black with vpunchs
    na "啪！咚！"
    scene bg_meiliv with dissolve
    mei_speaking "……啊……"
    show xiangimg fist eye_shock o at char_mid with dissolve
    mei "灯亮了，我扶着墙从地上站起来，和站在墙边的向夏大眼对小眼。"
    hide xiangimg
    show xiangimg fist eye_shock at char_mid
    mei "她也有些震惊，即使被我看着也没有移开视线，好一会儿才反应过来，微微撇开了头。"
    hide xiangimg
    show xiangimg fist eye_close at char_mid
    xiang_speaking "……"
    mei_speaking "……"
    $ renpy.music.play(music.memory_1, channel="music", loop=True, fadein=0.5)
    hide xiangimg
    show xiangimg fist eye_still o at char_mid
    xiang_speaking "刚刚是不是吓到你了？对不起啊。"
    show xiangimg fist eye_still o at char_c with zoomin
    xiang_speaking "你没事吧？"
    mei "向夏的语气有些着急。而后，她突然在我面前蹲了下来。"
    mei "膝盖处传来柔和的触感，很暖和，却好像冻住了我，让我完全僵在原地。"
    hide xiangimg
    show xiangimg fist eye_still at char_c 
    xiang_speaking "都红了……"
    mei "她的喃喃低语在此时格外清晰，引得我的腿猛地一颤，而后往相反的方向避开。"
    stop music fadeout 0.5
    scene bg_meiliv with vpunchm
    show xiangimg fist eye_still at char_right with dissolve
    xiang_speaking "……"
    $ renpy.music.play(music.memory_1, channel="music", loop=True, fadein=0.5,relative_volume=0.6)
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "我怕你撞伤了，没事就好。"
    mei "向夏飞速地站起身，语气平淡，好像刚才什么事都没发生过。"
    mei "——尽管，我和她都知道，不是这样。"
    show meiimg shirt at char_left with dissolve
    mei_speaking "……"
    xiang_speaking "啊，我先回去睡觉了，需要关灯吗？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "……不用。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "好。那，拜拜。"
    hide xiangimg with moveoutright
    hide meiimg
    show meiimg shirt at char_left
    mei "她笑了笑，而我只是站在原地。不知道过了多久，我慢慢移动脚步，离开客厅。"

    scene bg_meiroom with fade
    $ renpy.sound.play(sound.table_smash, channel="sound", loop=False)
    mei "砰的一声，卧室的门关上，我才感觉自己从那种浓稠的气氛中脱离出来。"
    mei_speaking "哈……"
    $ renpy.music.play(music.time_alone, channel="music", loop=True, fadein=1.0)
    mei "我靠着门滑坐在地上，仔细回想到底是哪里出了错。"
    mei "就在几天前，我们还可以一起爬到天台，交换平时难以启齿的故事。\n现在，连互相对话好像也变得难以启齿。"
    mei "而且，她为什么要那样做……"
    mei "不对，不应该是这样的……"
    mei "也许我就不该在那个地方停留，这样就不会看到突如其来的场景，也不会扰乱自己的心跳，更不会现在不睡觉在这里反复纠结。"
    mei "或者，也许我就不该搭话，不该靠近她，从一开始就……"
    mei "我不明白，这种心情以前从未有过，这让我感到烦闷。"
    stop music fadeout 0.5
    scene bg_black with dissolve
    mei_speaking "唉……"
    mei "我不明白。为什么，你每次都能给我带来意外啊……"
    stop music fadeout 0.5
    return