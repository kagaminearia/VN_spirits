label prologue_0:
    scene bg_vil1 with dissolve:
        function WaveShader(period = 3, amp=2.0, repeat='mirrored', double="both")
    mei_speaking "呕……咳，咳咳……！"
    mei "我摇摇晃晃地跌下车，立马弓起腰开始干呕。如果不是手臂被旁边的人抓住，双腿简直要支撑不住身体。但没办法，先让我吐完再说……"
    show bg_vil1 with dissolve:
        function WaveShader(period = 4, amp=6.0, repeat='mirrored', double="both")
    mei_speaking "咳咳，呼……哈啊……"

    scene bg_vil4 with fade:
        function WaveShader(period = 2, amp=1.0, repeat='mirrored', double="both")
    mei "突然起身让大脑有一瞬间的缺氧，我长长地吐出一口气，终于从晕车里缓了过来。"
    scene bg_vil4 with dissolve
    mei "眼前是空旷的浅蓝色天空，云层稀疏，明朗的日光照耀着低矮的建筑群……{p}照理来说，我应该觉得很熟悉，但此刻更多的却是陌生的感觉。"
    mei "不过，同样是这时候的大晴天，也许是因为这里更北，没有我之前住的地方那般炎热，让人舒服不少。"
    
    show yeimg at char_right with easeinright
    unknown_speaking "这就不行了吗，你的身体素质也太差了吧。"
    show meiimg at char_left with easeinright
    mei_speaking "……"
    mei "我无言移动视线，看向扶着我的女人。叶成华，我那不太熟悉却又过分自来熟的表姐，正夸张地冲着我叹气。"
    ye_speaking "有说错嘛？你不就是这样，坐车而已，才坐了不到一个小时。"
    hide meiimg
    show meiimg eye_still at char_left
    mei_speaking "……"
    mei "视线再次移动，落在旁边的那辆……三轮车上。\n老旧，破烂，生锈，歪七扭八，横杠成了斜杠。她所声称的，就是这样的……车。"
    mei "虽然以前也搬家过，但这么长时间，又辗转这么多次，条件还不好的还是第一次。"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "……你要是把……挖苦的时间，用来把车骑稳一点……就好了……"
    hide meiimg
    show meiimg eye_still at char_left
    mei "我太久没说过话，又是好不容易说这么长，更是累得要命，说一段就得缓一会。"
    ye_speaking "得了，这下又怪到我头上。"
    hide meiimg
    show meiimg at char_left
    mei_speaking "……"
    mei "实在有气无力，说不过她。经过几句反驳的时间，我终于缓过来——在夏初的中午，太阳还剩不少活力，再加上一路的颠簸弯折，坐在这平板三轮车上的我没彻底晕倒真是奇迹。"
    mei "不过，等不舒服的感觉褪去后，我能感觉到舒适而流动的空气扑上脸颊。的确比沉闷的房间好很多……我也能理解叶成华的想法。只是，对我来说……"
    ye_speaking "还是不行吗？要不要我背你走？不用担心，虽然我平时只对女朋友这么做，但偶尔也是可以关照下我妹妹的哦、"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "……\n不用……\n对了……这个，给我。"
    mei "这人虽然还是那么浮夸，但也的确让我轻松许多，即使很久不说话，说出口后也能显得自然了。"
    ye_speaking "行，你要是不舒服就说啊，我女朋友不会吃醋的。不过马上就到了，应该没事儿。"
    mei_speaking "呃，嗯……\n……谢谢。"
    mei "叶成华爽快地点点头，没有预想中的过分客气和谨慎。我从她手中接过一个行李箱，心里莫名松了一口气。"

    scene bg_vil1 with dissolve
    mei "道路蜿蜒而更加凹凸不平，所以我干脆跟在车后面缓慢踱步，尽管累，总比晕到死要好。"
    
    scene bg_meihome with dissolve
    mei "穿过草丛树木和几座平房，阳光穿过枝叶的缝隙落下，形成斑驳的光影。风吹过的叶片簌簌声和鞋底与砂砾的摩擦声音混合，给我熟悉又陌生的感觉。"
    mei "以前我在这里生活过一段时间，但那时候太小，只剩下很模糊的记忆。{p}与其说是回到老家，不如说像是到一个新地方重新开始。"
    mei "嗯……重新开始，吗……总感觉是个很糟的比喻。"
    mei "我强硬地止住了更深入的想法，避免自己总是旧事重提。"

    scene bg_meiliv with dissolve
    show yeimg smile at char_right with easeinright
    ye_speaking "进来吧。我最近在这边待的时间不多，给你的房间只是简单收了一下，可没有那么好的条件啊，你别太抱怨。"
    show meiimg o at char_left with easeinleft
    mei_speaking "哦……好。"

    scene bg_meiroom with dissolve
    mei "房间只有必要的大件家具，显得空间更为开阔。我跟着叶成华从楼梯上到二楼，进到这个风格一样的卧室。"
    mei "同色系的双人床，竖柜，一大一小两张桌子，简约到甚至有些简陋。\n不过我不是那种太注重精致环境的人，因而至少从宽敞程度来说，这里给我一种挺舒适的感觉。"
    show meiimg eye_still o at char_left with easeinleft
    mei_speaking "谢谢……我要做什么吗？"
    show yeimg smile at char_right with easeinright
    ye_speaking "不用啊，你就好好休息呗，坐完飞机又坐车，还走了这么久，估计累得慌吧。要吃东西的话，楼下冰箱里有。"
    hide meiimg
    show meiimg at char_left
    mei "你也知道啊……之前还一副大惊小怪的样子。我没有说出口，只是盯着她，希望她能看出我眼神里传出的幽怨"
    hide yeimg
    show yeimg at char_right
    ye_speaking "放心啦，我很忙，也不会干涉你，你就在这里住一段时间，其他都跟以前一样，可以不？"
    mei "只可惜她没有，还是笑嘻嘻的。不过，她的确说得有道理。\n只是住在这……我沉默着点点头。"
    hide yeimg
    show yeimg smile at char_right
    ye_speaking "哦！说起来，你不提醒我还真的要忘记了，算是有一件事吧，不过也不是要你做什么。"
    hide yeimg
    show yeimg at char_right
    ye_speaking "你还记得彭江丽吗？"
    hide meiimg
    show meiimg eye_still at char_left
    mei_speaking "……"
    hide meiimg
    show meiimg eye_still o at char_left
    mei_speaking "啊，嗯。"
    hide yeimg
    show yeimg smile at char_right
    ye_speaking "那就好。她还住这儿，我今晚约了她一起吃饭，毕竟你好不容易回来一趟。要是无聊，待会可以先去找她玩玩。"
    hide meiimg
    show meiimg eye_close o at char_left
    mei_speaking "……嗯。"
    hide meiimg
    show meiimg eye_still at char_left
    ye_speaking "不是什么急事，我也就是告诉你一下以免忘了，你现在不舒服咱们晚上聊也是一样的。"
    mei_speaking "噢……"
    ye_speaking "行了，我今天还得去东边走一趟，你有事的话去楼下打电话就行，先拜拜啰！"
    hide meiimg
    show meiimg eye_close at char_left
    mei_speaking "……"
    hide meiimg
    show meiimg eye_still o at char_left
    mei_speaking "好。"
    hide meiimg
    show meiimg eye_still at char_left
    hide yeimg with easeoutright
    mei "我终于抬起头，看到她离开的背影，风风火火，一点也不拖泥带水，显得我这突然涌起的情绪是如此没必要。{p}……随便吧，我已经无所谓了……"
    hide meiimg with dissolve
    mei "十一岁之前，我一直在这里生活。我妈很忙，总是把我留在彭江丽家。她是那时我唯一的朋友。虽然记忆已经模糊，但的确是我少有的单纯快乐时间。"
    mei "只是在搬走之后，我没能再联系上她，我们再也没有联系过。\n记忆随着年龄不断堆叠，逐渐忘了最开始的那些。"
    mei "我以为她讨厌我，或者早就忘记我了……所以，她也还记得我吗，现在又是怎么想我的？如果答应吃饭的话……是不是不排斥见到我的意思？"
    mei "我的思绪许久没有这么活络，却尽是些不着边际的想法。不，或许是一种说不上原因的害怕吧……以至于我不确定要不要去提前和她见面。"
    mei "既然如此……还是先睡一觉吧——我果断选择了逃避。"

    scene bg_meiroom with fade
    mei_speaking "好晕……啊，这里是……"
    mei "我愣了一会才回过神来，自己现在不在家里，而是暂时搬到了镇上，是这么回事……"
    mei "窗外的日光晃了晃眼，我回想起先前叶成华的话。距离晚上还有一段时间，我现在应该……？"

