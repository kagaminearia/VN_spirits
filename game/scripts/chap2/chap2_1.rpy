label chap2_1:
    stop sound
    scene bg_meiliv with Fade(1.5,0.5,1)
    $ renpy.music.play(music.xiang_spirits, channel="music", loop=True, fadein=0.5)
    mei "客厅的顶灯也许是年代太久了，在晚上显得有些昏暗，竟然将向夏的脸庞盖上一层诡秘的阴影。{p}不，那只是我自己产生的错觉……"
    stop sound
    $ renpy.sound.play(sound.summer_night, channel="sound", loop=True, relative_volume=0.8, fadein=0.5)
    show meiimg shirt at char_left with dissolve
    mei_speaking "那是什么意思？"
    show xiangimg o at char_right with dissolve
    xiang_speaking "嗯……神明，信仰，妖精，鬼怪，各种传说故事啥的，不是经常有这样的嘛，你没听过？"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "是听过，但，跟现在你说的有什么关系？"
    hide xiangimg
    show xiangimg eye_close o at char_right
    xiang_speaking "哎呀，你还没懂吗，我来这里就是为了这个呀！"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "本来想直接找路过的人问的，但是没有人理我。我也感觉一开始有点莽撞，所以只能慢慢来了，然后我发现你就是个好人选！"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "只要跟我说一些相关的就可以了，既然你也在这里生活，肯定是知道的吧。比如有什么神秘的故事还有文化之类的。"
    hide xiangimg
    show xiangimg laugh at char_right
    xiang_speaking "啊，还有还有，一般来说会有什么求神的仪式吧？对了……"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left 
    mei_speaking "等等等等……"
    stop music
    hide meiimg
    show meiimg shirt eye_wacky at char_left 
    mei "眼看着她越说越兴奋，我赶紧打断了她，结果她反而一副很不理解的样子。我无奈地捏了捏眉心，甚至已经隐隐感觉到了乏意。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "嗯？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "你说的，我不知道。\n你之前应该听叶成华说过吧，我是最近才回来的，之前不住在这里。"
    mei "虽然其实很小的时候是在这里住……不过这些事也没必要跟她讲，实在麻烦。只要跟她说我不知道就行了。"
    mei "其实，关于立涧村，我就只知道自己以前住过，以及这里好像发展渔业，除此之外什么都不知道。或许，还不如她这个外来人。"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "好吧……不好意思啊。"
    mei "嗯，这样她也知道该放弃了吧……"
    stop sound fadeout 0.5
    $ renpy.sound.set_volume(1.0, 0, channel="sound")
    hide xiangimg
    show xiangimg fist smile at char_right
    $ renpy.music.play(music.xiang_first_meet, channel="music", loop=True, fadein=0.5)
    xiang_speaking "要不你帮我问问其他人？可以吗？"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left 
    mei_speaking "……哈？！"
    mei "我过于震惊，以至于没忍住发出了声音。"
    hide xiangimg
    show xiangimg fist eye_squint smile at char_right
    xiang_speaking "你看啊，不管怎么说，你总比我更熟悉这里。比如，可以问问你的姐姐，或者你那个朋友也可以呀。我肯定不方便说，所以你能不能帮我问一声，这比之前还方便吧。"
    hide meiimg
    show meiimg shirt eye_wacky at char_left 
    mei_speaking "……"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "你什么都不知道，为什么要找？"
    mei "这么说会不会太没礼貌了……但是，我现在的确很困惑，或许，还有些好奇。\n之前还想问她为什么过来这里，一直没机会，没想到她先自己说了。"
    mei "正因为说了，才让我更加疑惑。这理由实在有些随便，却让她如此执着。一个人就这么直接过来，和叶成华搞出个离谱协议，也毫不避讳地找我帮忙。甚至即使是现在，听我这么问完全没有生气，反而似乎更加高兴。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "所以，你现在终于产生兴趣了吗？"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "算是。"
    mei "虽然认识她不久，但我不觉得她像是会有什么信仰的人……"
    hide xiangimg
    show xiangimg fist eye_squint smile at char_right
    xiang_speaking "其实，我是个很信鬼神的人哦。"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "嗯？"
    xiang_speaking "看不出来吗？"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "看不出来。"
    mei "我面无表情地点头，向夏反而笑得很开心。"
    hide xiangimg
    show xiangimg fist eye_close laugh at char_right
    xiang_speaking "那我才不告诉你呢。"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left 
    mei_speaking "……哈？"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "要是我现在就直接跟你说了，你不就不会再有兴趣了吗。那你还怎么帮我呀。等你帮我之后我再告诉你，这样也可以吧？"
    hide meiimg
    show meiimg shirt eye_wacky at char_left 
    mei "我听着她侃侃而谈，只觉得竟然无法反驳……\n不是吧，至于吗……"
    hide meiimg
    show meiimg shirt eye_close o at char_left 
    mei "她真是如此执着，为了这样的目的特地到这里来……\n我无奈地叹了口气，总感觉不忍心说什么，又觉得是自己被她说服了。"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "我，试试吧，但不能保证。"
    hide xiangimg
    show xiangimg fist eye_squint laugh at char_right
    xiang_speaking "真的吗？太好了！那——"
    mei_speaking "之后说，我现在累了。"
    hide xiangimg
    show xiangimg fist eye_squint smile at char_right
    xiang_speaking "噢……好吧好吧。没事，我不逼你的。\n那，晚安！"
    mei_speaking "嗯。"
    stop music fadeout 0.5

    scene bg_meihome with Fade(1.5,1,1.5)
    show pengimg o at char_right with moveinright
    peng_speaking "……"
    show meiimg at char_left with moveinleft
    mei_speaking "……"
    hide pengimg
    show pengimg at char_right
    mei "虽然答应了向夏，但真正开口还是难以启齿——我和彭江丽的关系才刚刚和缓一些，我可不想又回归原点。{p}但话都答应了，我也只好磕磕绊绊说完。"
    mei "于是……现在我在令人不安的沉默中，等着彭江丽的回答。"
    hide pengimg
    show pengimg o at char_right
    $ renpy.music.play(music.peng_awkward_talk, channel="music", loop=True, fadein=0.5) 
    peng_speaking "原来这就是她来这里的原因啊……"
    mei_speaking "嗯，应该是。"
    hide pengimg
    show pengimg at char_right
    peng_speaking "所以，你们已经这么熟悉了吗？"
    hide meiimg
    show meiimg o at char_left 
    mei_speaking "诶？有吗……"
    mei "我不知道她为什么问这个，也摸不准她的语气，只好含糊其辞。"
    hide pengimg
    show pengimg eye_still at char_right
    peng_speaking "她都把这件事跟你说了，怎么不去跟别人说啊。"
    mei_speaking "呃，可能，她不认识别人……"
    hide pengimg
    show pengimg eye_still o at char_right 
    peng_speaking "那她之前不也不认识你吗，你们也才刚认识而已。"
    hide meiimg
    show meiimg at char_left 
    mei_speaking "嗯……"
    hide pengimg
    show pengimg eye_care o at char_right 
    peng_speaking "啊，对不起，就是，我不是怪你的意思……我就是，有些担心你，被人利用之类的……你也不知道她到底是什么人，又住那么近……"
    hide pengimg
    show pengimg eye_care at char_right 
    peng_speaking "对不起，我不是想让你生气的。"
    hide meiimg
    show meiimg smile at char_left
    mei_speaking "我知道的，不会生气。"
    mei "我知道彭江丽是关心我才会这么激动，也不会像她想的那样生气。只是，我当然也不希望她为了这些气到自己。"
    mei_speaking "之前是想，可以试一下。如果你不想说，或者，没问到她想要的，我也不会让她强迫我，或者你的。"
    hide pengimg
    show pengimg eye_care o at char_right
    peng_speaking "嗯，那，那就好……"
    stop music fadeout 0.5
    hide meiimg
    show meiimg at char_left 
    mei_speaking "那……这件事，你怎么……？"
    hide pengimg
    show pengimg at char_right 
    peng_speaking "这个啊，这还真是……\n就算我说了……我觉得应该很难满足她的愿望吧，她……"
    hide meiimg
    show meiimg o at char_left 
    mei_speaking "没事的，她只是让我问你，也没说一定要回答。"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "如果能帮到忙的话也可以试试，我不说的话，她还会继续纠缠你的吧。"
    hide meiimg
    show meiimg at char_left 
    mei_speaking "……啊。"
    mei "我刚想说“应该不会”，但想了想，又觉得可能是向夏能做出来的事，于是只好硬生生止住话头。"
    hide meiimg
    show meiimg smile at char_left
    $ renpy.music.play(music.peng_hanging_out, channel="music", loop=True, fadein=0.5)
    mei_speaking "你真好。"
    hide pengimg
    show pengimg red at char_right
    mei "我脱口而出，彭江丽的表情顿时变得不太自然，搞得我也有些尴尬。不过，我夸她，应该不会让她不开心……"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "呃，嗯，但是我要补课，也有别的事情，平时的时间不太确定。所以，没办法很快答应……之后我找到机会再跟你说。应该没关系吧？"
    hide meiimg
    show meiimg o at char_left 
    mei_speaking "当然。不过，我现在是，有打扰你吗？"
    hide pengimg
    show pengimg smile at char_right
    peng_speaking "没事没事，我这不是马上就要走了嘛，就是路过来找你一下。\n那我先走啦，下次见。"
    mei_speaking "好。下次见。"
    stop music fadeout 0.5

    scene bg_pengliv with fade
    show xiangimg smile at char_right with moveinright
    $ renpy.sound.play(sound.bird_chirping_2, channel="sound", loop=True, fadein=0.5)
    xiang_speaking "你们家也好大啊，村里的房子真是不错。\n啊，我能坐这儿吗？"
    show pengimg shirt at char_left with moveinleft
    peng_speaking "……\n坐这边就行。"
    show meiimg shirt o at char_mid with moveinleft
    mei_speaking "那个，你自己没关系吗？"
    hide pengimg
    show pengimg shirt smile at char_left 
    peng_speaking "没事，是我请你们过来玩，怎么能让你们做事。"
    hide pengimg with moveoutleft
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "嗯，好……"
    stop sound fadeout 0.5
    hide xiangimg with moveoutright
    $ renpy.music.play(music.awkward, channel="music", loop=True, fadein=0.5)
    mei "向夏已经很自然地坐下，这倒也没什么。只是我有点担心彭江丽，总觉得她看上去兴致不高。但她这么说了，也只好点点头。"
    mei "之前，她说她和向夏也不熟，与其干坐着谈话，不如一起吃顿饭。{p}至于为什么是把我们请到她家来……自然是她不相信我和向夏的做饭水平。"
    hide meiimg
    show meiimg shirt eye_still at char_mid
    mei "唉，这的确是有理有据……虽然只有那一次意外，但总归还是更稳妥些好。"
    show xiangimg o at char_right with moveinright
    xiang_speaking "对了，我们真的不用帮忙吗，一个人做饭应该很久吧。"
    hide meiimg
    show meiimg shirt o at char_mid
    mei_speaking "你能做吗。"
    hide xiangimg
    show xiangimg at char_right 
    xiang_speaking "当然可以了，而且你不也可以吗，最近都是轮流做的饭啊。\n{size=30}虽然可能味道上不是那么好……{/size}"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "……\n等等就好了。"
    mei "恐怕我们两个加起来也没有彭江丽的效率高……"

    scene bg_pengliv with pixellate
    show q_m10 at cg_s with dissolve
    mei "等的时间不久，很快她就把餐桌布置完。一张圆桌，我坐在彭江丽和向夏的中间。{p}毕竟她们不熟……"
    mei "只是，我在人群中向来存在感很低，这个座位实在令我有些坐立难安。"
    stop music fadeout 0.5

    scene bg_pengliv with pixellate
    show xiangimg fist smile at char_right with moveinright
    xiang_speaking "现在我们要讲这边的传说了吗？"
    show pengimg shirt at char_left with moveinleft
    peng_speaking "嗯，好。不过我知道的不多，也可能跟你想的不一样，总之……你别抱有太大期望。"
    hide xiangimg
    show xiangimg fist laugh at char_right
    xiang_speaking "不会不会！你能告诉我就很好了，我不挑的。"
    mei "好直接的开场啊……我还以为她们会先说些闲话。"
    hide pengimg
    show pengimg shirt o at char_left
    $ renpy.music.play(music.calming_guitar, channel="music", loop=True, relative_volume=0.7, fadein=0.5)
    peng_speaking "这些是我以前在一个姐姐那里听来的事。以前，立涧村的确有深厚的，对于灵的信仰。"
    hide xiangimg
    show xiangimg fist o at char_right
    $ renpy.music.set_pause(True, channel="music")
    xiang_speaking "啊，抱歉，谁？这是人名吗？"
    hide pengimg
    show pengimg shirt at char_left
    peng_speaking "立涧村，是这个地方的名字。"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "噢，我说呢，抱歉啊，我们说话的有些发音好像不一样，我刚没听清。"
    hide pengimg
    show pengimg shirt eye_still at char_left
    $ renpy.music.set_pause(False, channel="music")
    peng_speaking "……没事。"
    hide pengimg
    show pengimg shirt o at char_left
    peng_speaking "以前这里有对于灵的信仰，其实现在也有，只不过因为很多因素，不会像以前那样普及了。"
    hide xiangimg
    show xiangimg fist o at char_right 
    $ renpy.music.set_pause(True, channel="music")
    xiang_speaking "就是说，现在也没什么人信这个了吗？"
    peng_speaking "也不是，要说不信也没有，只是，可能在很多时候显得没有那么重要了吧。"
    peng_speaking "就像在其他地方，其实好像根本没有这些说法……以前的故事在他们看来都过时了，也没什么稀奇的，我们这里，当然也会被影响。"
    hide xiangimg
    show xiangimg fist at char_right 
    xiang_speaking "唔，好像是这样，即使是最偏僻的地方，只要和别的地方还有联系就会有影响吧。"
    hide pengimg
    show pengimg shirt at char_left
    $ renpy.music.set_pause(False, channel="music")
    peng_speaking "嗯……"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "所以我找得可辛苦了，真的太感谢你了，我需要给你付钱吗？可以麻烦你把知道的都告诉我吗？"
    hide pengimg
    show pengimg shirt o at char_left
    peng_speaking "不用不用，我也没帮到什么，这些东西你去问其他人也是一样的。"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "她们都不跟我说，还用很奇怪的眼神看我，我以为不太合适呢，所以后来才找梅雨问的。"
    mei "是你看上去太吓人了吧……我差点一个顺嘴直接说出声音。{p}还是听着就好，现在就让她俩说话吧。"
    peng_speaking "可能她们有点忙，也不习惯跟陌生人说话。对了，说了这么久，你不吃点东西吗？"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "噢噢我感觉这个味道有点重，不太适应。而且我吃饭很快，不方便说话，我待会晚点吃吧，我想先问点别的，比如……"
    stop music
    hide pengimg
    show pengimg shirt eye_angry at char_left
    $ renpy.music.play(music.peng_angry, channel="music", loop=True, fadein=0.5, relative_volume=1.0)
    peng_speaking "算了吧。"
    hide xiangimg
    show xiangimg fist eye_squint o at char_right 
    xiang_speaking "啊？"
    hide pengimg
    show pengimg shirt eye_still o at char_left
    peng_speaking "不吃饭多不好啊，这都几点了，嗯……我这的东西不好吃，抱歉啊，你们都回去吃吧。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "啊？不不不，我可以的，那我一边吃一边问你……"
    hide pengimg
    show pengimg shirt eye_still at char_left
    peng_speaking "抱歉，我待会还有事呢，所以可能，呃，可能不太方便。"
    mei "糟了……"
    show meiimg shirt eye_shock at char_mid with moveinleft
    mei_speaking "那我们回去了，今天打扰你了，不好意思。"
    hide pengimg
    show pengimg shirt eye_angry at char_left
    mei "彭江丽的语气和表情让我心下瞬间一沉。我来不及想太多，赶紧抢在向夏开口之前说话。"
    hide xiangimg
    show xiangimg fist eye_still o at char_right 
    xiang_speaking "诶？啊……"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "那个，下次再找你玩，拜拜。"
    hide pengimg
    show pengimg shirt eye_still at char_left
    peng_speaking "好，拜拜。"
    stop music fadeout 0.5


    scene bg_vil5 with fade
    show meiimg shirt at char_left with moveinleft
    mei_speaking "……"
    show xiangimg fist eye_still o at char_right with moveinright
    xiang_speaking "我是不是说错话了？"
    $ renpy.music.play(music.fatigue, channel="music", loop=True, fadein=0.5)
    mei "我看着向夏，竟然不知道该有什么反应。{p}说生气，我好像没有生气的资格，说难过，可能也不至于。但，心里确实莫名有种堵着的感觉。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "应该是。"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    xiang_speaking "对不起……可，为什么呀？"
    mei "我摇摇头，刚才的应对只是条件反射，但说实话，我之前连跟人说话的次数都很少，更不知道该怎么处理这种情况。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei "唉……"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "这可怎么办……我让她这么生气，那我的问题岂不是问不了了？我还能挽回一下吗，找点什么办法？"
    return