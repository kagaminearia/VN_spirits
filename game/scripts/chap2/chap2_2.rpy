label chap2_2:
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "{size=30}不过，道歉啊……{/size}\n这事估计还得再麻烦你一次。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "嗯？"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "我就算想直接找她也没办法呐。下次找个时间，我来请客一起吃饭吧，跟她当面道歉。"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left
    mei_speaking "……\n这不算重蹈覆辙？"
    xiang_speaking "重蹈覆辙？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "就是，又是吃饭，不会重犯以前的错误吗。"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "噢，好像有道理，那你说怎么办？"
    mei_speaking "……我不知道。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "那不就是了，就先问问，如果她拒绝我再想别的方法？稳妥一点。"
    mei_speaking "好。"
    stop music fadeout 0.5

    scene bg_meiroom with pixellate
    $ renpy.music.play(music.cold_night, channel="music", loop=True, fadein=0.5)
    mei_speaking "……好，烦……"
    mei "吃完药后，我躺在床上辗转反侧。已经到了平时睡觉的时间，我却没有任何睡意。{p}要是之前没有答应向夏就好了……我本来就不常和人说话，现在还被夹在两个人中间，实在是不安而烦躁。"
    mei "如果可以，我根本不想答应这些事。可……彭江丽是我最好的朋友，即使她现在可能已经不这么认为，我还是不希望她难过。"
    mei "我之前听说，彭江丽并不是每天都补课，时间也不长，要抽出空来并不难。只是，难的是怎么控制好跟她的气氛。"
    mei "……现在的我们，只是见一面也需要提前思考这么多了。"
    mei_speaking "唉……"

    show bg_black with dissolve
    mei "身体的疲惫和吃药后的反应来势汹汹，大脑虽然还在被毛线团般的问题困扰，我还是逐渐陷入了深深的睡眠。"
    stop music fadeout 0.5

    scene bg_meiliv with fade
    show xiangimg fist o at char_right with dissolve
    $ renpy.music.play(music.xiang_first_meet, channel="music", loop=True, fadein=0.5)
    xiang_speaking "前几天我不小心冒犯到你，真的对不起了！\n我不是有意的，你要是觉得哪里不对，直接跟我说吧！"
    xiang_speaking "哦对了，一顿饭可能不够……我还需要做什么，你说，我都尽量做。"
    mei "她还是好直接，连铺垫都没有……不只是我，彭江丽也愣住了一瞬间。"
    show pengimg shirt at char_left with dissolve
    peng_speaking "不用这样，我……上次是我有点着急，不用在意了。"
    xiang_speaking "真的吗？你要是哪里不喜欢说出来没关系的。"
    hide pengimg
    show pengimg shirt eye_still at char_left 
    peng_speaking "……没有的。"
    hide xiangimg
    show xiangimg fist at char_right 
    xiang_speaking "那好吧，我听你的。那……这事就算过了？"
    hide pengimg
    show pengimg shirt at char_left 
    peng_speaking "……嗯。就这样吧。"
    mei "她俩的对话磕磕绊绊，像没上润滑油的链条努力向前推进。{p}我只用在旁边听着，倒是轻松不少。"
    mei "这么想不太合适，但我心里似乎莫名生出一种接近于暗爽的情绪——也许是因为看到不止我一个人跟向夏说话很费劲……"
    stop music fadeout 0.5

    scene bg_meiliv with pixellate
    show pengimg shirt at char_left with dissolve
    peng_speaking "之前说到哪来着？嗯，现在的……"
    show xiangimg at char_right with dissolve
    xiang_speaking "我能先问个问题吗，上次没来得及。"
    hide pengimg
    show pengimg shirt o at char_left 
    peng_speaking "什么？"
    hide xiangimg
    show xiangimg o at char_right 
    xiang_speaking "你们说的信仰具体是什么东西啊，是名字就叫“灵”吗，是什么传说里的人物吗，还是别的东西？"
    hide pengimg
    show pengimg shirt at char_left 
    $ renpy.music.play(music.nature, channel="music", loop=True, fadein=0.5)
    peng_speaking "不是的。灵……就是灵。"

    scene video_1 with Fade(1,1,1)
    peng_speaking "这不是名字，也不是任何一个人。\n它的含义比较模糊，但，可以解释成是魂灵，生灵。"
    xiang_speaking "生灵？那算什么，信仰每个小动物吗，为什么？这有什么……不，这样也没办法搞些祭祀什么的吧？"
    peng_speaking "不是小动物。"
    xiang_speaking "啊？"
    peng_speaking "一切的，所有生灵……你知道，“万物有灵”吗？"
    xiang_speaking "万物，有灵？"
    peng_speaking "嗯，尊重且相信世界上的所有生灵，相信它们都有魂灵，拥有同样的灵性。"
    peng_speaking "然后，真的这样相信着，就会有想象不到的事情发生。"
    xiang_speaking "哇哦，酷，竟然还有这种说法，我还是第一次听说。"

    show halfblack with dissolve
    mei "咦……{p}向夏姑且不论，这个说法倒是让我想起来一些事情。"
    mei "很模糊，很遥远……我那时还小，基本不记事，只以为是错觉或者记忆混乱。我妈很忙，几乎没有时间陪我，自然也没有人给我讲过这些传统。"
    mei "所以，那些飞舞的……闪烁的……到底是什么……？"
    mei "那个时候……"

    scene bg_meiliv with fade
    show xiangimg o at char_right with moveinright
    stop music
    xiang_speaking "喂，梅雨！"
    show meiimg shirt o at char_left with moveinleft
    $ renpy.sound.play(sound.bird_chirping_1, channel="sound", loop=True, fadein=0.5)
    mei_speaking "嗯？"
    xiang_speaking "你怎么总是走神啊？你还有什么要说的吗？"
    mei_speaking "没……你们讲完啦？"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "是啊，真的太及时了。原本我是打算，如果这两天找不到什么就走了。但我决定再待一段时间看看，等到那个节日结束之后再离开这。"
    mei_speaking "节日？"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "祝灵节啊，刚刚才说的，你都没听啊。不对，你真的什么都不知道诶，不是也住这里的吗。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "噢……"
    mei "我想起来了，这的确可以说是立涧村最传统，或者说最有那种信仰氛围的日子。"
    mei"那时候大家会聚在广场上，然后，好像有一些歌声和灯光……{p}嗯，不过，我还是不太记得……"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "以前住过，后来搬走了。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "这样啊，难怪难怪，不过，那你怎么现在又回来啦。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "呃……"
    show pengimg shirt o at char_mid with moveinleft
    peng_speaking "我吃完了。"
    mei "哒，桌上发出轻微的响声，仿佛一种打断我们对话的信号。\n彭江丽若无其事地放下筷子，冲着我们笑了笑。"
    xiang_speaking "诶，你吃得好快哦。"
    mei "向夏的注意力似乎被分走了，刚好，我也还没想好怎么搪塞刚才的问题……趁这个机会，别让她再继续纠结这些好了。"
    stop sound fadeout 0.5
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "什么时候祝灵节？"
    hide pengimg
    show pengimg shirt smile at char_mid 
    peng_speaking "下个月月底。"
    mei "还有将近两个月……现在才月初。"
    mei_speaking "你就一直留在在这？"
    hide xiangimg
    show xiangimg fist laugh at char_right
    xiang_speaking "是啊，这里环境挺好的呀，就当给我自己放个假。\n本来没打算花这么久时间，但是一请假就被公司辞退了，也就不用管回去工作的事情啰。"
    hide meiimg
    show meiimg shirt at char_left
    mei "不无聊吗……果然我无法理解她的想法。\n不过，即使我不理解，她一直都知道自己想做什么。"
    mei "不像我……"

    scene bg_meiliv with pixellate
    $ renpy.music.play(music.peng_hanging_out, channel="music", loop=True, fadein=0.5)
    mei "吃完饭后，我照常开始吃药。彭江丽和向夏坐在餐桌旁，有一搭没一搭地讨论除了祝灵节以外的其他部分。\n当然，主要是向夏在问。"
    show xiangimg fist o at char_right with moveinright
    xiang_speaking "话说你每天是吃什么药啊，我平时需要注意什么吗？"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "啊？这个是……"
    show pengimg shirt o at char_mid with moveinleft
    peng_speaking "你们要吃这个吗？"
    xiang_speaking "诶，这是什么？"
    hide pengimg 
    hide xiangimg
    hide meiimg
    show q_candy1 at cg_s with dissolve
    peng_speaking "这边的一种糖，味道还行，梅雨特别喜……欢。"
    mei "她的尾音变得缓慢，大概是看到我毫无反应，于是也不知道该如何接下去。{p}的确……我似乎，应该有反应才对。"
    mei "我后知后觉地想起来，以前我和彭江丽经常买它来吃。因为小时候钱不够，还总是把糖果锤碎一人一半。"
    mei "现在，就连看到包装的时候，我都差点没能想起来这是什么。"
    show q_candy2 at cg_s with dissolve
    mei_speaking "嗯嗯，是……"
    show q_candy3 at cg_s with dissolve
    mei "我拆开包装扔进嘴里，甜腻的味道直冲天灵盖，把我喉咙发出的声音堵得模模糊糊。{p}以前我怎么会喜欢吃这个？包装纸被捏得皱皱巴巴，我开始怀疑人生。"
    
    scene bg_meiliv with pixellate
    mei "只是我应当知道，糖果的味道从来没变过。{p}自然，改变的是其他东西。"
    stop music fadeout 0.5
    
    show xiangimg fist smile at char_right with moveinright
    xiang_speaking "哇哦，这糖好甜，谢谢你啊。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "不过，为什么我每次想找梅雨问话，你都要岔开话题？"
    mei "……咦。"
    show pengimg shirt o at char_left with moveinleft
    peng_speaking "……{p}你在说什么？只是巧合吧。"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "是这样吗？在我看来……可能你自己没感觉，但真的很明显。"
    hide pengimg
    show pengimg shirt eye_angry at char_left
    $ renpy.music.play(music.peng_explode, channel="music", loop=True, fadein=0.5)
    peng_speaking "……哦。\n既然你知道，那为什么还要继续问？你非要问这种问题吗？"
    mei "完了，感觉……{p}气氛很不妙……"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    xiang_speaking "我不是这个意思，我知道有些问题让人不想回答，我只是好奇为什么是你来拒绝。"
    hide pengimg
    show pengimg shirt eye_angry o at char_left
    peng_speaking "谁说的重要吗？你知道就是没有答案给你不就行了吗？"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "可能你觉得我很烦，但我也有良知。住在一起，我当然担心会不会无意影响梅雨。不是要问隐私，只是怕无意识做坏事。"
    peng_speaking "有什么良知？不想招惹麻烦才是真的吧。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "好，就算是那样，那至少明面上绝不会要害她，结果不是一样的吗？"
    xiang_speaking "况且再怎么说，我问的是梅雨。她又不是没有自理能力的小孩，她不想回答，或是想拒绝我的话她自己会说。"
    hide pengimg
    show pengimg shirt eye_angry at char_left
    peng_speaking "你……"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    xiang_speaking "你每次打断，会让我很困扰。你是她妈吗？连这种事也要你来说才行，你——"
    hide pengimg
    show pengimg shirt eye_angry o at char_left with vpunchm
    peng_speaking "你太过分了……！！"
    hide pengimg
    show pengimg shirt eye_angry o at char_left with vpunchs
    $ renpy.sound.play(sound.crash, channel="sound")
    na "啪！哐当！"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "——你看，我们现在讲话，梅雨也没有插嘴啊。"
    mei "巨大的桌椅碰撞声后，向夏平稳地说完被打断的话。{p}而突然拍桌站起的彭江丽，则是下意识快速扭头，对上了我的眼睛。"

    show meiimg shirt eye_shock at char_mid with dissolve
    mei_speaking "啊……"
    hide pengimg
    show pengimg shirt eye_angry at char_left with vpunchs
    mei "这四目相对十分突然，她的表情还停留在无比愤怒的状态，脸庞却飞速地涨红。{p}她的嘴唇无声地开合，眼睛颤抖地望着我，像是在恳求我做出什么回答。"
    hide pengimg
    show pengimg shirt eye_care at char_left with vpunchs
    mei "……而我却真的没能说出任何一句话。"
    stop music fadeout 0.5

    scene bg_meiliv with pixellate
    show pengimg shirt eye_still o at char_mid with dissolve
    peng_speaking "啊……这样啊，我明白了。\n抱歉，是我擅自做这样的事。"
    $ renpy.sound.play(sound.heartbeat_1, channel="sound")
    mei "不是……"
    hide pengimg
    show pengimg shirt eye_care o at char_mid
    peng_speaking "让你们感到困扰了，真是抱歉。\n你……你们，你们继续聊吧。我先走了。"
    $ renpy.sound.play(sound.heartbeat_2, channel="sound")
    mei "不是这样的……"
    hide pengimg
    show pengimg shirt eye_care smile at char_mid
    peng_speaking "今天打扰了，饭很好吃，谢谢你们。\n拜拜！"
    hide pengimg with easeoutright
    $ renpy.sound.play(sound.heartbeat_3, channel="sound")
    mei "别……"
    show meiimg shirt eye_shock at char_mid with vpunchs
    "砰！"
    hide meiimg
    show meiimg shirt eye_shock o at char_mid
    mei_speaking "……别走！"
    hide meiimg with dissolve
    mei "我的声音迟钝地从嗓子里逃出来，被重重落上的大门阻挡得干干净净。"
    show bg_meiliv with dissolve: 
        blur 15
    mei "彭江丽的笑容像在挤压我的心脏，逐渐演化成真实的疼痛。{p}我弓起身体，用力捂住心口，张开的嘴没能闭上，而是开始大口喘息。"
    mei "怎么会，变成这样……{p}好痛……好痛……"

    scene bg_meiliv with Fade(1,1,1.5)
    show xiangimg o at char_right with easeinright
    xiang_speaking "喝点水吗？"
    show meiimg shirt eye_still o at char_left with easeinleft
    mei_speaking "……\n谢谢。"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    hide meiimg
    show meiimg shirt eye_close at char_left
    mei_speaking "……"
    mei "缓慢地喝完水，我放下杯子，心情复杂地抬起头看她。但向夏只是平和地看着我，没有任何明显的情绪。{p}这反倒让我难以开口，本就凌乱的心绪更加无法平静。"
    mei "一瞬间，我很想冲她发火，但是……"
    mei "默认了彭江丽帮我岔开话题的是我，没有好好解释的是我，刚才，让彭江丽离开的人也是我……我实在，没有什么资格开口。{p}可是，可是……"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "你有什么话要说吗？没有的话，我把这些碗收了就回去了？"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "啊，嗯……"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "好，我收一下。对了，你的盒子刚刚掉地上了，我帮你放这咯。"
    hide xiangimg with easeoutright
    mei_speaking "谢谢。\n……"
    mei "我捏紧药盒，突然被无名的情绪控制，毫无预兆地朝那个站起来的背影开口。"
    hide meiimg
    show meiimg shirt eye_still o at char_left
    mei_speaking "之前是我，没有说话。你能不能，别生彭江丽的气。我之后跟她说……"
    show xiangimg fist smile at char_right
    xiang_speaking "原来你是说这个啊，我没生气啊。这事冷静下来之后，说开就好了。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……啊？你不是……"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "我不是说过了嘛，我没什么别的意思，只是想能好好说话。"
    xiang_speaking "就像现在我知道你的态度，你不想说的事情我就不会问了。然后如果我哪里让你不舒服，你告诉我就好。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "哦……嗯。"
    mei "事情没有解决，现在不应当产生这种心情，但……我真真切切松了口气。"
    mei "太好了，没有什么我没能解读出的暗示，她说话一如既往简单直接，真的，太好了……"
    
    scene bg_meiliv with pixellate
    na "嘟，嘟……"
    mei "听筒里第三次传来未接电话的忙音，我下意识地再次重复拨号的动作，又在最后一个按键按下时匆匆止住。"
    mei "这样也没什么意义……彭江丽不想接电话，我再继续也只是骚扰而已。"
    scene bg_meiroom with pixellate
    mei "我有些困乏地拖着脚步上楼，放任自己的身体扑通一声倒在床上，用厚厚的被子把自己埋住。{p}仿佛这样就能隔绝一切不顺心的事。"
    mei "以前，小时候……我和彭江丽从来没有吵过架。现在想来，说不定，那时候也只是她在让着我。{p}她是不是已经不满意我很久了？她……"
    mei "明天，直接去找她吧。就算她要骂我……我还是想……"
    scene bg_black with dissolve
    mei "我似乎在呢喃什么，但意识已经陷入了模糊。"

    scene bg_meiroom with fade
    na "呼——呼——呼——"
    na "哒，哒哒，哒哒……"
    scene bg_rainy_window with dissolve
    mei "事情没能像昨天预想的那般发展。{p}我坐在窗边，指关节来回敲打着窗台。不规律的敲击声响暴露了我内心的焦虑，但我即使意识到也无法控制。"
    mei "被水流来回冲洗过的窗玻璃又蒙上了一层水雾，却仍然能看到窗外凌乱飞舞的枝叶和密密麻麻落下的水滴。"
    mei "暴风雨来了。"
    return