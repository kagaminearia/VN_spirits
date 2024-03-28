label chap6_p1:
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "我也去吧，怎么送？"
    show yeimg smile at char_right with moveinright
    ye_speaking "啊，坐车回去，我先把她抱车上。"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left 
    mei_speaking "……三轮车？"
    mei "要用这个送人吗……{p}要不，还是把她直接叫醒吧……"
    hide yeimg
    show yeimg o at char_right 
    ye_speaking "咋可能呢！今天我们坐路花的车来的啊，正经小轿车！"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "哦……"
    mei "我不再多说，跟着她们往外走，和睡着的彭江丽一起坐在车后座。"

    lu_speaking "小梅啊，今天弄成这样，真是不好意思。"
    mei_speaking "诶……"
    lu_speaking "这话我来说其实不太适合，你就随便听听哈……{p}成华她也是想让你开心点，不过你要是真的不喜欢，之后直接去骂她就行，或者找我帮你骂！"
    mei_speaking "啊？不用……\n我没不高兴……也没生叶成华的气。"
    lu_speaking "真的？不要勉强自己哦。"
    mei_speaking "嗯，其实……"
    mei "其实我还挺高兴的……{p}但我没把这句话说出口。总觉得，有些不好意思……"
    mei "何况……"
    lu_speaking "怎么啦？"
    mei_speaking "啊，没……"
    lu_speaking "好吧，你没不高兴就好。也还是个孩子呢，开心最重要啦。"
    mei_speaking "谢谢……\n不过，那个，彭江丽没事吧？"
    lu_speaking "她就是睡着啦，你们估计都没怎么喝过酒，所以一下就醉了。还好你没喝太多，现在感觉晕吗？"
    mei_speaking "之前有点，现在还好。"
    lu_speaking "嗯，那行。唉呀，其实要我说呢，虽然有点意外，但小彭这时候睡一觉也好。\n她最近可忙了，你看那黑眼圈多严重啊。"
    mei_speaking "哎？怎么会……"
    mei "我心下一凉。说实在的，如果她没提到，我完全没有注意……"
    mei "那天之后她没有再联系我，我以为她生气了，也不敢联系她。\n原来不是因为生我气吗……但是，怎么会这么忙……"
    lu_speaking "之前那暴风雨不是很大嘛，大家都损失惨重。小彭那边也一样，最近她一直得忙家里的事情。"
    lu_speaking "你也知道的，小彭她，比较拼命嘛，也不愿意找别人去帮忙。一直在家，学校的补课就跟不上了，所以她最近都在熬夜学习呢。"
    lu_speaking "立涧村这边最近还在考虑，要不要把禁渔期临时取消一段时间——损失太大了，需要收入弥补。{p}要是取消了，就得开始打渔，那小彭之后估计还有的忙……"
    mei_speaking "……{p}这，这样啊……"
    lu_speaking "所以啊，看到她是睡着，其实我还松了口气呢。"
    mei "怎么会这样……\n后面的话，我已经没办法再听下去，脑子里只剩一片混乱。"
    mei "为什么，我……\n什么都不知道呢。"

    scene bg_vil5 with fade
    show halfblack
    show luimg smile behind halfblack at char_right with moveinright
    lu_speaking "好啦，你叫她起来吧，我这车没法再开进去了。\n里面你自己送她进去，可以吗？"
    show meiimg o behind halfblack at char_left with moveinleft
    mei_speaking "好。"
    mei_speaking "醒醒，醒醒……彭江丽？"
    peng_speaking "唔……嗯……"
    show pengimg shirt o behind halfblack at char_mid with dissolve
    peng_speaking "……诶？！\n怎，怎么回事……我睡着了？！天黑了？这，这是哪？"
    hide luimg
    show luimg laugh behind halfblack at char_right
    lu_speaking "没什么大事，就是你之前睡着啦。我跟小梅把你送回来了，之后的事你俩自己说吧~"
    lu_speaking "啊，这是你的衣服。穿上吧，小心着凉~"

    scene bg_vil5 with dissolve
    show halfblack
    show meiimg behind halfblack at char_left with moveinleft
    mei_speaking "……"
    show pengimg eye_still behind halfblack at char_right with moveinright
    peng_speaking "……"
    hide pengimg
    show pengimg eye_care smile behind halfblack at char_right
    peng_speaking "对不起啊，让你看笑话了。我没喝过酒，不知道反应这么大……\n明明是来庆祝你的生日的……"
    hide meiimg
    show meiimg eye_still behind halfblack at char_left
    mei_speaking "……"
    mei "我不想再听到她说对不起。"
    hide meiimg
    show meiimg smile behind halfblack at char_left
    mei_speaking "今天，我很高兴。谢谢。"
    peng_speaking "哎？"
    hide meiimg
    show meiimg o behind halfblack at char_left
    mei_speaking "所以……希望，你不要觉得对不起。{p}不高兴的话，可以跟我说吗？"
    hide pengimg
    show pengimg eye_care laugh behind halfblack at char_right
    peng_speaking "哎……啊，我，我没……我也很高兴……！"
    hide pengimg
    show pengimg smile behind halfblack at char_right
    mei "彭江丽的话语卡壳几次，这才全部说完。她的笑容不像勉强……我也有些放下心来。"
    mei "虽然我能做的事很少，但……\n至少……希望她能在跟我一起的时候，稍微放轻松一些。"

    scene bg_vil5 with dissolve
    show halfblack
    peng_speaking "对了，那个……"
    mei_speaking "嗯？"
    peng_speaking "虽然成华姐说不需要……但这次我没听她的……{p}嗯，你也别太在意……"
    mei_speaking "呃……什么？"
    peng_speaking "就是……\n这个……送给你！"
    mei "她猛地伸出手，手指紧紧地攥着一个精致的小发卡。\n发卡是细长的形状，主体透明，前端是一个色彩斑斓的小巧贝壳。"
    mei_speaking "诶，这是……"
    mei "我有些不可置信的看着那个熟悉的颜色和形状。"
    peng_speaking "嗯，是，是啊……就是，之前你说你觉得好看，我就想着，可以做一个东西送给你。啊，不过不是我做的，我只是找了人帮忙……"
    peng_speaking "对了，那个，就是……不会有味道吧？"
    mei_speaking "啊？没有没有……"
    mei_speaking "谢谢你……我，我不知道，该怎么才……"
    mei "我有些不知所措，两只手也只是僵硬着接过发卡，然后就完全不知道应该做什么动作好。"
    peng_speaking "别说啦，你能收下的话，对我来说就是最好的事情了。"
    show bg_black with dissolve
    mei "彭江丽笑了笑，她轻轻捏住我的手，从我的手里取回发卡。\n距离更近了，似乎能感觉到对方的气息。不知为何，我闭上了眼睛。"
    hide bg_black with dissolve
    mei "然后，额头上传来轻微的触感。我睁开眼，看到她微微倾身，将发卡别在我的刘海上。"

    scene bg_vil5 with fade
    show halfblack
    show pengimg laugh behind halfblack at char_right with moveinright
    peng_speaking "看，就像这样就行啦。\n果然很好看，跟我想象的一样。"
    show meiimg o shell behind halfblack at char_left with moveinleft
    mei_speaking "谢，谢谢……"
    mei_speaking "我，我帮你补课吧……"
    peng_speaking "……哎？"
    mei_speaking "啊，之前，路花跟我说的。她说你最近，学习有点累……我就想着，能不能帮你……啊，你要是不喜欢，就算了。"
    peng_speaking "没……就是，嗯，我怕麻烦你……"
    mei "彭江丽的笑容有些凝固，我慌忙解释，好在她似乎不是对我不满意……"
    mei_speaking "没事的……如果能帮到你……可以吗？"
    peng_speaking "当然，当然可以了。之后我联系你吧，今天我先回去了，抱歉，我还有些头晕……"
    mei_speaking "嗯，好……！"

    mei "彭江丽走之后，我才有些冷静下来，下意识抓住了自己的领口。还好，还好……今天没有晕过去……\n只是……"
    mei "之前一激动就说了那样的话，其实，我并没有自信能……"
    mei "但说都说了，不管怎么样，我也只能先试试了……"
    return