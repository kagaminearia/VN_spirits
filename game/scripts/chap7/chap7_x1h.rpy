label chap7_x1h:
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "……啊？我不要。"
    mei "我没怎么想就拒绝了。"
    mei_speaking "我是不想要求你什么，所以，现在这事也一样啊。"
    hide xiangimg
    show xiangimg fist eye_still o at char_right 
    xiang_speaking "但是，你不想知道发生什么了吗？这么简单的道歉完全不够。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "我想知道，但你如果真的不想讲，我当然不会强迫。"
    hide xiangimg
    show xiangimg fist eye_close o at char_right 
    xiang_speaking "但是这是不对的。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "啊？"
    hide xiangimg
    show xiangimg fist at char_right 
    xiang_speaking "我伤害到你，我总得解释清楚，还得赔偿啊。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "我不是说没事了吗。"
    hide xiangimg
    show xiangimg fist eye_close at char_right 
    xiang_speaking "这样我岂不是亏欠你了。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "唔，想起来了，等等我拿个东西给你！"
    stop music fadeout 0.5
    hide xiangimg with moveoutright
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "啊？"
    mei "她突然拍了下桌子，吓我一跳。而后，她飞快地进屋，又飞快地拿着什么东西出来。"
    hide meiimg
    show meiimg shirt at char_left
    mei "总感觉，有些眼熟……"
    show xiangimg fist laugh at char_right with moveinright
    $ renpy.music.play(music.xiang_handing_out, channel="music", loop=True, fadein=0.5)
    xiang_speaking "这个，这回你能收下了吧，当作我的补偿！"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "……你之前要给我的生日礼物？"
    mei "被她这么说，我想起来了这个包装，那天她短暂地拿出来过。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "嗯，是啊。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "好吧，是什……么——"
    hide meiimg
    show meiimg shirt eye_wacky at char_left
    mei "这是一个崭新的，薄薄的信封，我拆开封口处，就看到熟悉的纸张图案。"
    hide xiangimg
    show xiangimg fist laugh at char_right
    xiang_speaking "怎么样？"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left
    mei_speaking "……你送礼物，是指送钱给别人？"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "嗯，不行吗？"
    mei "她一脸理所当然，以至于我又卡了壳。\n哪有人这样送礼物的？？"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei_speaking "这，我不能收啊。"
    hide xiangimg
    show xiangimg fist eye_squint o at char_right
    xiang_speaking "为什么？你都拆开了！"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "……除了钱，你就想不到别的东西吗？"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "唔，我还请人吃饭。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei "的确，彭江丽上次的事情就是这样……\n手里的东西变得有些烫人，我无奈地看着它，又看看向夏执着的表情，还是收了起来。"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei "按照她的说法，下次再请她吃饭好了……\n还以为是什么礼物呢……我无奈地叹了口气。"
    stop music fadeout 0.5

    scene bg_meiliv with pixellate
    mei "我剩下的饭没多少，向夏又速度很快，即使被中间的插曲打断，也没用多少时间就就吃完了。"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "还要吃点别的吗？"
    show xiangimg o at char_right with dissolve
    xiang_speaking "呃，还有吗？"
    mei_speaking "嗯……现场做？"
    hide meiimg
    show xiangimg fist eye_close o at char_right
    xiang_speaking "好麻烦，算了，反正我也不用吃很多东西。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "好吧……"
    hide meiimg
    show xiangimg fist o at char_right
    xiang_speaking "我还是，解释一下之前的事情吧，不然总觉得不太好。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "什么？好啊，你要是想说的话，我当然愿意听。"
    mei "我倒是没想到她还想着说这事，但我现在的确很好奇，比一开始还要好奇……"
    hide meiimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "没问题，嗯……"
    hide meiimg
    show xiangimg fist eye_still smile at char_right
    xiang_speaking "不过，就坐在这里说，就算是我也会觉得害羞啊。"
    mei "向夏摸了摸脸，笑容有些犹疑。客厅很亮堂，顶灯的光线明晃晃地照在我们身上，拉出板正的影子。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei "平常的话，她像这样打趣我肯定会附和几句，但现在却只觉得开不了口。\n她那样坚定的语气，令我感到无地自容。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "好吧……你要去哪？"

    scene bg_balcony with pixellate
    show halfblack
    show xiangimg laugh behind halfblack at char_right with moveinright
    $ renpy.music.play(music.starlight, channel="music", loop=True, fadein=1.0)
    xiang_speaking "就这里吧！上去！"
    show meiimg eye_wacky flower behind halfblack at char_left with moveinleft
    mei_speaking "你说……这里？"
    hide xiangimg
    show xiangimg o behind halfblack at char_right
    xiang_speaking "你家阳台啊。"
    hide meiimg
    show meiimg eye_close o flower behind halfblack at char_left 
    mei_speaking "……我当然知道。"
    hide meiimg
    show meiimg o flower behind halfblack at char_left 
    mei_speaking "但你说上去……什么意思。"
    hide xiangimg
    show xiangimg smile behind halfblack at char_right
    xiang_speaking "用这个梯子爬到天台嘛。"
    hide meiimg
    show meiimg flower behind halfblack at char_left 
    mei_speaking "……"
    mei "真亏她能想出来啊……"
    hide meiimg
    hide xiangimg
    mei "二楼走廊的一侧连着落地玻璃门，外面就是阳台。上个月，我还在这里看过暴风雨。\n至于现在……"
    mei "阳台有上到这栋楼最顶端天台的楼梯，向夏指的就是那里。"
    mei "的确，无人的天台很符合一般故事里说秘密的场合，但是……"
    show meiimg flower behind halfblack at char_left with dissolve
    mei_speaking "我上不去啊。"
    mei "嵌进墙壁的梯子底部距离地面有一定距离，我的脚够不到，而我的力气没法让我只靠手臂就把自己拉上去。"
    show xiangimg fist eye_squint smile behind halfblack at char_right with dissolve
    xiang_speaking "原来你说这个呀。这个简单啊，我有办法，这样——"
    hide meiimg
    show meiimg eye_shock flower behind halfblack at char_left
    mei_speaking "什……么？！"
    hide xiangimg
    show xiangimg fist eye_squint laugh behind halfblack at char_right
    show meiimg eye_shock flower behind halfblack at char_c with vpunchs
    xiang_speaking "就行了！"
    mei "这人做什么啊……！！！"
    mei "她一下子把毫无防备的我举了起来，现在，我的脚几乎和梯子的最底部平齐，稍微抬腿就能够到那根铁杆了。"
    xiang_speaking "怎么样？能行吗？"
    hide meiimg
    hide xiangimg
    mei "她托着我，声音仍旧充满中气，甚至隐隐有顺着手臂传到我身上的感觉……不对，我在想什么。"
    mei "到这个高度，要爬上去就轻松很多，她都这样了，我也没法下去……"
    mei "唉……我轻轻叹气，无奈地伸出手，抓住栏杆。"


    scene bg_roof with fade
    show halfdarkblue
    mei_speaking "……呼啊。"
    mei "好在梯子不高，几乎不费什么力气。\n我上去之后，向夏也很快爬了上来。"
    mei "群星散布在头顶高高的天穹，像天鹅绒绸缎上点缀的钻石，在浓郁的夜色中发出微弱的光芒。"
    mei "四周很安静，也许所有生物都睡着了，只有我和旁边的人的呼吸声。"
    mei "这……\n这让我蓦地想起……那个充斥着狂风暴雨的夜晚。"
    mei "同样是夜晚……那时候，我注意到完全不同的向夏。而现在……也会是吗？"
    mei "我偏头看向她，不知是因为夜晚太黑，或是因为我被回忆影响，还是……她真的没有任何表情。"
    
    show xiangimg fist eye_still o behind halfdarkblue at char_right with moveinright
    xiang_speaking "我现在，倒是有点理解你那个朋友，嗯，叫彭江丽？我倒是有点理解她的想法了。"
    show meiimg o flower behind halfdarkblue at char_left with moveinleft
    mei_speaking "啊？什么意思……"
    hide xiangimg
    show xiangimg fist eye_still smile behind halfdarkblue at char_right
    xiang_speaking "有些事情，可能就是很不想说吧。连自己多说一句拒绝的话都不愿意，所以才想让别人帮忙。"
    hide meiimg
    show meiimg flower behind halfdarkblue at char_left 
    mei_speaking "……"
    hide meiimg
    show meiimg eye_close o flower behind halfdarkblue at char_left 
    mei_speaking "那你就别说啊。"
    hide meiimg
    show meiimg eye_close flower behind halfdarkblue at char_left 
    mei "不知为何，我有些莫名地烦闷，语气也变得生硬。\n是外套太热了吗？可是这个时间点的温度应该很低才对……"
    mei "真是的，既然想逃避，那为什么非要逼自己去做……"
    mei "……这样的话，岂不是，显得我十分软弱吗……"
    hide xiangimg
    show xiangimg fist eye_still laugh behind halfdarkblue at char_right
    xiang_speaking "嗯，也对。"
    hide xiangimg
    show xiangimg fist eye_close laugh behind halfdarkblue at char_right
    xiang_speaking "{size=30}你会那么想也是理所应当的，但是我……我必须自己面对一切才行。{/size}"
    hide meiimg
    show meiimg o flower behind halfdarkblue at char_left 
    mei_speaking "等等，你刚说什么了吗？"
    hide xiangimg
    show xiangimg fist o behind halfdarkblue at char_right
    xiang_speaking "啊，没有。"
    hide xiangimg
    show xiangimg fist laugh behind halfdarkblue at char_right
    xiang_speaking "我是说，来都来了啊，不说的话不就白爬上来啦？"
    hide xiangimg
    show xiangimg fist laugh behind halfdarkblue at char_right
    xiang_speaking "是吧？嘿嘿。"
    hide meiimg
    show meiimg flower behind halfdarkblue at char_left 
    mei_speaking "……哼。"
    mei_speaking "{size=30}就算，只是在这里看星星……也还行啊。{/size}"

    hide meiimg with dissolve
    hide xiangimg with dissolve
    xiang_speaking "好啦，我会说的，不过我不知道该怎么讲，要不直接从头开始吧？但我说不定会讲很久哦。"
    mei_speaking "无所谓啊，我不介意。"
    mei "我还没听过别人讲故事，说实话，挺新奇的……"
    stop music fadeout 0.5
    xiang_speaking "嗯，让我想想……"

    return
