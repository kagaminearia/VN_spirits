label chap4_3:
    scene bg_emptyroom with pixellate
    ye_speaking "向夏？你们还好吗？梅雨怎么样了？"
    mei_speaking "是我。"
    ye_speaking "梅雨！你没事吧？现在能外边走动了吗？我现在去接你？"
    mei_speaking "没事，不知道。你没睡？"
    ye_speaking "怎么睡得着啊，一直在等你的消息。"
    ye_speaking "唉，这事怪我。没提前看好警报，知道下雨的时候赶回去也来不及了。后来没信号，路也不能走，我真是担心死你了……回去之后我就给你买个手机。"
    mei_speaking "啊，嗯，谢谢。"
    ye_speaking "我再看看，如果路能开车我就回去，到时候打向夏电话告诉你。"
    mei_speaking "嗯。"
    ye_speaking "行，多的我也不说了，估计你现在也累得慌。\n你呢别想太多，记着有任何事任何时候都可以来找我就行。"
    mei_speaking "好。"
    mei "我简短和叶成华聊完，把手机递给向夏。她只是朝另一侧耸耸肩膀，我看过去，才发现不知道什么时候彭江丽也来走廊上了。"
    $ renpy.music.play(music.peng_awkward_talk, channel="music", loop=True, fadein=0.5)
    show xiangimg fist o at char_right with dissolve
    xiang_speaking "干啥呢？给她呀。"
    show pengimg shirt eye_care at char_left with dissolve
    peng_speaking "……你确定，我真的可以用吗？"
    xiang_speaking "当然，不是说了嘛，还能反悔不成。况且现在就我有手机啊，能用就用。"
    hide pengimg
    show pengimg shirt at char_left
    peng_speaking "……\n那，谢谢了。真的。"
    mei "看着彭江丽沉默一阵后的回应，我在心底松了口气。{p}马上就可以出去了，不管怎么样，她们两个只要别再起冲突就好。"
    stop music fadeout 0.5

    scene bg_emptyroom with pixellate
    mei "信号的回归似乎是一个好的预兆，当天上午，持续的暴雨终于迎来了终止。"
    mei "到了下午，轻柔的阳光从云后冒出了头。{p}雨停后，积水很快褪去，屋内和屋外都只剩浅至鞋跟的水层。"

    $ renpy.music.play(music.calming_guitar, channel="music", loop=True, fadein=0.5)
    scene bg_meicorridor with pixellate
    xiang_speaking "噢哟，放晴了。"
    show xiangimg o at char_right with moveinright
    mei "刷的一声，半遮挡的窗帘被向夏彻底拉开，明亮的光线穿过玻璃照进房间。"
    $ renpy.sound.play(sound.bird_chirping_2, loop=False)
    show meiimg shirt at char_left with moveinleft
    mei_speaking "嗯……"
    hide meiimg
    show meiimg shirt eye_squint at char_left
    mei "我微微眯起眼睛，几天不见这样的天气，现在已经觉得有些刺眼。{p}但，的确可以说是久违了。"
    hide meiimg
    show meiimg shirt at char_left
    mei "暴雨带来的插曲马上就要播到尾声，接下来的生活应该回归平常的旋律。"

    scene bg_meicorridor with pixellate
    show pengimg shirt o at char_right with moveinright
    peng_speaking "我去楼下收拾，把家具都整理一下。还能用的拿到一边，把房间空出来，清理剩下的积水。不能用的放另一边，到时候你们再看要不要扔掉。对了，我弄完之前别开电闸。"
    show xiangimg fist o at char_mid with moveinright
    xiang_speaking "那我也去，这估计得搞很久吧？"
    peng_speaking "还行，分几次弄，就还好。"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "啊，我……"
    hide pengimg
    show pengimg shirt smile at char_right 
    peng_speaking "噢，梅雨你就在家休息吧？等我们弄完了就跟你说。"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "……好。"
    hide pengimg with moveoutright
    mei "我还没出口的话被咽回去，换成简单易懂的回答。{p}没等我再说什么，彭江丽很快下楼，效率之高令我和向夏面面相觑。"
    xiang_speaking "待楼上估计无聊，你要一起下去吗？"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "我……下去也没事做。"
    xiang_speaking "那你在这不也没事做，不是一样的吗。再说了，想找事情做还不简单。"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "……"
    xiang_speaking "啊，当然我就问问，我是想说，想待哪待哪呗。"
    mei_speaking "……哦，嗯，我知道。"
    mei "我顿了顿，还是决定跟她一起下楼。"

    scene bg_meihome with pixellate
    mei "其实我不喜欢凑热闹，但正大光明坐着休息总觉得还是有些不合时宜。"
    mei "不过，即使下楼，能做的事也并不多。{p}在向夏的大呼小叫下，我大概只是是见缝插针地帮忙递水、开门——只是让我自己心里有些慰藉而已。"
    stop music fadeout 0.5
    stop sound
    
    unknown_speaking "小姑娘？"
    mei "那，我还有什么能做的吗……"
    unknown_speaking "小姑娘？"
    mei_speaking "……咦？啊，抱歉，请问？"
    old_speaking "我看你是叶家的小孩儿嘛？能不能来搭把手？"
    mei_speaking "您说？"
    old_speaking "我看你们也在这搞卫生，我这有个大冰箱没法搬，你一起来成不？"
    mei_speaking "啊？这个……"
    mei "虽然不知道那冰箱长什么样，但我的身体缺乏锻炼，也没力气，估计是还不如健康老太太。{p}可是，总不能就这么拒绝吧……要不看看，有什么别的办法……"
    old_speaking "哎，你要是不想就算了啊，没关系的，我也不是要逼你。行啦行啦，回去玩儿吧，我在这等村里的救援队就行。"
    mei_speaking "诶，不是……"
    show pengimg shirt smile at char_left with moveinright
    peng_speaking "陈奶奶，我们来帮您，冰箱在哪呢？"
    mei "彭江丽的声音出现在背后，我转过头，发现她和向夏似乎是听到动静靠了过来。"
    show xiangimg o at char_right with moveinright
    xiang_speaking "是啊是啊，我朋友刚忙完，现在换我们在弄，您说怎么搞就好。"
    old_speaking "好，好啊。你们都来这边吧。"
    hide pengimg with moveoutleft
    hide xiangimg with moveoutleft
    mei "我看着她们走远，不知道该不该跟上去。{p}正在纠结，向夏回过头，朝我摆了摆手，我于是有些磨蹭地跟在后面，保持一段距离。"
    
    scene bg_vil2 with pixellate
    $ renpy.music.play(music.peng_xiang_work_together, channel="music", loop=False, fadein=0.5)
    mei "我的猜测倒是没错，冰箱着实巨大，适合平时在家囤货的人。{p}在我凑近的时候，彭江丽和向夏已经在冰箱两侧站好，跃跃欲试。"
    show xiangimg fist o at char_right with dissolve
    xiang_speaking "哇……好重！"
    show pengimg shirt eye_angry at char_left with dissolve
    peng_speaking "你……小心点。"
    xiang_speaking "我懂我懂，没问题。"
    hide pengimg
    show pengimg shirt at char_left
    peng_speaking "……"
    xiang_speaking "三，二，一……走！"
    
    scene bg_vil2 with pixellate
    show q0 at cg_s with vpunchs
    xiang_speaking "哇……好了，我们真厉害！"
    peng_speaking "……嗯。"
    mei "她们放下冰箱，顺着刚才的动作击掌。彭江丽瞬间放下手臂、面无表情地撇过头，却也没说别的抱怨的话。"
    hide q0 with dissolve
    mei "而我只是站在旁边，不知道为什么移开了视线。"
    stop sound fadeout 0.5

    scene bg_vil2 with pixellate
    show pengimg shirt o at char_left with dissolve
    peng_speaking "梅雨？走吧。"
    show xiangimg fist o at char_right with dissolve
    xiang_speaking "哦对，我们那边也差不多搞完了，彭江丽说待会再继续，现在先吃饭。"
    mei_speaking "嗯。"
    hide pengimg with dissolve
    hide xiangimg with dissolve
    show bg_vil1 with dissolve:
        blur 15
    mei "……我不知道。"
    mei "我不知道是自己本来就走路缓慢，还是特意放慢脚步，拖着步伐落在她们身后。"
    mei "我不知道为什么她们之前还矛盾相向，现在却不需要我的调停也能心平气和地相处。"
    mei "我更不知道，这明明是对我有利的——她们不吵架，我也不用被夹在中间——但我却丝毫没有感觉到轻松的心情。"
    mei "我不知道。{p}到底，为什么……？"

    scene bg_meikitc with fade
    show pengimg shirt o at char_right with moveinright
    $ renpy.sound.play(sound.running_tap_water, channel="sound", loop=True, relative_volume=0.7)
    peng_speaking "对了，梅雨。{p}就是……能帮我叫向夏过来一下吗？"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "诶？"
    mei "之前，向夏终于学会了使用这里的灶台，因而现在她在做饭，我和彭江丽正在水池旁边收拾碗筷。"
    hide meiimg
    show meiimg shirt at char_left
    mei "彭江丽突然出声让我有些惊讶，但她的表情似乎没有要跟我解释的意思，我也不好多问。"
    stop sound fadeout 0.5

    show xiangimg o at char_mid with moveinleft
    xiang_speaking "咋了？我做了饭还要洗碗吗？"
    mei_speaking "应该，不是……"
    mei "为什么这会是第一想法……不过，我也不知道彭江丽要说什么。{p}甚至，我应该在这吗……但是，现在出去似乎也太刻意了。"
    $ renpy.sound.play(sound.running_tap_water, channel="sound", relative_volume=0.3)
    mei "所以，我只好小心地拧着水龙头，让流出的水柱控制到最小的尺寸，几乎没有声音，尽量把自己的存在感降低。{p}对……我只是需要在这里洗碗而已。"
    hide pengimg
    show pengimg shirt at char_right
    $ renpy.music.play(music.peng_xiang_talk, channel="music", loop=True, fadein=0.5)
    peng_speaking "哦，是我有事找你。{p}就是……"
    hide pengimg
    show pengimg shirt o at char_right 
    peng_speaking "向夏，之前我误会你，说你的不好，对不起了。"
    hide xiangimg
    show xiangimg fist eye_still o at char_mid
    xiang_speaking "呃……啥？"
    hide pengimg
    show pengimg shirt eye_care at char_right 
    peng_speaking "就是，我……因为我自己的原因，擅自猜测你的想法，吃饭的时候冲你发火，对不起。"
    hide xiangimg
    show xiangimg fist o at char_mid
    xiang_speaking "啊，没事，我没生气啊。{p}呃，谢谢……"
    hide pengimg
    show pengimg shirt at char_right 
    peng_speaking "你没生气是你的事，我只是认为我该道歉而已。\n嗯，就是，如果你不介意，就这样翻篇吧。"
    hide pengimg
    show pengimg shirt eye_still at char_right 
    peng_speaking "当然，如果你介意……就——"
    hide xiangimg
    show xiangimg fist eye_still o at char_mid
    xiang_speaking "我当然不介意。我，我也谢谢你这么说。"
    hide xiangimg
    show xiangimg fist smile at char_mid
    xiang_speaking "虽然不知道你为什么看不惯我啦……不过我们之后应该也不会联系，就这样吧，挺好的。"
    hide pengimg
    show pengimg shirt at char_right 
    peng_speaking "嗯，可以。"

    scene bg_meikitc with dissolve
    show pengimg shirt o at char_right with moveinright
    peng_speaking "梅雨？你怎么一直在放水？"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "……呃？\n啊，我，忘了，抱歉。"
    mei "被人提醒，我这才发现自己不知道什么时候停下了洗碗，只是任由水流从水龙头口出来，流过我的手掌，顺畅地向前流下去。"
    hide pengimg
    show pengimg shirt smile at char_right
    peng_speaking "没关系，你累了吗，剩下的我来？"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "不用，我可以。"

    scene bg_meikitc with dissolve:
        blur 20
    $ renpy.sound.set_volume(0.8, 0, channel="sound")
    mei "我重新开始手上的动作，却突然有些不得要领，时不时就握不住海绵，让它滑落到水槽里。"
    mei "不对，我只是在走神而已……"
    mei "因为我似乎后知后觉地摸清楚，令我迷茫而产生堵塞感的模糊感情。"
    mei "虽然不合，虽然碰撞，虽然有不理解，但她们都在各自前进。{p}只有我……"
    mei "只有我，一直停留在原地。"
    stop sound fadeout 1.0
    stop music fadeout 1.0

    return