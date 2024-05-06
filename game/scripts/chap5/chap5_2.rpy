label chap5_2:
    $ renpy.music.play(music.prologue_ending, channel="music", loop=True, fadein=0.5)
    scene bg_meiroom with fade
    show halfblack

    mei "吃完药，我躺在床上，用力用被子裹住自己，仿佛这样就能让自己多一分安心感。"
    mei "白天的事情让我有些提不起劲，回顾一遍，心情就像过山车从高处落到谷底。"
    mei "好像……我做什么都是错的。{p}那次之后，不管做什么事都与期望背道而驰，也许都是因为我……"
    mei "好想逃走。什么都不想管了。好想离开这里……"
    mei "但是，但是……我已经自己过表明态度了，是我自己想要留在这里的。\n现在，我不能再反悔……"
    mei "再待一段时间吧，反正我也无处可去……"
    stop music fadeout 0.5
    stop others fadeout 0.5

    scene bg_meiroom with pixellate
    show yeimg at char_right with moveinright
    $ renpy.music.play(music.time_alone_2, channel="music", loop=True, fadein=0.5, relative_volume=1.2)
    $ renpy.sound.play(sound.bird_chirping_1, channel="nature", loop=False)
    ye_speaking "几天没见，你最近有没有好一点啊？看起来还可以？"
    show meiimg shirt at char_left with moveinleft
    mei_speaking "有吗。"
    ye_speaking "嗯，你自己觉得呢？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "……{p}一点都不好。"
    hide meiimg
    show meiimg shirt eye_still o at char_left
    mei_speaking "感觉，还是跟以前没有区别。{p}做什么都不对，不知道该做什么，还……"
    mei "我忽然不想继续说下去。但这没来由的所谓的自尊毫无意义。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "还会被认为，是没用的人。也会，一直给别人添麻烦。"
    hide yeimg
    show yeimg smile at char_right
    ye_speaking "我不这么认为哦。"
    mei "意外又没那么意外的，叶成华仍然保持着淡淡的笑容，声音平静而温和。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "你只是这么说而已……因为你也觉得我是——"
    ye_speaking "你现在都愿意说这么多话了。"
    hide meiimg
    stop music fadeout 0.5
    $ renpy.sound.play(sound.wave, channel="sound", loop=False)
    show meiimg shirt at char_left
    mei_speaking "……啊？"
    mei "我将要说出口的话堪堪止住，变成一个有些滑稽的声音。"
    ye_speaking "虽然我是不想提这个的……不过，刚见到你那会儿，你就像个雕塑似的，什么反应也没有。{p}现在嘛，至少有点儿人气了不是？"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "……"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "是，是这样吗……"
    mei "听她这么说，我又觉得好像也有道理。可是……"
    ye_speaking "慢慢来嘛，不要着急。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "嗯……"
    stop sound fadeout 0.5
    stop nature

    scene bg_meiroom with vpunchs
    mei "在我纠结的时候，房门再度发出声响，顿时，我的手臂和肩膀全部紧缩了起来。"
    show yeimg at char_mid with dissolve
    ye_speaking "别紧张，不是坏人。"
    show meiimg shirt at char_left with dissolve
    mei_speaking "……"
    show luimg at char_right with moveinright
    $ renpy.music.play(music.calming_guitar, channel="music", loop=True, fadein=0.5)
    unknown_speaking "哈喽哈喽。\n你好啊~我是路花。"
    mei "诶，是她？我不免有些惊讶地看过去。{p}虽然没见过，但由于某个人的炫耀行为，实际上，我还算了解，甚至熟悉这个名字……"
    mei "路花，叶成华的女朋友，之前出了车祸，最近正在做康复训练，现在已经可以下地走路了……"
    mei "我赶紧站直身体，有些僵硬地打招呼。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "呃，你好。你……"
    lu_speaking "没事没事~我就是来陪你姐姐的，不用在意我~"
    ye_speaking "是啊，感觉很久没跟你吃饭了，正好路花的腿最近好多了，就顺便叫上她一起。"
    ye_speaking "你要不要先下楼看看，把桌子收一下？"
    lu_speaking "行，那你们继续聊，我就先下去，不打扰了~"
    hide luimg with moveoutright
    ye_speaking "说什么呢，你怎么可能算打扰，我马上就下去找你。"

    ye_speaking "怎么样，她人很好吧？说了不用紧张。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……是啊。"
    mei "虽然我应该感谢叶成华很忙还抽出时间，不过，她到底是过来干嘛的……{p}我有些无奈地看着她打情骂俏，等路花出门后才转过头来。"
    ye_speaking "其实我是想跟你单独再说两句的……但感觉刚刚也说得差不多了。{p}太多重复的话没什么意义，你也不乐意听。总之，看到你状态还行就好。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "嗯，我没事。"
    mei "被打断思绪之后，我也回不到刚刚那个纠结的状态，干脆就这样也不错。"
    ye_speaking "哎呀，好了，其实饭基本做完了，那我们也下去吧。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "嗯。"
    stop music fadeout 0.5

    scene bg_meicorridor with pixellate
    mei "走出卧室，穿过走廊，下楼梯，转过转角。"
    scene bg_meiliv with vpunchs
    $ renpy.sound.play(sound.boom, channel="sound", loop=False)
    na "砰！"
    mei "……嗯？"
    mei "不大不小的爆炸声在头顶响起，随后，五彩斑斓的飘带和亮晶晶的闪片在屋子里炸开，四处飞扬。"
    $ renpy.sound.play(sound.birthday, channel="sound", loop=True, fadein=0.5, relative_volume=0.6)
    show q_people at cg_s with dissolve
    "{size=50}生日快乐！！{/size}"
    mei_speaking "……啊……"
    mei "一瞬间，不止语言能力，连思考能力也从我的身体里全数消失了。"
    mei "十秒，三十秒，一分钟，几分钟，又或者是过去了很久很久……\n我这才找回酸涩的器官。"
    mei_speaking "谢谢……"
    scene bg_meiliv with dissolve:
        blur 25
    mei "我卡壳的大脑努力思考，好一会才意识到这罕见的场景所代表的意义。"
    mei "今天是……{p}我的十八岁。"
    # Don't stop music here
    return