label chap4_p1:
    hide meiimg
    show meiimg shirt eye_still behind halfblack at char_left
    mei_speaking "你没睡着吗？"
    hide pengimg
    show pengimg shirt eye_care smile behind halfblack at char_right 
    peng_speaking "嗯，不是……我只是比你醒得早一点。"
    mei_speaking "……这样啊。{p}那你还睡吗？"
    hide pengimg
    show pengimg shirt o behind halfblack at char_right 
    peng_speaking "不。"
    mei_speaking "……"
    mei "她的回答如此果断，令我不知道该如何继续。不过，看她连头发都没解开，肯定没有睡好……{p}说不定，连说自己睡过觉了也是逞强。"
    mei "我可以说是很幸运，没有要担心的人，也没有什么需要操心的事，因而还能分出情绪来感受暴雨。{p}她的话……也许只有焦虑和担忧吧。"
    hide pengimg
    show pengimg shirt eye_care o behind halfblack at char_right 
    peng_speaking "啊，是因为我把你吵醒了吗？抱歉……"
    hide meiimg
    show meiimg shirt behind halfblack at char_left
    mei_speaking "没，没有的事。"
    mei "反正已经睡不着了，我干脆也坐起来，抱着被子挪到彭江丽旁边。"

    scene bg_black with dissolve
    show cg_p40 at cg_0 with dissolve
    peng_speaking "你这样坐，会不舒服吧？"
    mei_speaking "不会。"
    peng_speaking "那就好……不舒服的话，跟我说。{p}嗯，说起来，我们好像，都很久没有像这样一起坐着了。"
    mei_speaking "诶？嗯……小时候，还睡一起的。"
    peng_speaking "是啊……以前你总是睡在我家，然后，晚上老抢我被子。"
    mei_speaking "有吗？没有吧……！"
    peng_speaking "嗯，好，都是怪我没有自己看好被子。"
    mei "彭江丽浅浅地笑了，而我则是有些不好意思，声音也扬起了几分。"
    peng_speaking "那时候好像都没做过什么别的事，就是每次睡觉而已。"
    mei_speaking "嗯？"
    peng_speaking "就是，我们今天不还讲了故事吗，还有别的……之前都没有想过这样。"
    mei_speaking "……你喜欢这种，的吗？"
    mei "我有些惊讶，我以为她会很讨厌向夏，也不喜欢搞这些胡编乱造的活动。"
    peng_speaking "不是！不是这个意思……我是觉得，这样能有机会跟你静下来聊天，就挺，挺好的……"
    mei_speaking "这，这样啊……"
    mei "不知为何，她突然有些结巴，搞得我也变得紧张起来。"
    peng_speaking "不过，小时候只要能和朋友凑在一起，就觉得很开心。只是，后来也……啊。"
    hide cg_p40
    show cg_p41 at cg_0
    mei_speaking "嗯……"
    stop music
    mei "彭江丽突兀地止住了话，我也瞬间意识到她原本想说什么。{p}我们从未直接提起过，却从来都避而不谈。"
    show cg_p40 at cg_0 with dissolve:
        linear .5 blur 10
        linear .5 blur 10
    $ renpy.music.play(music.calming_piano, channel="music", loop=True, fadein=0.5)
    peng_speaking "没事的……{p}现在这样，我也觉得很好。"
    mei "她轻声说道，而我则沉默许久。{p}现在，只要我稍稍抬起眼，就能够看到近在咫尺的她。"
    mei "灯光照明范围有限，灰沉沉的房间溶解了身影的轮廓，使得她看起来格外柔软。"
    mei "如果忘记刚刚的对话，这样的氛围和距离会让我产生一些错觉。{p}错以为我们现在还是十来岁，还不需要顾虑太多事情，还只是那时候无数的平凡夜晚的其中之一。"

    scene bg_black with fade
    peng_speaking "梅雨，我是不是……"
    mei "粘稠的沉默中，彭江丽忽然开口，只是说到一半就没了下文。"

    show cg_p50 at cg_0 with dissolve
    mei_speaking "……怎么了？"
    peng_speaking "不……没事。"
    mei_speaking "……"
    peng_speaking "……{p}我只是突然觉得，我在这里，和别人在这里，并没有什么区别。"
    mei_speaking "什么……"
    peng_speaking "如果是……如果是向夏的话，说不定她会跟你聊得更开心。"
    mei "这又关向夏什么事？{p}彭江丽只是自顾自地说着，声音低沉而缓慢，只有我摸不着头脑。"
    show cg_p51 at cg_0
    hide cg_p50
    peng_speaking "我只不过是占了早认识你的好处，其实我可能根本不适合……作为朋友，还比不上你刚认识的向夏。"
    mei_speaking "不，你……"
    show cg_p50 at cg_0
    hide cg_p51
    peng_speaking "梅雨。如果……{p}如果我们小时候不是邻居，我们还会是朋友吗？"
    mei_speaking "……"
    mei "是，或不是，我没法这么回答这个问题。{p}可是……"
    mei_speaking "……可是，没有如果。{p}我们已经，是朋友了。"
    mei_speaking "过去是，现在……也是。"
    mei "盖在腿上的被子被我攥得紧紧团在一起，我深深呼出一口气，终于费力地说完这句很短的话。{p}然后，我看到彭江丽似乎笑了。"
    show cg_p51 at cg_0
    hide cg_p50
    peng_speaking "你是这么想的吗？{p}那，真是……"
    show cg_p52 at cg_0 with dissolve
    peng_speaking "……太好了。"
    stop music fadeout 0.5
    stop sound fadeout 0.5
