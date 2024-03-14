label chap1_3:
    scene bg_meikitc with fade
    mei_speaking "……"
    mei "虽然据叶成华所说，她最近换了工作，但她还是很忙。况且立涧村东西侧距离不近，路况也很差，每天来回确实不方便。"
    mei "但……"

    scene glitches with fade
    ye_speaking "既然你现在也不是一个人住，干脆之后和向夏一起做饭吧，哦，对了，我是不是才跟你说她的名字来着？"
    mei_speaking "……是啊。"
    mei "她才发现吗……"
    ye_speaking "哎呀，这个，我之前忙忘了，现在跟你说了嘛。\n噢，不跟向夏一起也行，你要是愿意自己做饭，我也不用一天过来好几次了。"
    mei_speaking "……啊。"
    ye_speaking "这么想，学学做饭对你自己也有好处啊，以后一个人也不怕饿死了。"
    mei_speaking "……"
    mei "我就知道。\n她根本就知道我不会做饭，所以除了和向夏一起以外别无选择。"
    mei "不过，就算她没说，我也没打算让她每天过来给我做饭。已经住在这里了，怎么能给她添更多麻烦。"
    mei "反正向夏也不是熟人，不耗费精力在她身上，随便相处一下也无所谓。"

    scene bg_meikitc with fade
    mei "但说是一码事，真正面对的时候又是另一码事……{p}不过，说到底，本来就是叶成华要让我回到这里住的吧。"
    mei "我不应该这么想，但这种想法的确忍不住就会冒出来。"
    show meiimg shirt eye_close o at char_left with dissolve
    mei_speaking "唉……"
    show xiangimg o at char_right with dissolve
    xiang_speaking "怎么了，你对刚刚说的有什么意见吗？"
    hide meiimg 
    show meiimg shirt at char_left
    mei_speaking "哦，没事。"
    mei "只是突然想起造成我现在这个境地的罪魁祸首，实在忍不住想叹息而已……"
    hide meiimg with dissolve
    hide xiangimg with dissolve
    mei "因为我没尝试过，这又是我们第一次一起做饭，所以我们一致认为简单就好。\n尽管冰箱里食材不少，我们只打算把面条和青菜煮在一起。"
    mei "向夏烧水煮面，而我在旁边的桌子上笨拙地拿刀，把青菜切成一段一段的小块。{p}嗯，至少这种事我做起来还是没什么问题——"
    
    show q_x30 at cg_s, shaking

    xiang_speaking "——哇啊！！"
    mei_speaking "哈啊？？！！"
    na "呼——！啪——！咚——！"
    mei_speaking "喂！"
    xiang_speaking "啊！"

    window auto
    scene bg_meiliv with Fade(1.5,1,1)
    mei_speaking "……"
    xiang_speaking "……"
    peng_speaking "……"
    mei "我站在餐桌旁，和旁边的另外两个人面面相觑，一种比以往更加诡异而尴尬的气氛笼罩在房间里。{p}到底为什么会变成这样……完全难以招架啊……"
    show pengimg shirt o at char_mid with moveinleft
    peng_speaking "你，啊……你们还是先吃点东西吧。"
    show meiimg shirt eye_wacky at char_left with moveinleft
    mei_speaking "嗯……"
    show xiangimg eye_squint laugh at char_right with moveinright
    xiang_speaking "可以吗？啊，那好吧，真是太谢谢你了，那我先不客气啦。"
    mei_speaking "……"
    hide meiimg
    show meiimg shirt at char_left
    mei "在我还有些不自在的时候，向夏已经完全调整好了状态。在和彭江丽再次确认后，她毫不客气地坐下来，大口吃起炒面。\n她倒是自然……"
    mei "至于为什么是炒面……我下意识按了按手指，伤口的疼痛让我叹了口气。"

    scene bg_meikitc with fade
    show halfblack
    mei "口口声声说做过饭的向夏，一声尖叫后成功让我手滑切到自己的手，以及看到灶台上冒出的大火。"
    mei "一片混乱中，我冲到客厅打电话，等到打通才发现我下意识拨的是彭江丽的号码。"
    mei "她很快帮我们处理了麻烦，还顺便做了一餐饭。\n于是……"

    scene bg_meiliv with pixellate
    show pengimg o at char_right with moveinright
    peng_speaking "……那，我先回去啦？你趁热吃哦。"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "嗯……啊？"
    mei "彭江丽犹豫的声音打断了我的思考，抬头一看，向夏正专心吃饭，而彭江丽也已经穿好外套，只有我还呆呆地站在原地。"
    return