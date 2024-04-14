label chap3_3:
    scene bg_emptyroom with fade
    show halfblack
    show meiimg shirt eye_still o at char_mid with dissolve
    mei_speaking "嗯……几点了？"
    mei "我打了个呵欠，看着因为揉眼睛变模糊的小夜灯，正在散发着幽幽的白光。"
    mei "室内环境毫无变化，晦暗，寒凉，带着潮气。{p}如此这般密闭的空间，似乎连时间都被定格，浓稠得无法流动。"
    show xiangimg fist o at char_right with dissolve
    xiang_speaking "九点出头，还早。"
    hide meiimg
    show meiimg shirt o at char_mid
    mei_speaking "……该睡了。"
    xiang_speaking "啊？那……那行吧。\n你也觉得可以？"
    show pengimg shirt o at char_left with dissolve
    peng_speaking "是啊，现在睡觉也算正常。"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "好吧……少数服从多数，我懂。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "不是你要去哪儿？"
    mei_speaking "睡觉啊？"
    mei "向夏突然抓了抓我的衣服下摆，而我则是一脸莫名其妙。"
    xiang_speaking "你忘了，你房间不都淋湿了吗。"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "……"
    mei "我默默停止往外走的动作，转身，坐回原来的位置，叹气。{p}因为我中午睡觉习惯开窗，房间靠外的一侧全部都湿了。"
    mei "不过，只有我一个人在隔壁睡床也不太好……{p}这么想着，我又觉得好像没那么烦了。"
    hide pengimg
    show pengimg shirt eye_care o at char_left 
    peng_speaking "抱歉啊，都怪我也来挤你的位置……"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "就算你不过来，我也得在这睡啊。\n这有好几套被子呢，虽然不一样厚。来来分一下。"
    hide pengimg
    show pengimg shirt at char_left 
    peng_speaking "……"
    mei "彭江丽沉默了一瞬，没有理向夏，而是转过头看着我。"
    hide pengimg
    show pengimg shirt o at char_left 
    peng_speaking "梅雨，你拿这个最厚的吧，我随便一个就可以了。"
    hide meiimg
    show meiimg shirt o at char_mid
    mei_speaking "好。"

    scene bg_emptyroom with fade
    show halfblack
    $ renpy.music.play(music.calming_piano, channel="music", loop=True, fadein=0.5)
    mei "如之前所说，地垫确实够大，睡三个人绰绰有余，但……"
    mei_speaking "……"
    mei "总觉得……好奇怪啊。{p}我连宿舍都没睡过，现在却要直接跟两个人平躺在同一张“床”上。这对我来说……实在是有些冲击过大。"
    xiang_speaking "你们真的能睡着嘛？"
    peng_speaking "嘘……"
    xiang_speaking "好吧……"
    mei "实际上，我并没能这么快睡着。只是我实在很累，不想再说话，也不想睁开眼睛。"
    mei "闭上眼睛之后，其他感官会变得更加敏感。不知道是不是错觉，身体两侧的他人气息格外清楚。{p}这样真的能睡着吗……"
    mei "虽然这么想，但躺在松软的被子里，身体像是接收到什么信号，反应来势汹汹，无法阻挡。"
    mei "原来我比我想象的还累啊……{p}先前还没觉得，但毕竟冒着雨在外面走了许久，后来在走廊上睡当然也睡不踏实。"
    scene bg_black with dissolve
    mei "身体越来越重，我的思绪也逐渐变得朦胧。"
    mei "希望，雨快点停吧……"
    stop music fadeout 0.5
    stop nature
    stop sound
    return