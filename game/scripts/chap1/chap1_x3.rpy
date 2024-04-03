label chap1_x3:
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "噢，噢……好。\n麻烦你特地跑过来……就，不继续浪费你的时间了。"
    hide pengimg
    show pengimg at char_right
    peng_speaking "……嗯。"
    hide pengimg with moveoutright
    mei "我说出再生硬不过的话，彭江丽也明显愣了一瞬间，而后点点头，沉默着离开房间。"
    mei "抱歉……我看着她的背影，不自觉地喃喃自语。心脏有种被揪住的感觉，却又不知如何是好。{p}明明想要接近，却不知道该怎么做，最后剩下的只有尴尬和无措。"

    scene bg_meiliv with pixellate
    show xiangimg o at char_right with moveinright
    $ renpy.music.play(music.slow_laugh, channel="music", loop=True, fadein=0.5)
    xiang_speaking "哇，你真的不吃吗？浪费食物很过分欸。"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "啊？才没有。"
    mei "向夏的声音打断了我的遐想。我有些没好气地瞪了她一眼，说话的语气却也放松了许多。"
    xiang_speaking "那你在这杵着干嘛，面都坨了。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei "我不知道该如何回话，只是叹了口气，无奈地拿起筷子，用行动证明我要吃饭了。"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "喔，好吧，那你吃完之后叫我哦，我来洗碗。{p}{size=30}啊，本来还想着能再吃一点……{/size}"
    mei_speaking "……\n你想吃，自己再做呗。"
    mei "总觉得她说话总是有一茬没一茬的，实在令人费解……"
    hide xiangimg
    show xiangimg fist eye_squint laugh at char_right
    xiang_speaking "诶呀，这不是……我现在不太敢动那个灶台。"
    mei_speaking "……"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left
    mei_speaking "是哦，说起来，我记得有些人，明明之前信誓旦旦，说什么，做饭绝对没问题。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "结果，不仅烧了，还……"
    hide xiangimg
    show xiangimg eye_squint o at char_right
    xiang_speaking "哎呀，不是！这是意外啊。这个灶和我以前用的完全不同！你不做饭肯定不知道，这边的灶太容易炸了，那个火……完全不好把控火候。"
    xiang_speaking "下次，下次绝对不会出事！"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "对了，不过你的手指没事吧，是不是要买点药之类的。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "没事，只是蹭到。"
    mei_speaking "就算有事，现在说也晚了。"
    mei "不知出于什么心情，我又在原本的话上加了一句。原本，应该只是应答一声就够了。\n可能，就是莫名地想呛她一下……"
    hide xiangimg
    show xiangimg eye_squint o at char_right
    xiang_speaking "哇啊，真的对不起……那……在你的手好起来之前，我会帮你做饭洗碗的。\n或者，或者你说个什么别的条件？我绝对尽力做！"
    mei_speaking "真的没事。"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "真的？你这样说的话，那我不管了。不过今天的还是我来洗吧，毕竟我刚刚说过的。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "啊，好。"
    hide xiangimg with moveoutright
    mei "我有点傻眼。坦白讲，我以为一般人在这时候都会客气一下，至少推拉两三句，然而她完全没有这样的意识。"
    hide meiimg
    show meiimg shirt eye_still smile at char_left
    mei "不过，这样感觉也不错……我无奈地笑了笑，突然意识到自己的心情似乎轻松了不少。{p}明明之前还不是这样的……"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei "唉，我这忽上忽下的情绪到底是怎么回事啊……{p}我挠挠头，总觉得莫名有些别扭，但也不打算再继续细想什么。"
    mei "心情好，总归不算坏事吧……"
    stop music fadeout 0.5

    scene bg_meiliv with pixellate
    xiang_speaking "梅雨，过来一下！"
    mei_speaking "啊？怎么了？"
    mei "我一惊，生怕她这么叫是因为又出现像之前在厨房发生的那种事。\n然而转过头之后，却只远远看到她兴奋的笑容。"
    mei_speaking "……哈？"
    xiang_speaking "只是一下下啦，不浪费时间，没什么的，你过来呗。"
    mei "搞不懂她在打什么哑谜。\n我临时改道，把前进方向由楼梯改成厨房。"
    mei_speaking "嗯？"

    scene bg_sunset1 with Fade(0.5,1,1)
    $ renpy.music.play(music.sunset, channel="music", loop=True, fadein=0.5)
    mei "帘子被打开的窗户外侧，大片的橘黄色奢侈地在空旷的天际铺开。稀疏的云仿佛也被烧红，半是遮挡半是衬托着已经隐约可见的星点光芒。"
    xiang_speaking "怎么样？感觉不错吧，果然只要面积够大看起来就好看，我以前可没机会见到这种场景。"
    mei_speaking "是吗。"
    xiang_speaking "对啊，你不觉得吗？你看……黄黄的天，白白的云，还能看到小星星，真的很好看哦。"
    mei_speaking "……噗。"
    mei "听到她的形容，我没忍住笑出声。向夏转了转眼睛看我，没在意，又撑着下巴望窗外。"
    mei_speaking "是啊。"
    xiang_speaking "你说什么？"
    mei_speaking "我说，是很好看。"
    mei "其实我也没见过这样的场景。\n只是，在她提到之前，哪怕看到了，我大概也不会在意吧。"
    mei "我并不像她，能够注意到这些事情……"
    mei "所以此时此刻，我能够感受到眼前燃烧般的的天色带来的畅意，也能够看到她被夕阳染红的快活表情。"
    mei "嗯……说实话……{p}我不得不承认，如果仅仅体会当下，感觉还不错。"
    stop music fadeout 0.5
    return