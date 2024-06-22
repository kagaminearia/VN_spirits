label chap9_x2:
    scene bg_meiroom with fade(color="#fff")
    $ renpy.music.play(music.calming_piano, channel="music", loop=True, fadein=0.5)
    mei_speaking "啊——"
    $ renpy.sound.play(sound.bird_chirping_1, channel="sound", loop=True, fadein=0.5)
    mei "我从床上起来，长长地喘了一口气。昨晚没睡好，现在天已经大亮。"
    mei "但，我却还不想下楼吃早餐。"
    mei_speaking "做些别的吧……"
    stop sound fadeout 0.5

    scene bg_meiroom with pixellate
    mei_speaking "……难以置信。"
    $ renpy.sound.play(sound.pencil_2, channel="sound", loop=False)
    mei "我的手指紧紧地捏着笔，看着笔尖落在方正的黑色文字上。台灯的光线被挡住些许，在纸上留下浅浅的影子。"
    mei "这一次，那些纸上的墨水并没有扭曲，清晰地烙印在我的视野里。"
    $ renpy.sound.play(sound.pencil_3, channel="sound", loop=False,relative_volume=0.8)
    mei "第一题，第二题，第三题……笔尖在纸面上发出沙沙的声音，由慢变快。"
    show bg_line1 at cg_1, shaking
    mei "我好像又回到那个教室。周围都是人，我紧张地喘不上气。然后，下一秒，我就会晕倒……"
    mei "不，不是。现在已经不是那个时候了……"
    hide bg_line1 with dissolve
    mei "心脏有些憋闷，像是被东西压得难受。但没关系……\n我咬咬牙，继续写下去。"
    stop music fadeout 0.5
    scene bg_meiroom with pixellate
    mei "笔记本上新加的字不好看，但题目已经被写满。"
    mei "没想到……我本来只是想让自己不去想向夏的事，才选择逼自己一把，选择我本来更不想面对的东西。"
    mei "没想到……我竟然能够重新写完题目。"
    mei "看到它们，我仍然会感到疼痛，但……也许已经没那么害怕了。也许，即使害怕，也不会那么想躲避了。"
    mei_speaking "这……算是一个好消息吧。"

    scene bg_meiliv with fade
    $ renpy.music.play(music.summer_wind, channel="music", loop=True, fadein=0.5)
    mei_speaking "之前放哪了来着……好乱……"
    show xiangimg o at char_right with moveinright
    xiang_speaking "你这是在干啥？"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "咦？啊，我，呃，在找东西……"
    mei "我在客厅翻箱倒柜的时候，向夏忽然从旁边冒出来，吓得我手一抖，差点把纸洒了一地。"
    mei_speaking "之前暴风雨的时候，家里不是清过一遍吗，我有几本笔记本不知道后来扔哪了。"
    xiang_speaking "那种东西难道不应该在你房间里吗？你怎么在客厅找。"
    hide meiimg
    show meiimg shirt eye_close o at char_left 
    mei_speaking "这个嘛……我其实没随身收好，所以不在卧室，应该在外边的某个柜子里。"
    hide meiimg
    show meiimg shirt eye_close at char_left 
    mei "之前……我光是看到它们都会感到窒息，更加不想面对，会一起带过来完全是因为顺便，也只在贴身背包里留了一本。"
    hide meiimg
    show meiimg shirt at char_left 
    mei "但今天既然能写那本的题目，其他的，我也想重新翻来看看……"
    mei "我把手里的纸张塞回去，拉开别的柜子，终于找到了一沓厚厚的笔记。"
    xiang_speaking "哇，还真多。我能看看吗？"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "什么？随你啊……"
    mei "反正，只是我以前上学写过的资料罢了……比起这些，现在的向夏反而让我更加紧张，也不知道她为什么又能变回神色自如的样子。"
    mei "明明，昨天觉得，不像以前那样聊天了很难受，可现在看到她若无其事的样子，我的难受并没有减少。"
    mei "为什么会这样……我到底是……"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "这也太多了吧，上学还真是辛苦。"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "……还好。"
    mei "既然她也没有讨厌的意思，我干脆把本子和纸一次性拿出来，全部摊开在地上。"

    scene bg_meiliv with pixellate
    show xiangimg fist o at char_right with dissolve
    xiang_speaking "那你之前都没收，现在把这些东西拿出来干啥啊。"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "嗯……我在想，这些该怎么处理。\n因为，我现在……"
    mei "虽然之前已经说过了，但我还是不太习惯自己提到这些事。\n于是我只是摩挲着纸张，试图用沙沙的摩擦声响冲淡自己说话的声音。"
    
    scene bg_meiliv with dissolve
    show xiangimg fist o at char_right with dissolve
    xiang_speaking "所以你是说，这些东西现在不打算要了吗？"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "啊？也不是……"
    xiang_speaking "……啊？"
    hide meiimg
    show meiimg shirt eye_close at char_left 
    mei "我抿了抿嘴，也觉得自己这样扭捏实在不好。但是……"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "我今年，不是考试失败了吗，所以嗯，应该要准备重考一次。"
    mei "舌头打结。"
    hide meiimg
    show meiimg shirt eye_still o at char_left 
    mei_speaking "只是我不知道我能不能这么做。"
    show halfblack with dissolve
    mei_speaking "{size=30}因为在之前，之前就是，连这种事我都会出意外，再来一次说不定也是同一个结果……{/size}"
    mei_speaking "{size=30}……但如果这都做不好，我又能做什么。{/size}"
    hide halfblack
    hide xiangimg
    show xiangimg fist eye_still o at char_right 
    xiang_speaking "你，那个？"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "啊？呃，不好意思。"
    mei "我这才发现自己好像又陷入自己的思维里了，而且还发出了声音……向夏看着我，让我不由得有些脸热。\n太尴尬了……"
    hide meiimg
    show meiimg shirt eye_close at char_left 
    mei_speaking "刚刚，当我没说。"
    hide xiangimg
    show xiangimg fist eye_still at char_right 
    xiang_speaking "……"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "好吧——我还想着捧捧场呢。"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "……捧什么？"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "比如，我以为，你希望我提出建议之类的。当然啦，我的建议和陪聊没什么区别。"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "……"
    hide meiimg
    show meiimg shirt eye_still at char_left 
    mei "其实，刚才我说完的瞬间就开始后悔。把这些跟她说又有什么用，再说我们之间也……"
    hide xiangimg
    show xiangimg fist at char_right 
    mei "可是现在听她提起来，我反而意识到，自己的确想得到她的反馈。\n……哪怕随便说点什么也好。"
    mei "她会说什么……会调侃我的幼稚吗，或者是嘲笑我的懦弱呢。"
    hide meiimg
    show meiimg shirt eye_still o at char_left 
    mei_speaking "那你觉得呢？如果是你，之类的……"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "我？我才不要读书咧。"
    hide meiimg
    show meiimg shirt o at char_left 
    mei "向夏脱口而出，惊呆了我。我暂时忘了别的琐碎想法，只是愣愣地盯着她。"
    hide meiimg
    show meiimg shirt at char_left 
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "额……对不起？我不是嫌弃读书啊，这不是没缘分嘛。"
    mei "看到她被我盯得都变了表情，我有些想笑，捏着纸张的手也松了些。"
    hide meiimg
    show meiimg shirt smile at char_left 
    mei_speaking "不用对不起，我又没说什么。"
    xiang_speaking "好吧好吧，你没生气就好。"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "所以，嗯你觉得……做别的更容易吗？"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "问我吗？是啊，我都多少年没有读过书了，真不适合，要我在这方面努力还不如做点别的呢。"
    hide meiimg
    show meiimg shirt eye_close o at char_left 
    mei_speaking "嗯……我是不是也应该放弃？"
    mei "她答得很果断，让我来不及思考，想说的话直接说出了口。"
    xiang_speaking "什么？"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "啊就是，觉得，之前都失败，可能我也不适合吧。"
    hide meiimg
    show meiimg shirt eye_still at char_left 
    mei_speaking "如果做点别的的话……{size=30}像你一样。{/size}"
    mei "向夏没有继续上学，现在看起来也……\n我的话，也可以吗……"
    hide xiangimg
    show xiangimg fist at char_right 
    xiang_speaking "唔，这个问题好难啊，我——"
    stop music
    $ renpy.sound.play(sound.table_smash, channel="sound", loop=False)
    na "砰！"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "……什么声音？我没听错吧。"
    $ renpy.sound.play(sound.pot_drop, channel="sound", loop=False)
    na "梆！"
    hide xiangimg
    show xiangimg fist eye_shock o at char_right 
    xiang_speaking "好，好像是我之前在厨房……"
    hide meiimg
    show meiimg shirt eye_shock at char_left 
    mei "向夏和厨房……我的脑子里突然出现了一些不好的回忆。"
    hide xiangimg with easeoutright
    xiang_speaking "我我我我现在就去看看！"
    mei_speaking "……"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "我也去！"

    scene bg_meikitc with fade
    $ renpy.music.play(music.xiang_first_meet, channel="music", loop=True, fadein=0.5)
    na "滋……滋滋……"
    mei "冰凉的水流落在滚烫的锅底上，接触的表层发出阵阵声响。"
    mei "我盯了一会糊掉的锅底，随后把目光转移到向夏身上。"
    show xiangimg fist eye_squint smile at char_right with moveinright
    xiang_speaking "……啊这个是——"
    show meiimg shirt eye_wacky o at char_left with dissolve
    mei_speaking "意外？"
    hide xiangimg
    show xiangimg fist eye_squint laugh at char_right
    xiang_speaking "对！你真聪明！"
    hide meiimg
    show meiimg shirt eye_wacky smile at char_left 
    mei_speaking "……呵。"
    hide meiimg
    show meiimg shirt eye_wacky at char_left 
    mei "我简直不知道该不该生气。"
    hide xiangimg
    show xiangimg fist eye_squint o at char_right 
    xiang_speaking "真的是意外！本来我就想热一下的，然后听到客厅有声音，出去之后又跟你聊起来才这样的！"
    hide meiimg
    show meiimg shirt eye_close o at char_left 
    hide xiangimg
    show xiangimg fist at char_right 
    mei_speaking "……我知道。"
    hide meiimg
    show meiimg shirt eye_close at char_left 
    mei "好吧，我没法生气了。硬要说的话，这事故也有我的一份力……"
    stop music fadeout 0.5
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "你本来要做什么？"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "想试着做点甜品试试，就是用那天在镇上买的东西。"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "噢……"
    mei "难怪桌子上堆了这么多东西，我还以为是我忘记收了。"
    mei "不过……没想到她还会这个啊。"
    hide xiangimg
    show xiangimg laugh at char_right 
    xiang_speaking "嘿嘿，就是试试，我也没信心，要一起试试吗？"

    scene bg_meikitc with fade
    mei "……我没怎么思考就答应了。好奇怪，之前……我应该不会对周围的事感兴趣。"
    mei "灶台旁边一字排开容器、厨具和原材料，我小心地用刀把水果切碎，推给向夏，而她正用筷子在大碗里粗暴地把水果块捣成糊状。"
    mei "此情此景简直可以称得上温馨……却好像让我的心情变得更加复杂。"
    show xiangimg fist eye_close o at char_right with dissolve
    $ renpy.music.play(music.xiang_cooking, channel="music", loop=True, fadein=1.0)
    xiang_speaking "虽然现在找些零工容易多了，但我还是想找个靠谱点的好一点的工作啊。"
    show meiimg shirt at char_left with dissolve
    mei_speaking "嗯？啊……"
    mei "她突然开口，声音不大，和筷子碰撞产生的哒哒声混在一起，让我下意识附和完才反应过来。"
    mei "不过，为什么突然说这个……"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "之前攒的钱都花了，我应该还要攒一阵，然后打算去大城市找个技术学校学东西。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "学厨，之后就在这方面努力了，不然乱打一气，太累啦。"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "噢……真厉害。"
    mei "我发自内心地感叹，说出来的话却干巴巴的，嘴唇也有些干涩。"
    hide meiimg
    show meiimg shirt eye_still at char_left 
    mei "于是我没再说话，只是默默地看着她。"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    $ renpy.sound.play(sound.boiling_water, channel="sound", loop=True, relative_volume=0.6)
    mei "灶上开了小火，锅里的液体发出咕嘟咕嘟的响声。向夏垂着眼睛，没有看我，只是慢条斯理地搅拌。"
    hide xiangimg
    show xiangimg fist eye_close o at char_right
    xiang_speaking "怎么说呢……"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "嗯？"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "我倒不是觉得非要比较一下高低啥的，也没觉得以前不去读书很后悔。"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "只是我那个时候没有办法选择。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "如果，呃，如果是我有得选，我应该会好好选一下吧。哪怕结果一样，哪怕浪费点时间。"
    hide xiangimg
    show xiangimg fist smile at char_right
    mei "她歪了歪头，对着我笑了一下，我这才反应过来。"
    mei "绕了一圈，原来是要说这个……{p}我的心里好像痒痒的，不知道是什么心情。"
    xiang_speaking "喂，我说了这么多，你怎么还是一副丧气的样子啊？"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "啊？有吗……"
    mei "我下意识地摸了摸脸，随后又意识到摸了我自己也看不到，尴尬地放下了手。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "有的，绝对有。"
    mei_speaking "那——"
    xiang_speaking "反正怎么做都肯定会有坏处，说不定都会后悔，读书啊，工作啊，或者就留在你们这个村里。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "但有得选总比没得选好一些呗。"
    hide xiangimg
    show xiangimg fist laugh at char_right
    xiang_speaking "你这么厉害，肯定能做好自己选的事情啊。"
    hide meiimg
    show meiimg shirt eye_wacky smile at char_left 
    mei_speaking "……哪有……"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "没有你笑什么？"
    hide meiimg
    show meiimg shirt eye_wacky at char_left 
    mei_speaking "我——好吧……"
    hide meiimg
    show meiimg shirt eye_close o at char_left 
    mei "我不得不承认，听到她刚刚的话，我的嘴角好像是上扬了一些。"
    mei "……明知道她说的只是鼓励，一点也不现实，但我还是为此感到高兴。"
    stop music fadeout 0.5
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "对了，刚刚我的东西还没收完就进来了，我去收东西。"
    mei "下意识地，我飞速抛出一个借口，转身就走。"
    mei "向夏的惊诧声从身后传来，我眼疾手快，带上了厨房的门。"
    stop sound

    scene bg_meiliv with dissolve
    mei_speaking "……"
    $ renpy.music.play(music.xiang_crush_talk, channel="music", loop=True, fadein=0.5)
    mei "说好要收东西，但那些笔记本仍然散乱地堆在桌上，而我站在旁边没动，只是瞪着桌上的一小块污渍。"
    mei "刚才的场景顺滑地在我脑中重现，我那行云流水的动作……"
    mei "梅雨啊梅雨，你到底在想什么啊，太丢人了……"
    mei "我长叹一口气，摇了摇头，把本子一股脑揽进怀里，再把它们塞进我自己的背包。"
    mei "好像没什么好收的……我的手指在虚空中握了握，随后，收回袖口。"
    mei "还是回去看看吧，不知道厨房怎么样了……对，我只是担心厨房，只是这样而已。"

    scene bg_meikitc with fade
    show xiangimg fist o at char_right with dissolve
    xiang_speaking "怎么了？"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "哦，就是来看一下你弄完了没。"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "差不多了哦，你来得刚刚好。把这个倒在碗里就可以了。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "噢，好……"
    hide xiangimg
    show xiangimg fist laugh at char_right 
    xiang_speaking "对了，这玩意吃之前要放冰箱冰一阵子，你要不要先尝尝味道？要是不喜欢，现在还能再改改。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "嗯？行啊，听你的。"
    mei_speaking "不过，这玩意怎么吃——"
    scene bg_black with vpunchm
    mei "？！"
    stop music
    show cg_x111 at cg_s with dissolve
    mei "那句话结尾的“尝”字只说到一半，柔软的指尖毫无预兆地落在我的唇边。"
    mei "瞬间，细腻绵密的口感蔓延至整个口腔，带着温热的，淡淡的甜。"
    mei "的确，味道很好……\n但是，但是……"
    show cg_x112 at cg_s with dissolve
    hide cg_x111
    mei "不仅是口腔，我的整个脑袋好像都热了起来。而向夏则是……\n她的脸泛起潮红，动作僵在原地，好像自己也没反应过来发生了什么。"
    xiang_speaking "……"
    hide cg_x112 with dissolve
    mei "几秒的时间被拉得十分漫长，近乎停滞。在我即将退后的时候，向夏猝然撤回手臂，整个人往后弹了将近有一米的距离。"
    mei_speaking "……"

    scene bg_meikitc with dissolve
    $ renpy.sound.play(sound.water_tube, channel="sound", loop=True, fadein=0.5)
    mei "很长一段时间内，房间里都没有说话的声音。只有碗筷的碰撞声，液体的流动声，冰箱打开的声音。"
    show xiangimg fist eye_still at char_mid with dissolve
    xiang_speaking "……"
    hide xiangimg
    show xiangimg fist eye_squint smile at char_mid
    xiang_speaking "对了，感觉怎么样，是不是还挺好吃的？\n啊，我把这个装出来放冰箱，放几个小时，之后就可以随便吃了。"
    hide xiangimg
    show xiangimg fist eye_still smile at char_mid
    xiang_speaking "哦，要不我把它每份分出来，这样会比较好拿，不过就要洗更多的碗。我都可以，看你喜欢哪种。"
    hide xiangimg
    show xiangimg fist eye_still smile at char_mid
    xiang_speaking "……怎么了？"
    mei "不知不觉，我已经走上前，拉近了和向夏的距离。她身高比我高，但只比我高一些，所以，我抬眼，就可以看到她不自然的表情。"
    stop sound fadeout 0.5

    scene bg_meikitc with fade
    show meiimg shirt at char_left with dissolve
    $ renpy.music.play(music.xiang_heartbeat, channel="music", loop=True, fadein=0.5)
    mei_speaking "你又要装作无事发生吗？像之前的事那样。"
    mei "想都没想，我的话不经大脑就出口。但，的确……也许，这就是，我那被堵住的，憋闷而不知从何说起的情感……"
    show xiangimg fist eye_still at char_right with dissolve
    xiang_speaking "……"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "你在说什么？"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "嗯，我说的是昨天晚上的时候，还有之前看花的时候。"
    mei_speaking "你之前也说过吧，你觉得一切都是交易。既然是这样，为什么还要做这些事？"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    xiang_speaking "……"
    mei "向夏张了张嘴，但好一会儿也没发出声音。"
    mei_speaking "你不是最习惯有话直说的吗，为什么现在都学会岔开话题了。"
    xiang_speaking "……"
    hide xiangimg
    show xiangimg fist eye_still smile at char_right
    xiang_speaking "这不是，发现你们说的话有道理嘛。"
    hide xiangimg
    show xiangimg fist eye_squint smile at char_right
    xiang_speaking "你和你的朋友不都说，有些话不想说也是很常见的。我觉得很有道理呀，所以就学习一下。"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "……"
    mei "这算自己给自己挖坑吗……我现在，甚至分不清这是她用来搪塞的借口，还是真心赞同那番“理论”。但是……"
    scene bg_black with dissolve
    mei "……我不想管那么多。"
    mei "在我继续思考之前，我已经将她逼到墙角。"

    show cg_x121 at cg_s with dissolve
    mei_speaking "我记得你之前说，我可以提一个不过分的要求。"
    xiang_speaking "……你不是说你不需要的嘛。"
    mei "向夏的嘴角稍稍撇了撇，声音也变得很可怜的样子。说实话……有点可爱。"
    mei "不，我怎么还在想这个……"
    mei_speaking "我现在反悔了。"
    show cg_x122 at cg_s with dissolve
    hide cg_x121
    xiang_speaking "……"
    mei_speaking "我只是想知道，为什么……要做这些事？"
    xiang_speaking "没有，就是……我不小心做错了，之后不会了，对不起。"
    mei_speaking "……喂，那你——"
    xiang_speaking "都说了我做错了，所以，我也不是想刻意跟你拉进关系。所以别问了，我……"
    show cg_x123 at cg_s with dissolve
    stop music
    xiang_speaking "我很讨厌你。"
    scene bg_black with dissolve
    mei_speaking "……"
    mei "向夏的话出口前，我猜过很多种不同的回答。"
    mei "但没有一种，猜到现在的结果。"
    return