label chap8_p1:
    scene bg_meiroom with fade
    show pengimg shirt eye_care at char_right with moveinright
    $ renpy.sound.play(sound.cicada, channel="sound", loop=True, fadein=0.5, relative_volume=0.1)
    peng_speaking "那个，这道题好像错了……"
    hide pengimg
    show pengimg shirt eye_care o at char_right 
    peng_speaking "这里是52吗？"
    peng_speaking "这边也……"
    show meiimg shirt eye_still shell at char_left with dissolve
    mei_speaking "……"
    hide meiimg
    show meiimg shirt shell at char_left
    mei_speaking "抱歉。"
    scene bg_meiroom with dissolve
    mei "我无力地放下笔，疲惫到连一句多余的解释都说不出。"
    mei "其实我已经找借口休息两天了，但今天的状态似乎还是很差。"
    mei "本来说好要和彭江丽一起学习讲题的，但那天之后……我再次面对她的时候只觉得浑身不自在，手不是手，脚不是脚。"
    show halfblack with dissolve
    mei "要是，我当时没有偷听就好了……"
    hide halfblack with dissolve
    show pengimg shirt eye_care o at char_right with moveinright
    peng_speaking "你不舒服吗？对不起，都怪我不好，是我太麻烦你了，还是休息一阵吧？"
    peng_speaking "要喝点水吗？要不要去床上躺一会？要不，我先回去了，让你自己待着？"
    mei "不要这样说自己……"
    show meiimg shirt o shell at char_left with dissolve
    mei_speaking "不……都不用，抱歉。我坐一会就好。"
    scene bg_black with dissolve
    mei "最后，我还是只能说出这样的话。我实在，很不擅长说谎。"
    mei "要隐瞒自己的情绪原来是这么困难的事。"
    mei "那……彭江丽，如果她真的是那么想……\n她又是怎么度过跟我一起的每一天的？"
    mei "她……究竟隐藏了多久？"
    mei "我不知道，也不敢继续往下想。"
    mei "我不想就这么装傻，无条件接受她的好意，却也不知道该如何面对她的感情。\n即使是现在，她那天的哭泣仍然会回荡在我的脑海里。"
    mei "真是的，我之前还真敢说，说什么她是最重要的人……我对她的感情，真的比得上她对我的吗？我到底，对她是什么想法……？"
    mei "这样沉重的、真实的感情……我真的，能够回应吗？"
    stop sound fadeout 0.5

    scene bg_meiroom with dissolve
    show pengimg shirt eye_care o at char_right with moveinright
    $ renpy.music.play(music.time_alone, channel="music", loop=True, fadein=0.5, relative_volume=1.2)
    peng_speaking "啊……梅雨，你还是不舒服吗？哪里难受？"
    peng_speaking "其实我本来上课机会就很少，平时都是自己在家里看书的。你就算只帮我看一道题，就已经比平时的进度快很多了。所以——"
    hide pengimg
    show pengimg shirt eye_care at char_right
    peng_speaking "所以，你不要因为这事难受……"
    hide pengimg
    show pengimg shirt eye_care at char_right
    peng_speaking "……好不好？"
    show meiimg shirt eye_still smile shell at char_left with moveinleft
    mei_speaking "我……我真的没事，谢谢你。"
    hide meiimg
    show meiimg shirt eye_still shell at char_left
    mei "我抬头，对她笑了笑。但也许这个笑容并不好看……因为，她担忧的表情并没有任何和缓的意思。"
    hide pengimg
    show pengimg shirt o at char_right
    peng_speaking "啊我知道了，我们找一天时间出去玩吧？要不就今天吧？"
    peng_speaking "不过，我们最远只能去镇上，跟你们那里比起来也没什么好玩的……但是我想让你放松一些，暂时不要想课本里的事情了好不好……"
    hide pengimg
    show pengimg shirt at char_right
    mei "我在呆愣的时候，彭江丽还在说话，在为我考虑。"
    mei "必须要打起精神才行……"
    hide meiimg
    show meiimg shirt o shell at char_left
    $ renpy.music.play(music.time_alone_2, channel="music", loop=True, relative_volume=1.2)
    mei_speaking "你之前出去玩过吗？"
    hide pengimg
    show pengimg shirt o at char_right
    peng_speaking "什么？没有啊，这里过去也没那么方便，我就是假期要上学才会过去。"
    hide meiimg
    show meiimg shirt shell at char_left
    mei_speaking "原来是这样……"
    hide pengimg
    show pengimg shirt smile at char_right
    peng_speaking "所以要不要今天休息一下，去镇上可以吗？你想去吗？"
    hide meiimg
    show meiimg shirt eye_close shell at char_left
    mei_speaking "我……嗯，好啊。"
    mei "我犹豫片刻，还是点了点头。"
    hide pengimg
    show pengimg shirt eye_squint laugh at char_right
    peng_speaking "太好了！那我先把这些东西收一下，然后再……"
    scene bg_meiroom with dissolve
    mei "窸窸窣窣的声音传来，过了一会，却又逐渐消失，连彭江丽也没再说话。"
    mei "我用力捏了捏眉心，后知后觉地感觉到不对。\n刚才走神太久，我慌忙回神，却只看到彭江丽怔怔地盯着我的笔记本看。"
    show meiimg shirt o shell at char_left with dissolve
    mei_speaking "……彭江丽？"
    show pengimg shirt o at char_right with dissolve
    peng_speaking "这是你最近写的题目吗？"
    hide meiimg
    show meiimg shirt shell at char_left 
    mei_speaking "啊？是啊……"
    stop music
    mei "我没搞懂她突如其来的态度，一时间有些惴惴不安。"
    hide pengimg
    show pengimg shirt at char_right 
    peng_speaking "都是给我讲的题目。"
    mei_speaking "嗯，我得先准备——"
    peng_speaking "没有别的。"
    hide meiimg
    show meiimg shirt o shell at char_left 
    mei_speaking "……啊？"
    hide pengimg
    show pengimg shirt eye_care o at char_right 
    peng_speaking "你不是说要一起复习，准备明年的重考吗？为什么只有我问你的题目，为什么你没有别的资料，为什么——"
    hide pengimg
    show pengimg shirt eye_care at char_right 
    mei "她的声音戛然而止，最终还是没能说下去，我也终于明白她的意思，却只好低下头。"
    hide meiimg
    show meiimg shirt eye_still shell at char_left 
    $ renpy.music.play(music.time_alone_2, channel="music", loop=True, relative_volume=1.2)
    mei_speaking "……抱歉。"
    hide pengimg
    show pengimg shirt eye_still at char_right 
    peng_speaking "我……你……你怎么能这样……"
    mei "彭江丽的声音很小，我悄悄抬起眼皮，只看到她的头垂得很低，完全看不清表情。"
    mei "我心口一悸，硬生生从缩紧的喉咙里挤出话语。"
    hide meiimg
    show meiimg shirt eye_still o shell at char_left 
    mei_speaking "对不起，是我不敢。"
    hide pengimg
    show pengimg shirt eye_still o at char_right 
    peng_speaking "……什么不敢？"
    hide meiimg
    show meiimg shirt eye_close o shell at char_left 
    mei_speaking "……我不敢看前面的题目，每次看到都会想起之前在考场上晕倒。"
    mei_speaking "所有人都说最重要的时候，唯一能够证明我自己的时候，然后我晕倒了。"
    hide meiimg
    show meiimg shirt eye_close shell at char_left 
    mei_speaking "醒来之后，很多人围着，怜悯地看我。"
    hide meiimg
    show meiimg shirt eye_still o shell at char_left 
    mei_speaking "反正……就是这种破事。"
    hide meiimg
    show meiimg shirt eye_close shell at char_left 
    mei "我平铺直叙，没有任何起伏地说完，叹了口气。只是……我的真实心情要是也能真的毫无波澜就好了。"
    hide pengimg
    show pengimg shirt eye_still at char_right 
    peng_speaking "……"
    hide pengimg
    show pengimg shirt eye_still o at char_right 
    peng_speaking "对不起，是我错了，我不该让你想起这些的。"
    peng_speaking "我，我不应该……不应该这么麻烦你。"
    hide meiimg
    show meiimg shirt o shell at char_left 
    mei_speaking "啊，不……"
    hide pengimg
    show pengimg shirt eye_still at char_right 
    peng_speaking "可是，我还是想问……对不起，就是……"
    hide pengimg
    show pengimg shirt eye_care at char_right 
    peng_speaking "梅雨不想重新考试的话，之后有什么打算呢？"
    hide meiimg
    show meiimg shirt shell at char_left 
    mei_speaking "……"
    mei "这没什么惊讶的，每个人大概都会问。就连叶成华当时带我回来，也是希望我休息好之后能自己想清楚。"
    mei "虽然叶成华跟我说过不用着急这些事，但我也不可能永远欺骗自己，永远只是在逃避。"
    hide meiimg
    show meiimg shirt eye_close shell at char_left 
    mei "我……"
    hide pengimg
    show pengimg shirt  at char_right 
    peng_speaking "你会继续留在村里吗？"
    hide meiimg
    show meiimg shirt eye_still shell at char_left 
    mei_speaking "……不知道。"
    hide meiimg
    show meiimg shirt o shell at char_left 
    mei_speaking "你呢？"
    hide pengimg
    show pengimg shirt eye_still o at char_right 
    peng_speaking "我，我想离开这里。"
    mei "她说着，低下了头，我也没再说话。"
    mei "其实我不问也应该知道。她如此努力，在条件不好的这里也总是抓住机会，当然是想要得到更好的结果。"
    hide pengimg
    show pengimg shirt o at char_right 
    peng_speaking "啊，但是，我不是要继续麻烦你的意思。如果你觉得烦，不要再看这些资料也没关系的。我，我自己也可以。"
    hide meiimg
    show meiimg shirt eye_still shell at char_left 
    mei_speaking "嗯……"
    mei "但我其实也想跟她一起啊……我也想，做自己能做的事……这么想着，我却没法说出口。"
    mei "她就和我以前的同学一样，不，比她们还要努力更多。正因如此，看到她，更让我自惭形秽……"
    show bg_black with dissolve
    mei "我连这种事也……"
    hide bg_black with dissolve
    peng_speaking "梅雨……"
    hide meiimg
    show meiimg shirt shell at char_left 
    mei_speaking "……啊。"
    hide meiimg
    show meiimg shirt eye_still shell at char_left 
    mei "彭江丽十分担心地看着我，我敛下眉毛，不知道该如何回应。"
    hide meiimg
    show meiimg shirt eye_still o shell at char_left 
    mei_speaking "我怎么，才能跟你一样？"
    peng_speaking "哎？什，什么？什么要跟我一样？"
    hide meiimg
    show meiimg shirt eye_still shell at char_left 
    mei_speaking "像你一样，可以很勇敢地……"
    hide pengimg
    show pengimg shirt eye_care at char_right 
    peng_speaking "……我一点也不勇敢。"
    hide pengimg
    show pengimg shirt eye_still at char_right 
    peng_speaking "{size=30}只是因为你……{/size}"
    hide pengimg
    show pengimg shirt at char_right 
    peng_speaking "{size=30}但是……{/size}啊，我……我知道了！"
    hide pengimg
    show pengimg shirt o at char_right 
    peng_speaking "我跟你一起的话，一定可以的！"
    hide meiimg
    show meiimg shirt o shell at char_left 
    mei_speaking "……哎？"
    peng_speaking "就是……让我来帮你吧！"

    scene bg_meiroom with Fade(0.2,0.5,0.3)
    $ renpy.music.play(music.time_alone_3, channel="music", loop=True)
    peng_speaking "‘……在第二段中……表达了什么……’"
    peng_speaking "读完了。"
    mei_speaking "嗯……选B？"
    peng_speaking "对了！"
    peng_speaking "太厉害了，我就说你肯定可以的！"
    mei_speaking "扑哧……"
    mei "我还是忍不住小声地笑出来，不知道是因为被夸奖觉得开心，还是被我们现在的情况逗笑了。"
    mei_speaking "……太浪费时间啦。"
    peng_speaking "不会一直这样的，慢慢来，会好的！"
    mei_speaking "……"
    peng_speaking "现在我就帮你念复习资料和题目，不要你自己看，你慢慢熟悉之后，就不会那么抵触了。"
    peng_speaking "就算我一直念也没关系，你在其他地方帮我赶回时间就行了啊！"
    mei_speaking "……"
    peng_speaking "我们不是说互相帮助吗？你都不让我帮你，我也不好意思再听你讲题目啦。"
    mei_speaking "嗯……"
    mei "她都这么说了，我只好点头。只是，我对自己还是没什么信心……\n这样真的可以吗，我真的还可以面对吗……"
    mei "但，如果真的可以，说不定……"
    mei_speaking "谢谢你。"
    peng_speaking "是我要谢谢你才对。"
    mei_speaking "不，是我——"
    peng_speaking "那，那你要谢谢我的话，之后就一起加油吧！"
    mei_speaking "……{p}好。"
    stop music fadeout 0.5
    return
