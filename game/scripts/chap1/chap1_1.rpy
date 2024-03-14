image glitches:
    im.MatrixColor("images/glitch0.jpg",im.matrix.brightness(-0.3))
    pause 0.2
    im.MatrixColor("images/glitch1.jpg",im.matrix.brightness(-0.3))
    pause 0.2
    im.MatrixColor("images/glitch2.jpg",im.matrix.brightness(-0.3))
    pause 0.2

    repeat

label chap1_1:
    scene bg_meiliv with pixellate
    mei "吃过药后，我犹豫万分，还是到楼下打通了那个电话号码。"
    peng_speaking "是梅雨吗？你没事吧？！"
    mei_speaking "啊，啊，嗯……没事，抱歉，影响你了。"
    peng_speaking "怎么会！是我不好，非要当时拉着你走，明明之后再去也可以的……你现在还有没有不舒服？"
    mei_speaking "真的没事啦……"
    peng_speaking "那就好……那你，你要是以后有什么事，都可以跟我说……"
    mei_speaking "嗯，好。"
    peng_speaking "……"
    mei_speaking "……"
    peng_speaking "那，那就这样……你，啊，不……那我不打扰你啦。"
    mei_speaking "好。"
    mei "挂掉的电话声音像宣判我死刑的钟声，终于缓缓降下来。但在那一刻，我真的松了口气。\n绷紧的神经放松下来后，新的疲惫感涌上心头，但这次不是身体上的。"
    mei "真的，感觉糟透了……我不禁开始在心里埋怨起叶成华：如果不是她，如果不是她硬要把我带回来……"
    mei "……\n……只是，我也知道这根本只是在给自己找借口而已。"
    mei "是我自己糟透了才对……"

    scene bg_meiroom with pixellate
    na "咕噜……"
    mei_speaking "……\n……啊。"
    mei "好一会，我才意识到房间里突然出现的声音来自我的肚子。"
    mei "现在是几点了……我不得不面对现实，从卷成一团的被子里爬出来。\n真是的，我浪费了这么多时间，之后……嗯？之后……？"
    mei "不对，我已经不是在学校，治疗时间也早就结束了。没有要赶的课程，没有要做的检查。就算没浪费时间，也没有什么值得的事可以做。"
    mei "嗯，我现在就是这样毫无意义地活着……"
    na "咕噜。"
    mei "肚子的再次抱怨打断了我的自怨自艾。\n我叹了口气，没有换衣服的心情，只是草草披上外套准备下楼。"
    mei "我不会做饭，但不得不尝试了……叶成华肯定不会帮我准备，毕竟她现在不住这里，只是暂时把这间老房子借给我。"

    scene glitches with fade
    ye_speaking "哟，看这小脸瘦的，最近怎么样？"
    mei_speaking "……还好。"
    ye_speaking "你成天窝在这，是真还行？唔，你妈呢，只有你和阿姨在家？"
    mei_speaking "她不在。"
    ye_speaking "行吧，她又是这样。那你呢？你有什么打算没，有没有需要我帮忙的？什么都行，看你的想法。"
    mei_speaking "没。"
    ye_speaking "嚯，你是想持续这样吗，就一直待在家里？"
    mei_speaking "……\n嗯。"
    ye_speaking "……"
    ye_speaking "跟我走呗。"
    mei_speaking "啊？"
    mei "我有些惊讶地抬起头，对上叶成华的视线，又很快移开。还好她似乎并没感到惊讶，只是轻轻笑了一声。"
    ye_speaking "终于肯有点反应了，嗯，那就这样？"
    mei "我摇摇头，完全没听懂她在说什么。"
    ye_speaking "刚刚你不是说没计划吗，既然没其他事，跟我回去一段时间也不影响。"
    mei_speaking "去，哪……"
    ye_speaking "回立涧村啊，你搬出来之后好像还没回去过吧，刚好也可以看看现在啥样了。"
    mei_speaking "呃……"
    ye_speaking "反正你现在也是待在家，我把我那的旧房子借你，你一个人住段时间没问题吧。"
    ye_speaking "你呢也别想太多，我也不会打扰你，想干嘛干嘛，就是换了个地儿，其他一样的。"
    mei_speaking "我……"
    ye_speaking "那就这么说定了啊！别担心，要是你真不习惯了，我再送你回来就是了，没事的，啊。"
    mei_speaking "……"
    
    scene bg_meicorridor with Fade(1,1,1)
    mei_speaking "……"
    mei "这么想起来，当时我真的是完全被她带着走，简直是连哄带骗。\n回过神后，我也能明白她的良苦用心就是了……"
    mei "不过，昨天发生的事是不是完全辜负了她的心意啊。她大概会对我很失望吧……"
    mei "我怎么又开始了……嗯，别想了别想了，至少先下楼搞点东西——"
    mei_speaking "吃？！"

    show xiangimg o at char_right with moveinright
    unknown_speaking "……吃？你要吃东西？冰箱里有你姐姐给你留的菜，还有速冻饺子。"
    show meiimg shirt o at char_left with moveinleft 
    mei_speaking "……"
    hide meiimg 
    show meiimg shirt at char_left
    mei "楼梯口站着的人一头卷发，翘起来的毛格外显眼。听到我因惊讶爆发的声音，她转过头用手指了指楼下的方向。"
    if c0_x1 == 1:
        mei "她是我昨天在车站遇到的人……？我太过惊讶，以至于开始怀疑自己的眼睛和记忆。"
    mei "不，但……说到底为什么，我打开门会看见一个不认识的人站在这里？\n她完全没在意我，说完话就自顾自地转身走人了。"
    hide xiangimg with moveoutright
    mei "到底什么情况啊……我站在原地怔愣好一会才理清思绪。\n我没有移动电话，只好小心地下楼，好在那个奇怪的人似乎不在客厅，不知道去哪了。"
    mei "不过，不管她在哪，只要现在不在这里就行，我得赶紧先给叶成华打个电话。\n嗯，是这样……"

    scene bg_meiliv with pixellate
    mei_speaking "啊？"
    ye_speaking "抱歉啦我忙忘了，总之可能要麻烦你一段时间咯。不过她住在一楼，已经把东西搬下去了，每个房间也有独立的锁，所以问题不大。"
    mei_speaking "一楼……？这么突然？之前……"
    ye_speaking "哦那个啊，昨天碰巧看到她需要帮忙，就聊了一下。她在找房子，我觉得刚好可以让她短租，就让她搬进来咯。"
    mei_speaking "刚认识的人，搬进家里？"
    ye_speaking "没事没事啦，我有跟她说，她是住备用储藏室的，房间里有监控相机。况且，你房间又有锁，我每天也会过去看一次嘛。哦，要不要给你配个手机？"
    mei_speaking "不……等等，你说，房间里装相机？你——"
    ye_speaking "啊啊那个只是说着吓唬她的，我哪有钱装真的啊。不过她也答应了，而且，说不定人家真的有什么苦衷呢。还是个小孩，估计会守规矩的啦。"
    ye_speaking "你没其他事了吧？那我先挂了，晚上见哈。"
    mei_speaking "呃，好……"

    scene bg_meikitc with pixellate
    mei "嘶……我捏了捏眉心，试图理解现在的情况。总之，大概是有人要住进来一段时间吧。{p}这不是我的房子，所以我没资格说不同意或者别的什么，只是要接受这一点。"
    mei "不过那个人到底是怎么想的啊，叶成华也是……一个人让刚认识的人住进家里，另一个人完全接受自己住在有监控的房间——就算说是假的，她也不知道——真是难以理解她们……"
    mei "我叹了口气，把冰箱里的菜倒进锅里加热。"
    mei "天气仍然不错，客厅的窗外是碧蓝的背景点缀着绿色枝条。轻微的滋滋声响逐渐从锅里冒出来，我无所事事，只需要等着菜热好，在此刻怪异地感觉到内心十分平静。"
    mei "作为一天的开始，这个场景也许还算不错。\n当然，要是没有那两个人搞的事情就更好了……"

    scene bg_meicorridor with pixellate
    mei_speaking "嗯……？！"
    mei "我没想到，刚刚吃饭时才在心里吐槽过两个人，马上又遇到其中之一。{p}——这一回，我惊得连声音也发不出，只是赶紧转过头去，一眼也不想多看。"
    show q_x10 at cg_s with irisin 
    unknown_speaking "啊，我还以为房子里是我室友呢，还没习惯过来，不好意思啊。"
    mei "方才轻瞟一眼，我看到一个全身赤裸的女人从角落的洗手间里走出来，只有手里的拿着的浴巾堪堪遮挡住胸口。所以，她可以说是一丝不挂地站在我面前。"
    mei_speaking "你衣服呢？"
    unknown_speaking "我刚冲完凉，你要用厕所吗？那我快点。"
    mei_speaking "不用……啊，外面窗户没关。"
    unknown_speaking "行，没事，我就在这站会透透气，不走出去。"
    mei_speaking "呃，嗯。" 

    scene bg_meiroom with pixellate
    mei "我回到房间，虚掩上门，贴在门口仔细听着外面的声响。直到我确定外面的人已经离开，我才轻轻走到卫生间。"
    mei "为什么在自己家我还像做贼似的……虽然这也确实不是我家。\n大概就是一种难以言喻的不舒服的感觉吧。"
    mei "小时候我经常寄住在彭江丽家，但之后就没有和我妈以外的人住过。现在也不像小时候那么简单，因而像现在这样还是给我不习惯的感觉。"
    mei_speaking "啊，没有牙刷……"
    mei "对了，叶成华说过她很久没住这边，所以生活用品差的很多。\n她完全就是一时冲动把我带回来吧……看来今天得去一趟超市。"

    scene bg_meiliv with pixellate
    show xiangimg fist eye_squint o at char_right with dissolve
    unknown_speaking "哈……阿嚏！！"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "咿？！"
    hide xiangimg
    show xiangimg fist at char_right
    mei "到楼下，我又和一头卷发的女人撞见。本想就此忽略，但她忽然打出的巨大喷嚏让我愣了愣，下意识地转头看她。"
    hide meiimg
    show meiimg shirt at char_left
    mei "……是之前洗澡的时候着凉了吧……\n虽然现在已经是夏天的开始，但这里的早晚温差大，温度最低的时候一点也不像夏天。"
    mei "说起来，她这件衣服可能也不够厚……"
    return