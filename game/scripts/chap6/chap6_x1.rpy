label chap6_x1:
    scene bg_meiliv with fade
    mei "叶成华把彭江丽抱到路花的车上，我们看着路花开车离开。"
    mei "我和叶成华回到房间，她拒绝了我的帮忙建议，只说她自己收拾就好，而后把我和向夏都赶到了厨房外面。"
    mei "我下意识地瞥向旁边，结果刚好和向夏对上了视线。"
    $ renpy.music.play(music.xiang_awkward_talk, channel="music", loop=True)
    show xiangimg fist o at char_right with moveinright
    xiang_speaking "怎么了？"
    show meiimg shirt at char_left with moveinleft
    mei_speaking "……"
    mei "上次的事情之后，我还不知道该如何面对她，她倒是跟没事人一样，我也只好硬着头皮装作平淡。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "你没喝醉？"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "嗯？你说果酒吗？当然不会这样就醉。\n别小看打工的人，我可是曾经喝进医院过的。"
    hide meiimg
    show meiimg shirt at char_left
    mei "……这不好吧…………\n虽然我是想看她喝醉的糗态，但并没有想过会得到这种回答。"
    mei_speaking "不难受吗？"
    hide xiangimg
    show xiangimg fist at char_right 
    xiang_speaking "……"
    hide xiangimg
    show xiangimg fist laugh at char_right 
    xiang_speaking "呃，所以后来就不喝了嘛，不过像这种度数比较低的倒是没关系，还挺好喝的。"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "哦，对了，刚好趁这个机会……{p}虽然你姐之前说不需要，不过我觉得还是给你……"
    mei_speaking "我不要。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "喂喂，我还没说完呢，你知道我要说什么吗就拒绝了。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "礼物？"
    hide xiangimg
    show xiangimg fist at char_right 
    xiang_speaking "好吧……既然你知道，那别拒绝了呗？我多尴尬啊。"
    mei "我可没看出来你有哪里尴尬……{p}虽然收不收我都觉得无所谓，但是……"
    mei_speaking "只是交易关系，就没必要了吧。\n为什么要送？反正……我们不熟。"
    hide xiangimg
    show xiangimg fist eye_still at char_right 
    xiang_speaking "……"
    mei_speaking "你不送，我也不会害你。"
    hide xiangimg
    show xiangimg fist eye_still smile at char_right 
    xiang_speaking "行吧。先说啊，我没那个意思，但是都准备好了，你就收下呗，你就不好奇是什么吗？"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei_speaking "不要，不好奇。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "哇，我怎么才发现……你这个人除了很阴沉以外，还特别倔强啊。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "那明明是你……"
    show yeimg at char_right with dissolve
    show xiangimg fist o at char_mid with moveinright
    hide meiimg
    show meiimg shirt o at char_left, shakeonce
    ye_speaking "你俩在这干嘛呢？"
    stop music
    hide meiimg
    show meiimg shirt at char_left
    mei "嘶……吓死我了\n我的肩膀剧烈地抖了抖，而后被向夏按住。"
    ye_speaking "我都快收完了，怎么还站在这里啊……你们该不是吵架了吧？"
    hide xiangimg
    show xiangimg fist eye_squint laugh at char_mid 
    xiang_speaking "哪能呢？我们是在讨论事情。"
    $ renpy.sound.play(sound.girl_chuckle, channel="sound", loop=False)
    mei "向夏顺势一把拉过我的肩膀，摆出一副贴近的样子。\n这人的反应还真快……我有些无奈，但现在还是配合一下吧。"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei_speaking "嗯，是啊。"
    ye_speaking "那你们杵在这聊干嘛？去房间里啊。我待会还得收拾外边呢，行行行去吧。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei "搬起石头砸自己的脚……"
    stop sound

    scene bg_meiroom with fade
    $ renpy.sound.play(sound.bird_chirping_2, channel="sound", loop=False, fadein=0.5)
    mei "老话说，一个谎言要用无数个谎言去圆。现在虽然不用再说，但……"
    mei "因为刚才的谎话，我现在只能待在房间里，和向夏面面相觑。"
    show xiangimg fist eye_still o at char_right with moveinright
    $ renpy.music.play(music.xiang_first_meet, channel="music", loop=True)
    xiang_speaking "呃，这……是个意外。\n我以为，她说完之后就会走了。"
    show meiimg shirt at char_left with moveinleft
    mei_speaking "……"
    mei "算了……正好趁这个机会说清楚也好。总不能一直尴尬下去，她还要在这里待一阵子呢。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "放心好了，我没想着跟你吵架。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "啊？好啊，我也不喜欢吵。不过，你是还要说点什么吗？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "呃，算是吧。\n之前……算是我想岔了。总之，我们像最开始那样就行。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "就当个舍友，好好相处。"
    mei_speaking "你走之前，我不想给叶成华添麻烦。"
    hide xiangimg
    show xiangimg fist laugh at char_right
    xiang_speaking "正好呀，我也是这么想的！这是不是就叫做，嗯，聪明的人想的都差不多？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei "她怎么能如此自豪地说出这句话……"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "像这样也没什么不好的嘛，又不是不说话了，就是，就是选取自己需要的呗！你看你平时说话这么少，可以放心跟我练习啊，多练练就好了。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "我又不是不会说话。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "那你倒是说呀，平时不总是很阴沉的嘛，像费老大劲了。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "那只是……算了，好吧。"
    mei "那只是因为以前实在没什么机会和别人交流，长久以来语言水平有些“退化”，但我本身并不排斥。{p}不过，倒没必要跟她解释得这么详细……"
    hide xiangimg
    show xiangimg fist laugh at char_right
    xiang_speaking "对了，既然不吵架，那你要不把礼物也一起收了？"
    mei_speaking "不。"
    mei "只有这个是不需要的。"
    mei "毕竟，如她所说，也许把这些都当做交易就会轻松很多……\n但如果是交易，自然，也不需要这些额外的东西了。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "好吧好吧，我知道了，你还真不可爱。"
    mei_speaking "……"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left
    mei_speaking "……呵。"
    hide meiimg
    show meiimg shirt at char_left
    mei "我挤出一声轻哼，算是对她这句无端的指责的回应。"
    stop music fadeout 0.5
    return