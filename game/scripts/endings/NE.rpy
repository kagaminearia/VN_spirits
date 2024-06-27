label NE:
    scene bg_vil4 with fade
    mei "天色湛蓝，薄云缓慢地漂浮，在远处的山脉上留下淡淡的阴影。\n我拖着行李，在不规则的路上发出喀喀的声响。"
    mei "……和来的那天差不多。"
    show yeimg at char_right with moveinright
    ye_speaking "怎么了？突然停下，不舒服吗？"
    show meiimg o at char_left with moveinleft
    mei_speaking "啊？不，没事。"
    mei "事实上我只是有些走神，所以才忘了继续走……{p}叶成华仔细打量了我一遍，见我真的没什么反应，这才舒了口气，继续往前。"
    ye_speaking "有事跟我说啊，不差这一点时间的。"
    mei_speaking "嗯，我知道。"
    hide meiimg
    show meiimg at char_left 
    mei_speaking "……"
    hide meiimg
    show meiimg o at char_left 
    mei_speaking "这样，真的好吗？"
    ye_speaking "你说什么不好，从这回去吗？现在反悔的话还来得及哦。虽然买了票，但也就亏一点点，没有你的想法重要。"
    mei_speaking "……\n没，算了，我随便说的。"
    mei "事实上，我真的有一瞬间的心动，但很快冷静下来。{p}这个决定不是临时起意，我不打算再麻烦叶成华，也觉得在这个地方不能达到我想要得到的结果。"
    mei "自己想不明白，逃避到哪里都没用。我应该知道。"
    mei "不知是不是感觉到我的状态低沉，叶成华也没有再说话。我们只是一路无言地走到车站，期间，只有重复的滚轮声循环播放，十分闷沉。"
    
    scene bg_station
    show yeimg smile at char_right with moveinright
    ye_speaking "别担心。"
    show meiimg at char_left with moveinleft
    mei_speaking "……嗯？"
    ye_speaking "我说，你别担心。{p}你从这里离开，不是你不适应，是这里不适合你。"
    ye_speaking "我知道你大概迷茫，但我也帮不上忙，真的是很抱歉。"
    hide meiimg
    show meiimg eye_still at char_left 
    mei_speaking "不，不是你……是我自己不行。"
    ye_speaking "嗨，日子还长呢。就算现在你没遇到，以后，总能遇到能让你敞开心扉的事情，或者遇到你想敞开心扉的人。你呢，就遵从自己内心想法就好了。"
    mei_speaking "可是，我真的不知道……"
    ye_speaking "没事，慢慢想。或者，就选一个让自己轻松点的，不那么难受的事情吧。{p}世界上这么多人，真正能想清楚自己的人也没多少嘛。有时候我自己都搞不懂呢。"
    hide meiimg
    show meiimg at char_left 
    mei_speaking "……唔。嗯。"
    mei "叶成华用力揉着我的脑袋，有些痒，不过我没有避开，而是任由她揉着。"
    hide yeimg
    show yeimg at char_right
    ye_speaking "车快到了，你先过去吧。之后有任何事，随时联系我。"
    mei_speaking "好。"
    mei "感受到头顶的触感消失，我下意识地抬头，不知道是想挽留她的手，还是什么别的东西。{p}但是没有，我只是呆呆地看着叶成华。然后她笑了，轻轻拍了拍我的后背。"
    ye_speaking "别担心。"
    mei_speaking "嗯。"
    mei "没什么的，我知道……{p}我……总要找到自己的路。"
    $ persistent.NE = 1
    window hide
    scene bg_white with Dissolve(4)
    pause(0.5)
    show screen endings_screen(endings,"NE") with Pixellate(3,25)
    pause
    scene bg_station with Fade(0.5,1.5,0.5)
    show movie_side with moveinleft
    lu_speaking "行了，车都走远了，还有啥好看的？"
    ye_speaking "啊……是。"
    na "被身旁的人提醒，叶成华下意识应了一声，而后才回过神，有些无所谓地笑了笑。"
    lu_speaking "怎么，后悔啊？"
    ye_speaking "后悔什么？"
    lu_speaking "后悔非得把你那小妹妹骗过来呗？人现在还不是走了，也没用啊。"
    ye_speaking "也是预想过的结果啊。"
    na "叶成华耸了耸肩膀，对路花语气中的挖苦视而不见。"
    lu_speaking "所以说——有必要嘛，完全是给自己找麻烦。"
    ye_speaking "哼，也不知道是谁，比我还在意梅雨的情况呢，每天都得问一遍。"
    lu_speaking "……就你话多。"
    na "路花瘪了瘪嘴，瞪着叶成华的笑脸，而后飞快地撇过头去。"
    ye_speaking "你又不是第一天知道。"
    lu_speaking "好，好。"
    na "叶成华伸手轻轻地梳着路花垂下的柔顺长发，好一会才把人给哄好。"
    na "她嘿嘿笑了两声，又沉默了好一阵，才再次开口。"
    ye_speaking "那时候……我看到梅雨，她真是把我吓到了。简直就像，就像……"
    lu_speaking "就像死人一样？"
    ye_speaking "怎么说话呢小路花？"
    lu_speaking "哎呀，就说是不是嘛。"
    ye_speaking "是……呸，是个头啊。她就是像……像玩偶似的，很冷漠，对什么事都没兴趣，跟她说话也没有任何反应，基本就是坐在那里。"
    ye_speaking "啧，真的是……我当时就想着，至少找个办法让她转移下注意力啊。"
    ye_speaking "现在嘛……至少她没那么封闭自己了，之后再想别的，慢慢来吧。"
    lu_speaking "你倒是一直挺乐观。"
    ye_speaking "那不然怎么办嘛？"
    na "路花嗤笑一声，而后又轻轻叹了口气。"
    lu_speaking "我是担心你罢了……现在没事是很好，但小梅这种情况，你之前那样贸然干涉她，很有可能会让她的情况更严重的。"
    ye_speaking "……是啊，我是被吓到，太冲动了。不过我也会负责的，最坏……我养她一辈子也可以。"
    lu_speaking "哼，你倒是想得清楚。"
    ye_speaking "装什么呀，你不也是这么想的？"
    lu_speaking "……"
    na "路花又轻哼一声，而后定定地盯着叶成华看了好一会儿。两人的目光毫不避讳，最终还是路花败下阵来，移开了视线。"
    lu_speaking "别替我说好话，你知道我只是因为你才这么做，不然我才没空管其他小孩的事情呢。"
    ye_speaking "好，好，我知道，反正我们会照顾她的对不对？"
    lu_speaking "是啊。大人照顾小孩儿，天经地义嘛。"
    na "温暖的阳光从树叶间落下，落在两人相视而笑的脸庞之上。远处，大巴车离开的方向已经没有人影，只有被加热到有些扭曲的空气。"
    na "如同梅雨来时的那天一样。"
    scene bg_white with Dissolve(1)
    pause
    return