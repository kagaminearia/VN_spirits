label chap5_x1:
    scene bg_meiliv with fade
    na "咔哒。"
    show xiangimg o at char_right with moveinright
    xiang_speaking "原来是你啊，你今天终于出来吃饭了？"
    mei "我到楼下的时候，角落的门被打开，向夏也刚好走出来，笑着朝我挥了挥手。"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "嗯。"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "对了，看起来你好像没事，你要跟我一起出去吗？"
    mei_speaking "啊？"
    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "我要去别人家帮个忙，清理房间和家具啥的。"
    mei_speaking "……你去帮忙？"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "啊，有报酬的，顺便帮帮嘛，大家都是邻居。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei "难道我才是那个外来的人？"
    mei "说真的，我还真是很佩服她这既来之则安之的心态……"
    xiang_speaking "所以你去不去？我马上就要走了。"
    mei_speaking "……\n不。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "好吧，我看你之前不是还——"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "我去也没用。"
    mei "我意识到向夏似乎要提到之前的事情，脑中的弦瞬间绷紧，连想都没想，就粗暴地打断了她的话。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "——还，嗯，所以你的意思是，你其实是想去的？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "不。我又做不了事。"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "这样啊，嗯，我说……{p}你是不是没上过班？"
    hide meiimg
    show meiimg shirt eye_wacky at char_left
    mei_speaking "哈？"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "你想做事还不简单啊，就算没事也能给你找出事情来。\n反正你现在也没别的安排吧，真的不去吗？"
    mei_speaking "……\n好吧。"
    mei "她倒是说对了一点，我的确没事可做。\n确实，无所谓了……我也不知道该做什么……"

    scene bg_misc1 with pixellate
    mei "家具被近日的阳光晒得很干，看起来已经恢复原状，但只要靠近，就能闻到表面散发出的难闻气味。"
    mei "水分和污染物并不会因为日晒通风就被除尽，我拿着抹布，小心地沾上清洁剂，在家具的表面来回擦拭。"
    mei "去除可能残留的细菌和脏污之后，可以把去味剂放在有空间的家具内部，不过，之后向夏会把家具再拿去晾晒，这时候就没必要太过浪费资源。"
    show xiangimg o at char_right with moveinright
    xiang_speaking "这边弄完了吗？"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "啊，没，我尽量快……"
    hide xiangimg
    show xiangimg smile at char_right with moveinright
    xiang_speaking "哦我就问问，先搬那边也一样的，之前搞了一些了。\n又没催你，别急啊，这事不得细致点嘛。"
    show meiimg shirt at char_left 
    mei_speaking "哦……"
    mei "她这么说，倒是让我稍微放松一些。"
    mei "我擦洗家具的每个缝隙和死角，清理之后，让向夏把东西搬到后院。{p}之后，再处理之前晒好的一部分，使用防霉剂防止可能的霉菌。"

    scene bg_misc1 with pixellate
    grandma_speaking "行了行了，别再忙了。今天真是多亏你们啊，做得可真干净，真是谢谢了。"
    grandma_speaking "我这也没什么好东西，你俩一人一个荷包，收着吧。"
    show meiimg o at char_left with dissolve
    mei_speaking "啊？不……"
    show xiangimg fist eye_squint laugh at char_right with dissolve
    xiang_speaking "好哎，那就谢谢您啦，之后需要帮忙再来找我就行。"
    mei "没等我再说话，向夏很快和老人完成了交涉，然后推着我往外走。{p}绣有刺绣的布包鼓鼓囊囊，我打开一看，发现里面竟然塞了几张小额钞票。"
    mei "这差点让我惊得跳起来，我原本以为她说的报酬只是邻里间互送的小玩意，没想到是货真价实的报酬。"
    show cg_x51 at cg_0 with dissolve
    mei_speaking "喂，这个，得还回去……"
    xiang_speaking "为啥？我就是为了这个才来帮忙的啊。"
    mei_speaking "哈？你连人家这——"
    xiang_speaking "等等等等，都说了你别急啊。这边的广场那里有个公告栏，日常会发些超市打折啊送东西啊还有找人帮忙的告示，这个都是人家说好的，我就是赚一点点小外快。"
    mei_speaking "……这样啊。"
    hide cg_x51
    show cg_x52 at cg_0 with dissolve
    xiang_speaking "嘿嘿，我是不是比你更像这里的人？"
    mei_speaking "……哦。"
    mei "在得意什么……我无奈地干笑两声，只觉得额头上的汗比之前更多了。"
    show bg_vil4 with dissolve:
        blur 25 
    mei "黏糊的感觉让我不太舒服，但还挺新鲜——平时我很少出门，也不做任何额外的活动，这里面自然也包括会让人出汗的事。"
    mei "直到风吹过，比以往更加凉爽。{p}我愣愣地伸出手，想要抓住风中飘摇的发丝，那深黑色和橙棕色交缠的几缕。"

    scene bg_vill6 with fade
    show meiimg shirt at char_left with dissolve
    mei_speaking "……啊。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "这给你吧，我也没帮上什么忙。。"
    mei "回过神来，我意识到自己在做什么，连忙飞快地收回手，而后把另一只手攥着的布包递给向夏。"
    mei "之前是不知道，现在我反倒是像跟她抢报酬的了，这不是我的本意。{p}当然，也有要掩饰刚刚的动作的意思……"
    mei "不过，向夏却没有接，反而一脸惊讶地看着我。"
    show xiangimg fist o at char_right with dissolve
    xiang_speaking "说啥呢，你做了很多事啊，别把自己的努力说得这么不值钱。她谢谢的是我们，不是我一个。"
    mei_speaking "啊……"
    xiang_speaking "所以说，你就拿着吧，人老人家给你的啊。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "嗯。"
    hide meiimg with dissolve
    hide xiangimg with dissolve
    mei "我默默收回手，说不清现在是什么心情。{p}但，回去的路上，脚步似乎变得轻快起来。"

    scene bg_meikitc
    mei "几天没进厨房，本来也不熟练的事情更加生疏了。{p}前几天我都把自己关在房间里，现在决定出门后自然也要恢复做饭。"
    show xiangimg fist o at char_right with moveinright
    xiang_speaking "哦，不错啊，我还以为在我走之前都是我做饭了呢。"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "……嗯，抱歉。"
    xiang_speaking "啊？你不用道歉啊，我只是说说。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "反正这是你家嘛，你想怎么做都行，我哪能逼你。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    na "哗啦。"
    mei "洗到一半的菜离开我的手，一下子全部散开，落到盆里，溅出不少水花。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "为什么，要这么说？"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "嗯？什么意思？"
    mei "对啊，我什么意思……\n但……看着她疑惑的表情，莫名的，我心里突然冒起的火似乎烧得更旺了。"
    mei_speaking "之前，我们不是说好的吗？说轮流做饭。"
    xiang_speaking "嗯，是啊。"
    mei_speaking "可我违反了约定。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "所以，难道你的意思是我应该对你发火？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "你就不生气？"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "我为什么要为了这种事生气……本来我跟你就不一样，再怎么说，我也没有立场对你发火吧？"
    mei_speaking "为什么？"
    xiang_speaking "我在这，都听你的还来不及——"
    mei_speaking "因为你觉得，我们只是租客和房东？"
    xiang_speaking "不然呢？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    show halfblack with dissolve
    mei "她斩钉截铁的话语打断了我所有的情绪，一瞬间，我竟然也搞不懂自己为何会心绪起伏。{p}为什么，似乎是我在生气……"
    mei "我深吸一口气，先努力按住了不安的胸口——以免说着说着，自己先晕过去了……"
    hide halfblack with dissolve
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "我怎样都可以，那你觉得，之前，我为什么跟你一起轮流做事？"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "什么？你可以跟我分担饭钱啊。而且，你也需要活动活动身体吧。\n你不是身体不好吗，刚好可以多活动一下，不就对你有好处吗。"
    xiang_speaking "那句话怎么说来着，各自要各自的？"
    mei_speaking "各取所需？"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "嗯！"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei_speaking "在你看来，这些都是各取所需吗。只是交易吗。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "是啊。"
    mei_speaking "暴风雨的时候，为什么，要来找我和彭江丽？"
    xiang_speaking "……"
    xiang_speaking "我跟你一起住在这里，如果你出事了，那我岂不是很难交代？"
    hide meiimg
    show meiimg shirt eye_still smile at char_left
    mei_speaking "好。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "所以你觉得，叶成华让你住在这就是为了收房租。隔壁，那几个奶奶找我们帮忙，是因为我们比镇上的人便宜方便。是这样吧？"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "……\n啊，可能吧。"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    mei "你以为房租才多少钱？还要冒着把陌生人带回家里的风险，还不是因为叶成华觉得你看起来很需要帮助……你以为我们做的能比得上镇上的专业公司吗，只不过是这里的人习惯了互相帮忙……"
    mei "当然，我知道这些都是一厢情愿，也不觉得只要付出过，就非要期盼别人有相同的回应。{p}但是，但是……"
    mei "做饭，吃饭，看夕阳，聊传说，暴风雨，讲故事，一起去帮忙，在你看来都是交易吗？"
    mei "我有很多话想说，但看到她不知什么时候变得毫无表情的脸，却突然觉得没力气开口了。{p}她都这么说了，就这样吧……"
    mei "好烦，总觉得，心脏好痛……"
    hide meiimg
    show meiimg shirt eye_still o at char_left
    mei_speaking "你脑子里只有这些吗？"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "……\n这样不好吗？"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    xiang_speaking "谁也不欠谁的。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "……嗯，我知道了。"
    hide meiimg with dissolve
    hide xiangimg with dissolve
    mei "我长长地吐出一口气，不再开口，只是避开她的目光往门外走去。"

    show xiangimg fist o at char_right with dissolve
    xiang_speaking "梅雨。"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "嗯？"
    mei "烦死了，为什么我下意识就转过头……"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "对，可能就像你说的那样，我应该就是个愚蠢又自私的人。{p}不过没关系，因为……我也不会在这里住很久嘛。就是还要麻烦你再忍受一阵子了。"
    hide xiangimg
    show xiangimg fist eye_still smile at char_right
    xiang_speaking "你要是想的话，我也可以不出现在你面前。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei "你就想说这些吗。{p}亏我还期待了一瞬间……"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "哦，你不想见到我的话，那之后就还是我做饭吧？抱歉啦，你是不是要休息会。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "嗯。\n没事，轮流。"
    mei "我咽下那句“没有不想见你”，只是尽量缩短词句，简要回应。"
    mei "我这次没有再回头，几乎用上跑步的速度，飞快地穿过楼梯，走到二楼，再也不要看到那个房间的身影。"

    scene bg_meiroom with fade
    mei "……"
    mei "气死我了，气死我了……"
    mei "你知道我花了多大勇气才主动找人说话吗？你知道你轻松做到的事情对我来说有多难吗？{p}结果你一点也不懂，根本不知道珍惜，也根本不理解这种事……"
    mei "亏我还天真地以为，你是因为我们变熟悉了才说出那些话……"
    mei "我才是愚蠢的人，你只不过是个……令人讨厌的家伙罢了。"
    mei "可恶……"
