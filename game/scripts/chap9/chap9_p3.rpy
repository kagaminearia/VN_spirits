label chap9_p3:
    scene bg_vil3 with vpunchm
    mei_speaking "别走！"
    mei "我想都没想，直接朝她的方向冲了过去。\n彭江丽似乎愣住了一瞬间，但很快又重新迈开腿。"
    mei_speaking "喂！！"
    scene bg_vil3 with dissolve:
        function WaveShader(period = 2, amp=1.0, repeat='mirrored', double="both")
    mei_speaking "喂……啊……哈啊……"
    mei "我没跑两步，就已经觉得胸口有种被拉扯的疼痛感，只好停下脚步，看着彭江丽不断远离的背影。"
    scene bg_vil3 with vpunchm
    mei_speaking "别跑了！！"
    mei "意料之内，没有回应。"
    mei "我皱了皱眉，虽然不能跑步，但我还是尽量加快了脚下的速度，跟着她离开的方向走。"
    mei "不过，这个方向……总感觉，有点熟悉……"

    scene bg_hill1 with fade
    mei_speaking "啊——累死了……你可把我害惨了……"
    $ renpy.sound.play(sound.heartbeat_2, channel="sound", loop=True, fadein=0.5)
    mei "我大喘一口气，无奈地嘟囔着，看向草丛里明显不久前才被人踩过的痕迹。"
    mei "这个地方通往北边的后山，因为土壤不适合种果树，现在也没有合适的植物成熟，平时很少会有人来这里。"
    mei "但，如果是她的话，应该就是这里了……"
    mei "太阳已经接近地平线，高耸的山林分不到太多光照，显得有些阴沉。\n这个时间点进山可不是好选择……要是我猜错，她不在这里就好笑了。"
    mei "可如果我没猜错，她真的进去了……"
    mei_speaking "唉……"
    mei "毕竟，这说来其实是我的问题……要是我委婉点，没那么说就好了……"
    mei "不，要是我当时拦住她就好了……"
    mei "不过，现在想这些也没有用。我长叹一声，只好也顺着脚步痕迹往里走。"
    scene bg_hill2 with fade
    $ renpy.sound.play(sound.peng_wind, channel="sound", loop=True, fadein=0.5)
    na "啪嚓……簌簌，唰唰……"
    mei "摩擦和碰撞的声响从身边不断发出，偶尔因为我的动作停止，而后又随着步伐响起。"
    mei "就这样，我慢慢进了树林。"

    scene bg_hill4 with dissolve
    mei "视线里都是高大的树木，几乎遮天蔽日。因而，本就稀薄的光线愈发被阻拦在外，四周显得更加阴沉。"
    mei "鞋底踩过土地和植物的根茎，发出挤压的声音，在安静的林间格外突兀。"
    scene bg_hill2 with dissolve
    mei_speaking "呃，有人吗……？彭江丽？喂——"
    mei "在这样的环境里，我实在不敢发出太大声音，只是轻轻朝着远处呼唤。"
    mei "但即使如此，我也能够听到一些模糊的，分不清是回音还是错觉的遥远声响。"
    mei_speaking "好像还有点痕迹，走这边吧……"
    mei "我自说自话地给自己打气，顺着散开的枝叶走。"
    mei "往左，往右……"

    scene bg_hill3 with fade
    mei_speaking "……嗯？"
    mei "脚下的痕迹变得混乱，没有规律。"
    mei_speaking "怎么办……\n啊。\n……咦？"
    mei "我无意识地一直在往前走，现在停下来才发现自己已经找不到路了。"
    mei "天色阴沉，四周的景象更加相似，只是茂密的枝叶相互叠加，分不清前后左右。"
    $ renpy.sound.play(sound.owl, channel="nature", loop=True, fadein=0.5)
    mei_speaking "……彭江丽……？\n有人吗？"
    mei_speaking "有……？唉。"
    mei "唉……理所当然的，我听不到第二个人类的声音。"
    mei "那，还是算了……我无奈地摇摇头，不打算继续做无用功。"
    mei "虽然这样很不好，但也没办法……我掏出手机给叶成华打了个电话。"
    stop nature

    ye_speaking "……你说什么？！你没在开玩笑？\n梅雨，你……"
    mei "叶成华的分贝大到有些刺耳，我把手机拿开一点，过了一会才听到她长长地叹了口气。"
    ye_speaking "梅雨，梅雨，你啊……真没想到你能做出这种事。"
    mei_speaking "这是个意外……"
    ye_speaking "哎，等着吧，我回去还得一段时间呢。"
    mei_speaking "好。"

    scene bg_hill5 with Fade(0.3,0.3,0.3)
    mei "挂断电话后，我找了块石头坐下，疲惫地闭上眼睛，捏了捏眉心。"
    mei "天色彻底暗下，肉眼只可见微微的光。"
    mei "这一下可真的是把我累惨了……我这半个病号，追着人满村跑……噗。"
    mei "虽然时机不对，但我着实是被自己的抱怨逗乐了。"
    show bg_black with dissolve
    mei "但……一想到这件事的源头，我又有些笑不出来，只好更加用力地揉着眉心，仿佛这样就可以把麻烦的事情揉出脑海。"
    show light behind bg_black
    show halfblack behind bg_black
    hide bg_black with dissolve
    mei_speaking "……嗯？"
    stop sound fadeout 0.5
    $ renpy.music.play(music.young_dream, channel="music", loop=True, fadein=0.5)
    mei "我眯着眼睛，忽然觉得哪里有些不对。余光处似有点点微光在闪烁，但天色早就暗下，我的手机屏幕也已经熄灭，哪来的光源？"
    hide halfblack with dissolve
    mei "我放下手，彻底睁开双眼。然后……我发现那并不是错觉。"
    hide light with dissolve
    show light at cg_0 with dissolve
    mei "点点淡黄色的荧光漂浮在静谧的树丛中，隐约构成一条正在飞舞的弧线。在遮蔽所有外来光线的树木间，唯有它们上下摇曳，如此耀眼。"
    mei_speaking "什么……"
    mei "我不知道它们是什么时候出现的，但……这是……在指引我吗？"
    mei_speaking "这是……"
    mei "来不及思考，身体已经快过大脑提前行动。"
    mei "我站起身，没有犹豫地朝着散发点点光亮的地方走去。"
    mei "我……我想起来了。\n这样的场景，这样熟悉又相似的场景。我见过。"
    scene bg_white with dissolve
    mei "在许久以前，在我小的时候，我见过……"
    scene glitches with dissolve
    young_mei "呜，呜……有没有，人……谁，来……"
    show mem1 with dissolve
    young_mei "我，迷路……好像……"
    hide mem1 
    show mem2 at cg_1, shaking
    young_mei "……呜，灯……？"
    young_mei "…谁……？"
    mei "那时，那时候也是这样……\n数个发光的小点漂浮着，带我走向一条清晰的道路。"
    scene glitches with dissolve
    mei "然后，在道路的尽头，我看到了她……"
    show mem3 with dissolve:
        alpha 0.5
    young_peng "阿雨！"

    scene bg_black with vpunchm
    peng_speaking "梅雨！"
    show cg_p131 at cg_0 with dissolve
    mei_speaking "……咦？"
    show flash with dissolve
    hide cg_p131
    mei_speaking "不是，回忆……？不只是，回忆吗？"
    mei "我倏地回过神，只觉得自己好似身在梦境之中，不知道今夕何夕。"
    scene bg_black with dissolve
    mei "一瞬间，已经跨越多年的，沉淀的记忆重新浮起，和眼前的场景重叠。"
    show cg_p131 at cg_0 with dissolve
    mei "同样的记忆，同样的情形，同样是……那个人，出现在我面前。"
    stop music fadeout 0.5
    show cg_p133 at cg_0 with dissolve
    hide cg_p131
    peng_speaking "梅雨真的是你！太好了你没事……太好了，我要吓死了……"
    show cg_p132 at cg_0 with dissolve
    hide cg_p133
    peng_speaking "我没想到你会跟过来，对不起，你没事，没事就好……都怪我，我不——啊？"
    hide cg_p132 with dissolve
    mei "什么都不想去想了。"
    mei "我张开双臂，抱住了她。此时此刻，我只想这么做。"
    $ renpy.music.play(music.peng_love_you, channel="music", loop=True, fadein=0.5)
    mei_speaking "谢谢。"
    mei_speaking "谢谢你……丽丽。"
    mei "谢谢你，再一次出现在我的面前。{p}谢谢你，担心着我。{p}谢谢你……一直以来，如此重视我。"
    show cg_p141 at cg_0 with dissolve
    mei "好一会儿，我感受到我的身体被更用力地抱紧——在我抱住她的时候，她就已经稳稳地环住我的腰——而后，轻柔的气息从耳侧传来。"
    peng_speaking "真好……我又找到你了……阿雨。"
    mei "她的声音极其柔软，落在我的身上，仿佛要将我融化了。"
    mei "我的四肢都将融化到失去直觉，只剩下心脏在剧烈地跳动。"
    mei_speaking "我……"
    peng_speaking "……阿雨……"
    hide cg_p141 with dissolve
    peng_speaking "我喜欢你。"
    stop music fadeout 0.5
    return