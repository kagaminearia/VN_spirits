label chap8_x1:
    scene bg_station with fade
    $ renpy.sound.play(sound.stressed, channel="sound", loop=True, fadein=0.5)
    mei "太阳高悬，带来持续的暑气。地面的温度仿佛顺着鞋底传至躯体，漂浮着灰尘的空气也仿佛被微微扭曲。"
    mei "时间过得真快啊……刚来的时候还没有这么热的。"
    mei "还要多久……也许是被气温影响，我难得变得有些焦躁起来，不断地来回查阅车票和手机上的时间。"
    show xiangimg o at char_right with dissolve
    $ renpy.music.play(music.xiang_awkward_talk, channel="music", loop=True, fadein=0.5)
    xiang_speaking "应该还要五分钟吧。"
    stop sound fadeout 0.5
    show meiimg shirt at char_left with dissolve
    mei_speaking "啊？哦……你怎么知道我在看时间。"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "这不是很明显吗？你都翻了好多遍了。别担心啦。"
    hide meiimg
    show meiimg shirt eye_close at char_left
    mei_speaking "好吧……"
    hide xiangimg
    show xiangimg laugh at char_right
    xiang_speaking "今天还真是谢谢你啰，如果不是你，我都没办法坐车。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei "我无语地叹气，只觉得身上好像更闷热了。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "你为什么直接把证件给叶成华了啊。"
    mei "是了，要不是这边的大巴车查票不严，今天她根本没法跟我去镇上。"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "这不是想让她相信我吗？我可是要住到你家里诶，很危险的。"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left
    mei_speaking "……给证件不危险吗。"
    hide xiangimg
    show xiangimg eye_squint smile at char_right
    xiang_speaking "哎呀，这个……因为，她看起来不像坏人啊。要是赌错了，也没办法啰。"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "以前我打工，只能找不正规的地方，他们那些地方都是要押证件的，所以我习惯了嘛。"
    mei "向夏似是很无奈，夸张地耸了耸肩膀，带着衣服上的蝴蝶结一颤一颤。"
    hide meiimg
    show meiimg shirt eye_wacky at char_left
    mei_speaking "……"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "你怎么了？我不是跟你解释了吗，还生气啊？"
    hide meiimg
    show meiimg shirt eye_close at char_left
    mei_speaking "……没有。"
    mei "就是说啊，再怎么说这也是她的事情，我有什么好生气的，纠结个什么劲啊。\n只是，莫名有种憋闷的感觉……"
    mei "肯定是因为今天太热了。"
    stop music fadeout 0.5

    scene bg_black with dissolve
    show movie_side
    show video_9 behind movie_side with dissolve
    mei "大巴一路颠簸，晃晃悠悠地开了一个多小时。"
    hide video_9 with dissolve
    $ renpy.music.play(music.calming_guitar, channel="music", loop=True, fadein=0.5)
    mei "到站后，我赶紧提着袋子从车上跳下来，只觉得车外的热风也变得清爽。"
    mei "我实在不喜欢乘坐交通工具，尤其是这样满员的老旧公交。今天会到镇上，也是为了帮叶成华一个忙。"
    mei "之前给她添这么多麻烦，现在有个机会帮她，我自然是要答应。"

    scene bg_station2 with dissolve
    show meiimg shirt eye_close o at char_left with dissolve
    mei_speaking "呼……"
    show xiangimg o at char_right with dissolve
    xiang_speaking "哇，你竟然没晕倒，我都准备扶你了。"
    show meiimg shirt at char_left
    mei_speaking "……走吧。"
    mei "我懒得跟向夏斗嘴，只是重新核对笔记，确认我们没坐过站。"
    mei "不过……其实我不是很明白她今天为什么要跟过来。\n就算要拿回证件，我帮她带回去就行了。"
    mei "搞不懂她……"

    scene bg_ground2 with fade
    show xiangimg o at char_right with moveinright
    xiang_speaking "就是那边吧，喏，人好多啊。"
    show meiimg shirt at char_left with moveinleft
    mei_speaking "嗯，应该是……"
    mei "医院的几栋高楼在这一片建筑中鹤立鸡群，门口处是来来往往的人流，吵吵嚷嚷。\n嗯，实在是令人感到不快的场景……"
    xiang_speaking "那个谁……你姐姐的女朋友，在哪里啊？"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "她今天来医院复诊，然后结束治疗。我刚刚发消息问她，她说现在在二号楼，应该在……"
    xiang_speaking "那边吧，你看地图。"
    mei "向夏指了指竖在路边的巨大标牌，我点点头，往那个方向走去。"

    scene bg_clinic1 with fade
    show luimg o at char_right with moveinright
    lu_speaking "哟，还搞这么花里胡哨的呢。"
    mei "路花看到我从袋子里掏出一捧花束，十分惊讶的瞪大了眼睛。"
    hide luimg
    show luimg smile at char_right
    lu_speaking "小梅呀，我没想到你还真的过来一趟，真是太麻烦了。"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "没事，是叶成华说，她今天抽不出空，所以让我帮忙。"
    mei "我指了指花束上夹着的卡片，上面写着“恭喜”。"
    lu_speaking "这些我知道呀，但是就是办个手续，也没必要吧？真是的，就会使唤你做事，咱下次不听她的，啊。"
    mei_speaking "叶成华说，你终于结束治疗，应该给你庆祝一下，她没时间，但是要端正态度，至少让我过来陪你一下。"
    lu_speaking "这话说得，还端正态度，我是她领导吗？小梅你也太乖了吧，哈哈哈，除了叶成华的话，你自己没有什么想说的吗？"
    hide meiimg
    show meiimg shirt eye_close at char_left
    mei "嗯……看着她好奇的眼神，我分神思考了一瞬，然后尽量诚恳地回答。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "没有。"
    hide luimg
    show luimg laugh at char_right
    lu_speaking "噗，哈哈哈哈。真可爱，行啦，真是辛苦你了，这大老远跑过来就为了给我送个花。"
    mei_speaking "叶成华说……"
    hide luimg
    show luimg smile at char_right
    lu_speaking "好了，别说啦别说啦，你是成华牌复读机吗？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"

    scene bg_clinic1 with pixellate
    show luimg laugh at char_right with dissolve
    lu_speaking "不过，感觉你最近状态好很多呀~"
    show meiimg shirt at char_left with dissolve
    mei_speaking "嗯，是吗？还行……"
    lu_speaking "你都能收拾成华的烂摊子了呀，挺好挺好~"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "也不是……是我给她添麻烦。"
    hide luimg
    show luimg smile at char_right
    lu_speaking "你怎么会这么想？是她擅自干涉你的对吧？会觉得排斥也是人之常情嘛。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei "说起来，刚开始的时候，也许我真的是这么想的。但是现在，现在的话……"
    lu_speaking "不过既然你现在觉得还行，我能不能，也麻烦你帮我个小忙呀~"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "啊？我能帮到什么吗……？"
    hide luimg
    show luimg laugh at char_right
    lu_speaking "你能做的事可多了，肯定可以啊~只是看你愿不愿意。你先听听看吧？不愿意也没事啦。"
    mei_speaking "噢，好。"
    lu_speaking "是这样的，你看，我的腿不是彻底好了嘛，所以我想给小叶一个惊喜。到时候，你能不能帮我把她骗到立涧村北边的那片花田去啊~"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "诶……"
    mei "我没想到她说的帮忙是指这个。不过仔细想想，也很合理，毕竟我也帮不了什么事，也就这种……"
    mei "叶成华应该会很高兴吧……我不禁也替她们感到高兴。"
    mei "当然，还有些隐约的羡慕。她们总是在想着对方，真好。"
    mei "不过现在我倒不该纠结这些，而是……"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "我演技很差的，不太行吧？"
    hide luimg
    show luimg o at char_right
    lu_speaking "诶~是这样吗？不用担心哦。"
    lu_speaking "但是，那也就是说，除了这方面的顾虑，你其实愿意帮忙？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "算是吧……"
    hide luimg
    show luimg laugh at char_right
    lu_speaking "那，我来想个计划，然后你照着做就行，怎么样？"
    mei_speaking "啊？是不是有点……太麻烦了？"
    hide luimg
    show luimg smile at char_right
    lu_speaking "不会不会~我会弄个很适合你的剧情的，绝对很简单哦~本色出演！"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei_speaking "……好吧。"
    mei "我倒是没有不愿意，如果她觉得我行，也没什么不可以的。"
    mei "只是……我也着实佩服她的脑回路。\n只能说，路花不愧是叶成华的女朋友。"
    stop music fadeout 0.5

    scene bg_clinic1 with pixellate
    show luimg smile at char_right with dissolve
    $ renpy.sound.play(sound.cicada, channel="sound", loop=True, fadein=0.5, relative_volume=0.1)
    lu_speaking "好啦，那你今天还有什么安排？你应该是下午的车回去吧。"
    show meiimg shirt at char_left with dissolve
    mei_speaking "嗯。"
    hide luimg
    show luimg o at char_right
    hide meiimg
    show meiimg shirt o at char_left 
    lu_speaking "没安排啊？那要不……"
    mei_speaking "啊，不，那个，我和……"
    mei "我推脱的话脱口而出，却说到一半自己卡壳。\n……该怎么说？怎么描述？她到底是……？"
    mei "顿了顿，我决定直接换一个说法。"
    mei_speaking "你记得向夏吗，之前一起吃饭的时候，那个卷发的人。"
    hide luimg
    show luimg smile at char_right
    lu_speaking "噢，当然，挺开朗的小孩，她怎么了？"
    mei_speaking "就是，我今天跟向夏一起来的，所以……"
    hide luimg
    show luimg o at char_right
    lu_speaking "这样啊，那她人呢，怎么不进来？"
    mei_speaking "她在外面等。"
    lu_speaking "这多不好呀？"
    lu_speaking "好吧好吧，我知道了，你们是觉得不熟尴尬是吧。我不强留你了，不过好不容易过来一次，可以趁这个机会在周边转转。"
    lu_speaking "这个给你拿着！"
    hide meiimg
    show meiimg shirt eye_shock o at char_left 
    mei_speaking "啊？不用，我——"
    stop sound fadeout 0.5
    return
