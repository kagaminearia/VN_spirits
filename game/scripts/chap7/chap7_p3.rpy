label chap7_p3:
    scene bg_meiroom with fade
    $ renpy.sound.play(sound.bird_chirping_1, channel="sound", loop=False, fadein=0.5)
    mei "被阳光晒醒时，我有一瞬的恍惚，好一会才反应过来自己是在彭江丽家——我自己住时，睡觉几乎不开窗帘。"
    mei_speaking "几点了……"
    mei "昨晚没睡好，也许是因为床太小了，也许是因为睡在她身边，我的心脏一直在不规律地跳动，搞得我心神不宁。"
    show halfwhite with dissolve
    mei "以至于，即使醒了，脑袋也昏昏沉沉的，眼睛也因为阳光太刺眼而睁不开，只能眯着眼睛四处摸索。"
    mei "外套，好像在柜子上，先拿一下……"
    scene bg_black with vpunchm
    na "轰！咚！"
    mei_speaking "哇啊！"
    mei "因为看不清，我凭着感觉到处乱摸，手肘不小心挂到了桌子抽屉的把手。\n随即，似乎有什么东西噼里啪啦掉出来，落了一地。"
    scene bg_meiroom with dissolve
    mei_speaking "呃……"
    mei "眼睛逐渐习惯光线，我赶紧把东西摆回原来的地方，却被其中一个东西吸引了注意力。\n它旧得离谱，和其他东西格格不入。"
    show q_letter at cg_s with dissolve
    mei "这似乎是一张“纸”，上面密密麻麻贴满了胶带。胶带已经发黄，可以隐约看见底下的碎纸边缘和墨水晕开的字。"
    hide q_letter with dissolve
    mei_speaking "这什么……"
    show pengimg shirt o at char_right with moveinright
    peng_speaking "梅雨！你没事——"
    hide pengimg
    show pengimg shirt at char_right 
    mei "彭江丽急匆匆地推开房门，脸上还带着水——大概是刚洗完脸——看到我时却愣在原地。"
    show meiimg shirt eye_still o at char_left with moveinleft
    mei_speaking "抱歉，我刚刚不小心撞到了柜子，这个……"
    hide pengimg
    show pengimg shirt eye_care o at char_right with vpunchs
    peng_speaking "啊这个我来收就好！"
    mei "砰的一声，她粗暴地把所有东西一股脑塞进抽屉。"
    stop sound

    scene bg_meiroom with pixellate
    # ?: peng shirt changed
    show meiimg eye_still o shell at char_left with dissolve
    mei_speaking "对不起，不过你别担心，我什么都没看到……"
    mei "实话说，那胶带缠得一层一层，还变色，我都差点看不出那里面贴的是一张纸。"
    show pengimg shirt eye_care o at char_right with dissolve
    peng_speaking "……啊，没事，没事的……我就是，有点惊讶。刚刚你没受伤吧？没撞到哪里吧？"
    hide meiimg
    show meiimg shell at char_left
    mei_speaking "没事，不过你没去上学么？"
    hide pengimg
    show pengimg shirt smile at char_right
    peng_speaking "我刚回来呀，现在都到午饭时间啦。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "啊？我睡了这么久……那我怎么还这么困……"
    hide pengimg
    show pengimg shirt o at char_right
    peng_speaking "肯定是昨晚没睡好，都怪我，非要拉你过来睡觉，唉……"
    hide meiimg
    show meiimg shell at char_left
    mei_speaking "没有没有，没事的，今天晚上我回去就行了，也不打扰你。"
    hide pengimg
    show pengimg shirt at char_right
    peng_speaking "嗯，好吧……"

    scene bg_pengback with pixellate
    $ renpy.music.play(music.peng_poor_little_girl, channel="music", loop=True, fadein=0.5)
    mei "彭江丽看起来兴致不高，因而我午饭后又跟她一起做了一次清洗工作——当然，我也只能在院子里看着。"
    mei "她来回搬着已经洗完的工具，动作却突然停了下来。"
    show meiimg eye_shock o shell at char_left with moveinleft
    mei_speaking "怎，怎么了？"
    mei "我有些慌忙地走上前，她却只是笑了笑，冲着我摇摇头。"
    show pengimg shirt smile at char_right with moveinright
    peng_speaking "只是感觉有点重……可能是最近没锻炼身体吧，嘿嘿……"
    hide meiimg
    show meiimg eye_still shell at char_left 
    mei_speaking "……"
    mei "是因为最近太累了吧……家里的事变多，去学校补课的次数也多。\n只是，我虽然这么想着，却什么也没说。"
    hide meiimg with dissolve
    hide pengimg with dissolve
    mei "苍白的安慰最无力，而我什么也帮不到她。"
    mei "她明明是我最重要的朋友，我应该，应该……"

    show pengimg shirt smile at char_right with dissolve
    peng_speaking "怎么啦？站在这里，我东西都搬完了哦。"
    show meiimg o shell at char_left with dissolve
    mei_speaking "噢……"
    show halfwhite with dissolve
    mei "汗珠从彭江丽的脸颊两侧流下，在反射出亮晶晶的光线，晃了我的眼睛，也晃了我的心神。"
    mei "因此，没有多想，话语就从我的口中蹦出。"
    hide halfwhite with dissolve
    hide meiimg
    show meiimg shell at char_left
    mei_speaking "我身体的情况，你知道多少？"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "啊……啊？！"
    hide pengimg
    show pengimg shirt eye_care at char_right
    peng_speaking "怎么突然这样问……"
    hide pengimg
    show pengimg shirt eye_still o at char_right
    peng_speaking "就是，嗯……知道你之前搬家是因为生病了，这次回来是休养身体，之前，嗯，晕倒的时候，好像也是因为……"
    hide pengimg
    show pengimg shirt eye_still at char_right
    mei "她的声音越说越小，表情也变得紧张。\n我尽量让自己露出一个笑容，试图让气氛轻松一些。"
    hide meiimg
    show meiimg eye_still smile shell at char_left
    mei_speaking "感觉，之前都瞒着你，不太好……\n不过其实，也差不多……"
    hide meiimg
    show meiimg eye_close shell at char_left
    mei_speaking "这次是叶成华让我回来住的。她可能……觉得我需要换个环境休息一段时间吧。"
    hide meiimg
    show meiimg eye_close o shell at char_left
    mei_speaking "因为，嗯……其实我今年的升学考失败了。"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "……啊……？？"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "噢，我晕倒是因为病跟心脏有关，还……挺严重的。那天，跟你第一次见面的时候，算是后遗症吧……抱歉啊，我都没跟你说。"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "不过其实……我小时候有给你写信，一到新家就开始写了。后来在医院的时候也……我一直想跟你联系，但是我没想到，那时候弄错地址了，就没寄成……"
    mei_speaking "后来做完手术，可以正常上学，只是要吃药，不能做激烈的活动，也不能有激烈的情绪起伏。"
    hide meiimg
    show meiimg eye_close o shell at char_left
    mei_speaking "那时候，我也没有想着回来找你……因为我一直害怕，害怕你怪我，什么都不说就走了。对不起。"
    hide pengimg
    show pengimg shirt eye_care at char_right
    peng_speaking "我怎么会那么想……"
    hide meiimg
    show meiimg eye_close shell at char_left
    mei_speaking "……"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "那，就是……\n升学考的事呢……？"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "嗯……在学校的时候，我有很多……很无聊很幼稚的想法，想证明自己啦之类的。\n所以，那个考试我真的很看重。"
    hide meiimg
    show meiimg eye_still smile shell at char_left
    mei_speaking "结果……结果挺可笑的，第一天考试我过度紧张，心脏受到刺激晕倒了，后来就在医院里看着考试结束。"
    mei "真有意思啊。\n一直把我牢牢困住的事情，留下让我疼痛的印记的事情，竟然用这么简单的一句话就能说完了。"
    hide pengimg
    show pengimg shirt eye_care at char_right
    peng_speaking "怎，怎么会……"
    hide meiimg
    show meiimg eye_still shell at char_left
    mei_speaking "……"
    hide meiimg
    show meiimg eye_still laugh shell at char_left
    mei_speaking "哎呀，其实只是，就是……"
    hide meiimg
    show meiimg eye_still smile shell at char_left
    mei_speaking "就是……"
    hide meiimg
    show meiimg eye_close shell at char_left
    mei "……就是什么呢？\n就是我太笨了。就是我不自量力。就是我什么都做不好。就是……"
    mei "我沉默很久，还是没能说出完整的话。{p}我以为我能豁达地笑过去，显得很潇洒，不在意，但……做不到。"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "反正——"
    hide meiimg
    hide pengimg
    show halfwhite with dissolve
    mei_speaking "……啊。"
    mei_speaking "我的话没能说完，因为彭江丽忽然抱住了我。\n她的双臂温暖而有力，虽然在微微颤抖，但还是紧紧环抱着我。"
    peng_speaking "……是我该说对不起，才对。"
    peng_speaking "是我给你太大压力了吧……对不起。\n那天，我说有话想跟你说，吓到你了吧。"
    mei_speaking "不，没……"
    peng_speaking "其实，那一天，我是想说……你还愿意重新跟我做朋友吗。\n是，这样的意思……"
    mei_speaking "这样啊……"
    mei "我抬起手臂，轻轻地放在彭江丽的肩膀上。\n虽然看不到她的表情，但这触感是如此真实。太好了……她没有讨厌我。太好了……"
    mei_speaking "当然愿意了。"
    peng_speaking "那就好……\n{size=30}只要这样，就好……{/size}"

    scene bg_pengback with fade
    mei "拥抱后，身上还残留着她的体温，我有些尴尬地移开视线。"
    show meiimg eye_close o shell at char_left with dissolve
    mei_speaking "咳……其实，我是想说。"
    show pengimg shirt o at char_right with dissolve
    peng_speaking "什么？"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "你看，我现在也……需要学习。所以，跟你讲题的时候，也是自己复习啊。我也会，跟你一起学习的。"
    mei "俗话说，说谎要三分假七分真，我大概现在就在实际应用吧。"
    hide pengimg
    show pengimg shirt eye_care at char_right
    peng_speaking "……啊。"
    mei_speaking "我不是要强迫你，我是想问，你……不去学校的时候，可以再一起讲题目吗？"
    peng_speaking "……"
    hide pengimg
    show pengimg shirt smile at char_right
    peng_speaking "好啊。"
    stop music fadeout 0.5

    scene bg_meiroom with fade
    $ renpy.sound.play(sound.summer_night, channel="sound", loop=True, fadein=0.5)
    mei "今天，终于说出想说的话了……"
    mei "我躺在床上，止不住卷着被子滚来滚去的动作。\n真是，不知道为什么……"
    show halfblack with dissolve
    mei "之后，还能跟她一起学习，太好了……\n虽然这么说很自大，但是……"
    mei "我想帮她，想帮她实现目标……"
    stop sound fadeout 0.5

    scene bg_meiroom with fade
    mei_speaking "嗯……"
    mei "结果，因为我对还没开始的事想太多，昨天晚上又没睡好，连第二天的午睡也比平时更久，睡得头晕。"
    mei_speaking "现在，几点……"
    mei "窗帘晃动，些许光线进入，照亮床头的电子显示屏，下午五点。"
    mei "昨天才说想要努力，结果今天就睡这么久……"
    mei "唉……我叹了口气，有些无语地往外走。\n……嗯？"

    scene bg_meicorridor with dissolve
    $ renpy.sound.play(sound.stressed, channel="sound", loop=True, fadein=0.5)
    mei "楼梯口传来微小的声响，似乎是有人在说话。"
    mei "这时候会有谁在客厅……我放轻脚步，如同做贼一样悄悄下楼，还没下到楼底，我就听清了外面的声音。"
    mei "是……叶成华和彭江丽……？叶成华倒是有时会回来，但彭江丽为什么在这……"
    show halfblack with dissolve
    mei "不知道出于什么心情，我没有直接下楼走出去，而是继续压低脚步，停在墙边。"

    scene bg_black with Dissolve(0.2)
    show movie_side
    show bg_meiliv behind movie_side with moveinleft
    ye_speaking "你问我跟路花？让我想想……我当时刚开始在镇上工作，然后就认识她了，后来就在一起了。"
    peng_speaking "……这样啊……"
    mei "声音窸窸窣窣，隔着墙壁传来，不算大声，但也足够听得清。"
    ye_speaking "哈哈哈，抱歉啊，有些事涉及路花，我是不太好私自说。"
    peng_speaking "没有，我其实……"
    ye_speaking "嗯，你特意过来，应该不是真的只是想问我这个吧？"
    peng_speaking "啊……"
    ye_speaking "我只是自己猜测啊，要是说错了，你就当我在胡扯。"
    peng_speaking "没有错……我……"
    peng_speaking "……梅雨还在睡觉吗？"
    mei "怎么突然提到我的名字……虽然知道自己不会被看到，我还是不由得绷紧了身体。"
    ye_speaking "肯定还没起呢，估计是昨天没睡好吧？她但凡下午睡觉总会睡很久，没事，我不会跟她讲的。"
    peng_speaking "……嗯，我知道。我就……问问。"
    peng_speaking "你和路花姐，是怎么确定关系的呢……？\n我好像也有，喜欢的人……但，我……"
    $ renpy.music.play(music.peng_after_school, channel="music", loop=True)
    mei "什么……彭江丽，她有喜欢的人……"

    ye_speaking "……\n你喜欢的人，也是女生吗？"
    peng_speaking "……"
    peng_speaking "……是，的……但是，我……"
    peng_speaking "我不知道……我应该是喜欢她，却忍不住嫉妒她。我希望她好，却不希望她那么好，我怕她把我甩在身后，我怕她嫌弃我……"
    peng_speaking "她总是很善良，很坚强，不管我怎么样都会包容我……我对她做了很过分的事，她却还是……我，呜……"
    ye_speaking "嗯，我觉得你先不要这样想，她肯定——"
    peng_speaking "不是的，我……我欺骗了她，还想装作什么都没发生过，想跟她越来越亲密……我知道这不对……可是我不敢告诉她……"
    peng_speaking "我只是，不，我……我觉得……我觉得保持现状就已经很满足了……"
    ye_speaking "……"
    ye_speaking "我想，你一直都是个很有自己想法的人，现在也肯定是。"
    ye_speaking "既然你已经想好了，今天特意过来，我现在有什么能帮你的呢？"
    peng_speaking "谢谢你，成华姐……"
    peng_speaking "我只是，我想……\n……"
    peng_speaking "成华姐，你这么聪明，肯定早就知道我在说谁了对不对……"
    ye_speaking "哎呀，这个怎么说呢……"
    peng_speaking "对不对……？"
    ye_speaking "算是有一些自己的猜测吧。"
    peng_speaking "嗯，我知道……\n我，就是想拜托成华姐一件事……"
    ye_speaking "嗯，什么？"
    peng_speaking "我……我知道，梅雨是您很关照的妹妹，所以……"
    peng_speaking "我知道这样很卑鄙，但是……{p}求求你，不要把我说的事情告诉梅雨。"
    mei "……咦？"
    peng_speaking "我……我绝对不会再做对她不好的事，但是……"
    show cg_p91 at cg_0 with dissolve
    peng_speaking "我好不容易才找回她，无论怎样都好，我绝对不要她讨厌我……！！"
    stop music
    stop sound
    mei_speaking "……"
    mei_speaking "怎么会……"
    scene bg_black with dissolve
    $ renpy.sound.play(sound.stressed, channel="sound", loop=True)
    $ renpy.sound.play(sound.pencil_final, channel="nature", loop=True)
    $ renpy.sound.play(sound.pencil_2, channel="extra_1", loop=True)
    mei "我完全呆住了，甚至没有时间去思考对话中代表的含义。"
    mei "剧烈的抽泣声和断断续续的说话声变成无意义的噪音，四面八方，从耳朵进入大脑，把一切绞成无序的碎片。"
    mei "一团乱麻中，我突兀地抓住一条可以听见的声音。"
    stop sound
    stop nature
    stop extra_1

    $ renpy.sound.play(sound.pencil_breaking, channel="sound", loop=False)
    show glitches with dissolve
    young_peng "我，我才不会哭呢，那样太丢脸了！"
    young_peng "但是但是，阿雨你哭的话就没关系，我会帮你打掩护的！"
    stop sound
    hide glitches with dissolve
    $ renpy.music.play(music.peng_after_school_2, channel="music", loop=True)
    mei "……"
    mei "我后知后觉地意识到，那时候说的玩笑话，彭江丽真的做到了。"
    mei "至少……在我认识她的时间里，她从来没有流过眼泪。"
    mei "这是……我第一次见到她哭。"
    stop music fadeout 0.5
    return