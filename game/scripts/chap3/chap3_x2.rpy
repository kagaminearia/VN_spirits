label chap3_x2:
    hide meiimg
    show meiimg shirt at char_mid 
    mei "就投给彭江丽吧。"

    scene bg_emptyroom with fade
    show halfdarkblue
    $ renpy.music.play(music.chill_vibe, channel="music", loop=True)
    mei "三张纸写好后放在一起，随后同时被翻开。{p}向夏一票，彭江丽一票，我一票。"
    hide pengimg
    show pengimg shirt o at char_left
    peng_speaking "……你给自己投票？"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "是啊。"
    hide pengimg
    show pengimg shirt eye_angry at char_left
    peng_speaking "哪有这样的？"
    hide xiangimg
    show xiangimg at char_right
    xiang_speaking "之前也没说不能啊。"
    hide pengimg
    show pengimg shirt eye_angry o at char_left
    peng_speaking "你之前不还说梅雨的故事很好吗？"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "那我要投票肯定还是投自己呀。"
    hide pengimg
    show pengimg shirt eye_angry at char_left
    peng_speaking "你这人根本不讲道理。"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "哎呀，那你说怎么办？"
    peng_speaking "……"
    hide meiimg
    show meiimg shirt o at char_mid 
    mei_speaking "要不……重投？"
    mei_speaking "而且，现在是平票。"
    hide pengimg
    show pengimg shirt at char_left
    peng_speaking "我都可以。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "好吧——也有道理，那我也没问题。"

    scene bg_emptyroom with fade
    show halfdarkblue
    mei "结果很快就再次出来。彭江丽一票，我两票。\n有之前的事情，我倒不是很意外……"
    show xiangimg fist laugh at char_right with moveinright
    xiang_speaking "你们说吧！我应该都没问题的！"
    mei "你不要说得我们像土匪一样……{p}向夏摆出一副以身赴死的样子，让我有些无奈。"
    mei "彭江丽看向我，而我眨了眨眼睛，示意让她先说。"
    show pengimg shirt at char_left with moveinleft
    peng_speaking "我没什么想问你的，不过，如果你真的能遵守约定的话，希望你之后别逼梅雨做她不喜欢做的事情。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "诶？这是什么意思，我之前也没有逼她呀。"
    peng_speaking "谁知道呢？就算你不听我也没办法，我只是这么说而已。"
    hide xiangimg
    show xiangimg fist at char_right 
    xiang_speaking "好吧，你这人可真没意思。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "那你呢，梅雨？"
    show meiimg shirt o at char_mid with moveinleft
    mei_speaking "啊？我……"
    mei "向夏撇了撇嘴，然后看向我。{p}我没有打探别人秘密的习惯，不过，有件事我的确有些在意。"
    mei_speaking "你什么都不知道，为什么要来这个地方？"
    hide xiangimg
    show xiangimg fist at char_right 
    xiang_speaking "……\n这不是你之前问过我的问题嘛。"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "嗯，上一次你没说，现在，我帮过你了，可以说了吗？"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "你记性还真好，难怪能把那么长的故事全背下来。"
    mei_speaking "还行。"
    hide xiangimg
    show xiangimg fist eye_close o at char_right 
    xiang_speaking "哇，没想到这成了我给自己挖坑了，行吧行吧……"
    xiang_speaking "其实也没啥，就是……我以前被人帮过一次，还发生了一些神奇的事。"
    xiang_speaking "那个人帮完我就消失了，我就开始找一些神神叨叨的东西，然后找到这里，就想过来看看。"
    hide pengimg
    show pengimg shirt o at char_left
    peng_speaking "……就这样？"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "是啊，哪有那么多复杂的理由。当然，你们不信也正常，不过其实就是这样。"
    xiang_speaking "而且我觉得这里本身也挺好的啊，如果不用工作一直住在这里也没关系。\n梅雨，这回答可以吧？"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "嗯，好。"
    hide meiimg
    show meiimg shirt o at char_mid
    mei_speaking "我只是想知道，会不会影响彭江丽和其他人，别的无所谓。"
    mei "况且，就算她说谎了，我也没法辨认啊……"
    hide xiangimg
    show xiangimg fist eye_close laugh at char_right 
    xiang_speaking "行吧行吧。你们倒是互相关心，合着只有我当恶人啊。"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "……"
    mei "她这话让我心下一紧，但看向她时她仍然是笑着的，语调也很轻松，我也就顺着她把这事揭了过去。"
    mei "不过，我其实并没有想太多，只是不想给别人添麻烦。{p}而向夏某种程度上，也算是我带来的“麻烦”，所以我有种莫名的责任感。"
    stop music fadeout 0.5
    return
