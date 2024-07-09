label chap8_x4:
    scene bg_meiliv with fade
    show yeimg o at char_right with moveinright
    ye_speaking "什么？你说你联系不上向夏了？"
    show meiimg shirt eye_close at char_left with dissolve
    mei_speaking "对……她今天早上说想去后山那边，但是中午到现在都没回来。"
    $ renpy.music.play(music.xiang_handing_out, channel="music", loop=True, fadein=0.5)
    mei "我不擅长说谎，即使演练过，也还是难免有些不自然。好在我说话本身就比较慢，还容易卡壳。"
    mei "希望叶成华别发现吧……"
    hide meiimg
    show meiimg shirt o at char_left 
    mei_speaking "所以我想着去找一下，就是，我一个人的话可能不够……"
    ye_speaking "嗯……的确麻烦啊。虽然我觉得她应该不会出什么问题，但这种事就怕有个万一啥的。"
    hide yeimg
    show yeimg smile at char_right 
    ye_speaking "反正也不远，我跟你一起过去看看吧。"
    mei_speaking "嗯，好。"

    scene bg_meihome with pixellate
    mei_speaking "我去找靠着山脚的那边吧，我小时候去过里面，比较熟悉。"
    ye_speaking "行，有什么事情就给我打电话，别着急。"
    mei "最后一步了……我悄悄地呼出一口气，按捺住自己的脚步，不让它变得过于慌乱。"
    mei "叶成华从花海的左侧往里走，我确认她的视线远离后，往花海的另一边走去。"

    scene bg_flower1 with fade
    mei "走近之后，可以看出花群只是从外面看起来很拥挤，但它其实是分块种植的，不然也没法维护管理了。"
    mei "我站在花茎间留出的小路中，被巨大的花瓣和叶片震惊得说不出话。真正站到面前，我才意识到它貌似比我还高。"
    mei "真是神奇，只是花朵竟然也可以长这么高……嗯？"
    show q_x40 at cg_s with dissolve
    mei "右臂突然被一道力度拉住，我转过头，发现是向夏。她一边维持一个艰难的半蹲姿势，一边伸手拉着我。"
    mei_speaking "……你在干嘛？"
    xiang_speaking "这不是怕被发现吗，毕竟我个头这么高。"
    mei_speaking "发现什么？而且你不就比我高了一点？"
    xiang_speaking "高一点也是高，这花遮不住我不就被你姐她们看到了吗。"
    mei_speaking "她们要是见面了，肯定知道我们在说谎啊，看到就看到呗。"
    xiang_speaking "那我还怎么偷看？"
    mei_speaking "……哈？"
    xiang_speaking "不然我过来干什么，只是你说要找我，我完全可以不在这出现啊。\n你就不好奇她们要在这干嘛吗？"
    mei_speaking "……\n这，这样好吗？"
    mei "实话说我也很好奇，但还是用意志力制止了这份心动。"
    xiang_speaking "这怎么了，这里可是公共场合呀，我们就是碰巧路过怎么了？来都来了嘛。"
    mei_speaking "……"
    stop music fadeout 0.5
    hide q_x40 with dissolve
    $ renpy.sound.play(sound.light_wind, channel="nature", loop=True, fadein=0.5)
    mei "我和她之间绝对有一个人对“碰巧”的理解有问题。"
    mei "只是，虽然这么说，但我也没有再往外走。因为……"
    mei "起风了。"
    mei "绿叶和花瓣互相贴近，它们向着同一个方向摇摆，发出簌簌的声响。"
    xiang_speaking "咦……"
    xiang_speaking "这个风吹的方向，好像就是你姐姐她们在的地方哦。这么神奇？"
    mei_speaking "诶？"
    xiang_speaking "走啊走啊，过去看看！"
    mei "我没再拒绝，也放轻脚步跟在向夏的身后，朝左手边的方向走去。"

    scene bg_flower2 with Fade(0.2,0.4,0.3)
    mei "用手轻轻拨开花茎，层叠的花瓣和叶子悄悄让开一条缝隙，在那之间，能够看到远处花朵间的人影。"
    mei "路花正在跳舞。身形优美，步伐轻盈，衣角随着动作飘起又落下，绘制成美丽的剪影。两侧的花朵和枝叶也伴着人影一起飘摇，仿佛天然的伴舞。"
    mei "甚至，随着又一阵微风，空中悠悠卷起本不应该存在的，掉落下的橘黄花瓣。"
    mei "花瓣漂浮，在身影的周围飞舞，迟迟没有下落。"
    mei_speaking "……"
    xiang_speaking "……"
    mei "……被这样的场景震撼，我完全失语了，向夏也完全没有出声。"
    mei "奇迹……我蓦地想起暴风雨时的突兀水流。\n现在这样……是不是，也算一种奇迹呢。"

    scene bg_flower2 with fade
    xiang_speaking "话说……我们，是不是不该过来看……？"
    mei_speaking "……嗯，但是，你现在才说，好像也晚了吧？"
    xiang_speaking "哎呀，这不是意外吗，我们现在走还来得……啊。"
    mei_speaking "……啊。"
    mei "向夏说到一半的话突然顿住，我顺着她的视线看去，也停住动作。"
    show movie_side with moveinleft
    mei "在我们讲话时，舞蹈已经迎来尾声。因而，场景里增加了观众的身影。"
    mei "明艳的花丛中，两个身影逐渐靠近，而后贴在了一起。"
    mei_speaking "……"
    stop nature
    $ renpy.sound.play(sound.heartbeat_2, channel="sound", loop=True, relative_volume=1.2)
    mei "我知道，我应该移开视线，可身体却十分僵硬，不知道该如何行动。"
    mei "身侧……身侧，不属于自己的气息在这时变得格外明显，仿佛提醒我，应该赶快打断这奇怪的气氛。"
    mei "我和向夏躲在这里看情侣接吻，而我们之间的距离也如此接近……不知为何，我突然不敢转头看她。"
    mei "心跳突然变得有些不均匀，是因为偷窥带来的紧张，还是因为……"
    scene bg_black with dissolve
    mei "我突然不敢继续想。"
    mei "不，不对，我肯定想多了，向夏肯定不会在意这些的，她冷静的话我也能冷静下——"
    stop nature fadeout 0.5

    show cg_x101 at cg_0 with dissolve
    mei "我猛地转过头，却彻底愣住。"
    mei_speaking "……\n你……"
    $ renpy.music.play(music.xiang_heartbeat, channel="music", loop=False, fadein=1.0, relative_volume=0.8)
    mei "向夏正目不转睛地看着我，似乎在我转过头之前，就已经注视了许久。"
    mei "她从未有过地睁大了双眼，黑曜石一般的眸子清澈透亮，似乎因为某种情绪而微微颤动。"
    mei "阳光不止照耀她的眼眸，也在她那随风摇曳的发丝上落下斑驳光影，更诚实地映照出她通红的脸颊。"
    show cg_x102 at cg_0 with dissolve
    hide cg_x101
    xiang_speaking "呃……"
    mei "毫无防备的四目相对。我的手指骤然绷紧，不受控地死死揉捏住外套的边角。"
    mei "你……你在脸红什么啊！你怎么会脸红啊，明明你之前看到那些黄色小电影都毫无反应的不是吗……？！"
    mei "你要是这样……"
    mei "我岂不是，更加没有办法控制住自己的心跳了吗？"
    stop music fadeout 0.5
    stop sound fadeout 0.5
    return
