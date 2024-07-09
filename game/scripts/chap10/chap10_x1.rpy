label chap10_x1:
    scene bg_store2 with fade
    show meiimg o flower at char_left with dissolve
    $ renpy.music.play(music.peng_hanging_out, channel="music", loop=True, fadein=0.5)
    mei_speaking "好多人……"
    mei "我提着购物袋，只觉得今天排队的人比以往多了很多——连叶成华都经常往村里跑了。"
    show yeimg smile at char_right with moveinright
    ye_speaking "当然，下周就是祝灵节了，基本上还有联系的人都会回来看看的，毕竟这是村里最重要的节日。夸张点的话，就跟过年差不多啊。"
    hide meiimg
    show meiimg flower at char_left
    mei_speaking "这样啊。"
    hide yeimg
    show yeimg o at char_right
    ye_speaking "不习惯吗？"
    hide meiimg
    show meiimg o flower at char_left
    mei_speaking "还好……只是很久没去过这么多人的地方。"
    hide yeimg
    show yeimg smile at char_right
    ye_speaking "我还以为你会很排斥，没想到还可以嘛。"
    mei_speaking "嗯，不会啊，之前是……没什么机会。"
    hide yeimg
    show yeimg laugh at char_right
    ye_speaking "挺好，真挺好的。不管怎么说，看到你这样，我也就不用时不时问你一下，你也不用嫌我烦了。"
    hide meiimg
    show meiimg smile flower at char_left
    mei_speaking "……是啊。"
    mei "好像，还真的比以前好多了……某种程度上，还真是多亏了叶成华……还有……她。"
    stop music fadeout 0.5

    scene bg_meiroom with fade
    mei "时间很快，在意识到的时候尤其如此。现在，我穿着外套，已经隐隐觉得有些热。"
    mei "有些喧闹的声音从窗外传来，我偏过头，看到有几个小孩打闹着跑过楼底下，伴随着越来越明显的音乐声。"
    $ renpy.music.play(music.festival, channel="music", loop=True, relative_volume=0.3, fadein=0.5)
    $ renpy.sound.play(sound.chinese_beat, channel="sound", loop=True, relative_volume=0.2, fadein=0.5)
    mei "这样可没办法专心啊……干脆，也去看看好了，毕竟是一年一度的节日。"
    mei "祝灵节……在这一天，空闲的人们集合起来，放上传统音乐，点上特制的香薰，围在广场上唱歌跳舞。"
    mei "在日落的瞬间，所有人会点亮火灯，念唱祝歌，祝愿所有的生灵平安幸福。"
    mei "在那之后，如果对着天空许愿，据说……就能短暂地见到最想见的人。"
    mei "说起来好像，她当时，似乎就是为了这个节日来的。"
    mei_speaking "……"
    mei "不过，我没有强烈的信仰，不在乎这些是真是假，也没有什么想见的人。不过，像这样在某种节日下许下愿望的感觉……我并不讨厌。"
    mei "我放下手中的笔，悠悠地朝人多的方向走去。"
    scene bg_black with Dissolve(1)
    show movie_side
    show video_10 behind movie_side with dissolve
    mei "广场的正中央已经点上篝火，隐约能听到周围空气撕裂的噼啪响声。因为还没到日落的时间，周围的人只是三三两两，想跳舞的跳，不想的站在旁边谈笑风生。"
    mei "我记得向夏好像说过，她是为了这个节日才留在这里……也不知道她会不会害怕这些篝火。\n想到这里，我无奈地叹了口气，也不知道是为谁而叹。"
    mei "太阳逐渐西斜，越来越低，周围也逐渐聚起越来越多的人。\n不知道什么时候，我被四周围在一起的人们簇拥着，靠近中心。"
    mei_speaking "啊……\n我不会唱歌啊。"
    unknown_speaking "没事儿，我跟你说啊，你站在这跟着哼哼就行！别害羞！"
    mei_speaking "……\n噢。"
    mei "我原本只是在自言自语，却被旁边热情的阿姨“科普”一番。\n反正现在也走不出去了……就这样吧。"
    mei "……当然，我是不会唱歌的，哼哼也不会。"
    stop music
    stop sound
    # nit: change the scene here?
    scene halfblack with Fade(0.3,0.5,0.3)
    mei "人群逐渐密集，直到我看不到边沿。周围的人双手相交，盯着远处空旷的天际。\n被这样的气氛带动，我也不自觉地合起了双手。"
    mei "终于，那橘黄色的耀眼光芒只剩一缕，马上就要彻底消失。不知道谁起了头，所有人呢喃起我不知名字的歌。"
    $ renpy.music.play(music.worship, channel="music", loop=True, fadein=0.5)
    mei "不同的低语声汇在一起，变得浑厚明亮，形成汹涌的海洋，而我也被卷入其中。"
    na "祝愿吧，祝愿所有的生灵，都获得幸福。"
    na "祝愿……"
    mei "不知道是不是我的错觉，原本在我的位置应该已经看不见的，远处的火堆突然爆发出巨大的光芒。"
    mei "星星点点的微小光晕漂浮在空中，火光摇曳，撼动我的心神。"
    mei "奇迹……吗。我的脑海中不自觉浮现出许多记忆，在这里生活的日子，那些事情……"
    mei "……无论，这是不是真实的，此时此刻，我真心地想要相信……个人的意志能够带来奇迹。"
    stop music fadeout 0.5

    scene bg_black with dissolve
    show movie_side
    show bg_sunset1 behind movie_side with dissolve
    mei "天色渐晚，人群逐渐散开，周围的环境由篝火变为由夕阳染成的淡淡橙红。"
    $ renpy.music.play(music.xiang_coming_back, channel="music", loop=True, fadein=0.5)
    mei_speaking "……阿嚏！"
    mei "冷风吹过，我终于回过神。因为篝火已经基本散去，我成功被冷得直打哆嗦。"
    mei_speaking "阿嚏！\n呃啊……嗯？"
    show xiangimg eye_still o at char_right with dissolve
    xiang_speaking "要衣服吗？"
    show meiimg shirt at char_left with dissolve
    mei_speaking "……"
    show halfblack with dissolve
    mei "我没想过转身会看到她。"
    mei "事实上，在那天之后，我没有再见过向夏，我甚至以为她已经离开这里了。"
    mei "但是没有，她还是像之前所说的那样……也许，刚刚正与我见证了同一个时刻。"
    mei "她出现在这里，还主动找上了我。"
    hide halfblack with dissolve
    xiang_speaking "……要衣服吗？"
    return