label chap3_2:
    scene bg_emptyroom with fade
    show halfblack
    $ renpy.sound.play(sound.close_water_tap, channel="sound", loop=False)
    mei_speaking "呼……"
    mei "黏着的水汽慢慢消散在空气中，身上的潮湿沉重感也尽数褪去。不幸中的万幸，二楼的水还能用。{p}我放松地舒出一口气，总觉得……平日里这种随处可见的情形，竟然感觉有些久违。"
    mei "现在，还在下着雨吧……{p}我在心里默念着明知道结果的问题，披上干净的外套往外走。"
    scene bg_black with fade
    show movie_side
    show video_4 behind movie_side with dissolve
    show video_5 behind movie_side
    $ renpy.sound.play(sound.wind, channel="nature", loop=True)
    $ renpy.sound.play(sound.rain_on_window, channel="sound", loop=True)
    mei "无数的雨点下，我站在窗前，幻想着它们落在自己身上。{p}但是没有，当然没有，它们只是落在雾蒙蒙的窗户上，发出噼里啪啦的敲打声。"
    mei "肆意飞溅，没有方向。{p}我，是不是也……"
    mei "我下意识地伸出手，却只摸到冰凉坚硬的玻璃。"
    mei_speaking "呼……"
    mei "果断的触感让我从不着边际的联想里回神。{p}是啊，我想什么啊……我怎么敢这样比较自己……"
    mei "我根本格格不入……就像……{p}就像我分明看得清外面的狂风暴雨，实际上却是被幕墙隔绝在原地。"
    show halfwhite with dissolve
    xiang_speaking "你冲完凉啦，站在这干什么？吓我一跳，我还以为你不见了。"
    mei_speaking "啊？嗯……只是看看。"
    mei_speaking "……回去吧。"
    xiang_speaking "嗯？好哦。"
    mei "既然已经被人注意，我也没有了继续待在这的心思。{p}况且的确……这种时候自己不打招呼就离开不太好。"

    scene bg_emptyroom with fade
    show halfblack
    show xiangimg fist smile behind halfblack at char_right with moveinright
    xiang_speaking "麻烦你啦，明明你住这里，竟然最后才冲凉。"
    show meiimg shirt behind halfblack at char_left with moveinleft
    mei "无所谓。"
    mei "我摇摇头，表示不太介意。{p}虽然我身体不好，但那仅限于平时的运动，像是感冒发烧之类的事反而比较少见。"
    show pengimg shirt eye_care behind halfblack at char_mid with moveinleft
    peng_speaking "对了，我在这里打扰……真的没事吗？"
    hide xiangimg
    show xiangimg fist o behind halfblack at char_right 
    xiang_speaking "就算你现在这么说也回不去啊。"
    hide xiangimg
    show xiangimg fist behind halfblack at char_right 
    mei "彭江丽没说话，甚至没有转头看向夏那边，只是直直地望着我。{p}这两个人真的没问题吗……我不由得有些担忧。"
    hide meiimg
    show meiimg shirt o behind halfblack at char_left
    mei_speaking "水退之前都住这，没问题。"
    mei_speaking "噢，这里条件不好……要不，你睡我房间。"
    hide pengimg
    show pengimg shirt o behind halfblack at char_mid 
    peng_speaking "啊？！不，不用了，就这里就可以了！"
    hide meiimg
    show meiimg shirt behind halfblack at char_left
    mei_speaking "……噢。"
    mei "我挠挠头，不太明白她为什么只在这时候反应这么大。{p}不过，如果她不介意和向夏一起，那就按照现在这样也算不错。"
    mei "虽然没有床，但地垫足以覆盖过半的房间地面，厚实温软，面积够大，即使睡几个人也没问题。{p}不过……"
    hide meiimg
    show meiimg shirt o behind halfblack at char_left
    mei_speaking "睡觉吗？"
    hide xiangimg
    show xiangimg fist o behind halfblack at char_right 
    xiang_speaking "太早了吧，而且之前还睡过了，感觉根本睡不着。\n不过，不睡觉好像也没事可做啊。"
    hide pengimg
    show pengimg shirt behind halfblack at char_mid 
    peng_speaking "没办法，现在电被断了，风和水都太大了，也没法修。"
    hide pengimg
    show pengimg shirt o behind halfblack at char_mid 
    peng_speaking "你们……也是倒霉，我好多年没见过这么大的暴风雨了。"
    hide xiangimg
    show xiangimg fist smile behind halfblack at char_right 
    xiang_speaking "嗨，像你说的，这也没办法……但是竟然见证了那种神奇的事情，其实也算幸运。"
    hide pengimg
    show pengimg shirt eye_still o behind halfblack at char_mid 
    peng_speaking "……\n{size=30}你不是这里的人，才会这样想。{/size}"
    hide pengimg
    show pengimg shirt behind halfblack at char_mid 
    hide meiimg
    show meiimg shirt behind halfblack at char_left
    mei_speaking "那个……啊。"
    mei "彭江丽的那句话声音很小，估计只有我听见了。"
    mei "本来想着跟向夏解释一下，但彭江丽做了个“嘘”的动作，好像并没有这个意图，我也只好作罢。"

    scene bg_emptyroom with fade
    show halfblack
    mei "我靠坐在房间的角落，只是低着头来回摆弄床垫。{p}如果抬头，就得面对向夏和彭江丽……但现在实在是无事可做，无话可说。"
    mei "室内只剩一盏小夜灯还在工作，平稳的光线将暗下来的房间点亮一角，也像拢起一层薄薄的膜，将纷乱嘈杂的因素全部挡在外侧。"
    mei "因而，即使窗户噼啪作响，暴风和骤雨肆意敲打玻璃和边框，此时此刻，却并未再像先前一样使人感到惊慌。"
    mei "在这片不知何时停止的暴雨中，我感到十分久违的宁静，甚至一瞬间希望就如此持续下去。"
    mei "可惜自然不行。"

    scene bg_emptyroom with fade
    show halfblack
    show xiangimg smile behind halfblack at char_right with moveinright
    $ renpy.music.play(music.xiang_handing_out, channel="music", loop=True, fadein=0.5)
    xiang_speaking "一起来玩游戏吧！"
    show pengimg shirt o behind halfblack at char_left with moveinleft
    peng_speaking "这不好吧。"
    mei "向夏“啪”的一声拍掌，兴奋提议。{p}我还没来得及反应过来，就听到彭江丽委婉的拒绝。"
    show meiimg shirt behind halfblack at char_mid with moveinleft
    mei_speaking "……"
    hide xiangimg
    show xiangimg o behind halfblack at char_right
    xiang_speaking "啊？为什么不好？"
    peng_speaking "为什么要玩？"
    hide xiangimg
    show xiangimg fist behind halfblack at char_right
    xiang_speaking "嗯，就是无聊啊。那不然，现在这么早，你要直接睡觉吗？"
    hide pengimg
    show pengimg shirt behind halfblack at char_left
    peng_speaking "是啊，我想睡了。"
    mei "……总觉得，这样的彭江丽很少见。{p}虽然语气很平和，但对她来说也许算是咄咄逼人了。"
    mei "不过，这样直接说出来，总比她自己憋着好……{p}反正，估计向夏也不会在意。"
    hide xiangimg
    show xiangimg fist o behind halfblack at char_right
    xiang_speaking "好吧，那你睡吧。我睡不着，只能继续坐这了，抱歉啊。"
    hide pengimg
    show pengimg shirt eye_still behind halfblack at char_left
    peng_speaking "……"
    mei "彭江丽并没有动，只是继续沉默地坐着。{p}也是，有两个人坐在旁边，谁能这样睡着……更不要说，现在她其实不困吧。"
    mei "其实，我大概能理解向夏的想法，毕竟，在这样的距离，面对面待着的确很尴尬……"
    hide meiimg
    show meiimg shirt o behind halfblack at char_mid 
    mei_speaking "要不……做点别的？"
    hide pengimg
    show pengimg shirt o behind halfblack at char_left
    peng_speaking "啊？梅雨你想做什么？"
    hide meiimg
    show meiimg shirt behind halfblack at char_mid 
    mei_speaking "……"
    hide meiimg
    show meiimg shirt o behind halfblack at char_mid 
    mei_speaking "一般……小说里，这种时候，都是讲鬼故事。"
    hide xiangimg
    show xiangimg fist eye_still o behind halfblack at char_right
    xiang_speaking "哇，不要啊——我很怕鬼的。"
    mei_speaking "不是无聊吗。"
    xiang_speaking "那，这也……"
    mei_speaking "讲完的话，还会有鬼陪着，马上就不无聊了。"
    hide xiangimg
    show xiangimg fist eye_shock o behind halfblack at char_right
    xiang_speaking "{size=50}哇你怎么现在就开始讲了犯规！{/size}"
    hide meiimg
    show meiimg shirt eye_wacky o behind halfblack at char_mid 
    mei_speaking "……呃，抱歉。"
    hide xiangimg
    show xiangimg fist behind halfblack at char_right
    hide meiimg
    show meiimg shirt behind halfblack at char_mid 
    mei "虽然很抱歉……但我却莫名有点想笑。{p}她好像也知道自己刚才的反应大了，说完后就马上收了声音。"
    hide xiangimg
    show xiangimg fist o behind halfblack at char_right
    xiang_speaking "好吧……我投降了。那，讲鬼故事也行吧，你们要讲吗？"
    hide pengimg
    show pengimg shirt eye_care behind halfblack at char_left
    peng_speaking "……"
    hide pengimg
    show pengimg shirt eye_care o behind halfblack at char_left
    peng_speaking "要吗？你确定？"
    mei "转变还真快啊……我实在佩服向夏的能伸能屈。我看向彭江丽，她虽然没拒绝，但似乎有些担心。{p}……她是还在担心向夏吗？"
    xiang_speaking "不玩游戏，讲讲故事也没什么的吧。"
    hide meiimg
    show meiimg shirt o behind halfblack at char_mid 
    mei_speaking "你不是怕吗。"
    hide xiangimg
    show xiangimg fist smile behind halfblack at char_right
    xiang_speaking "反正你刚刚也讲过了，而且，现在也这么多人呢。"
    hide pengimg
    show pengimg shirt o behind halfblack at char_left
    peng_speaking "……我不会讲。"
    xiang_speaking "没事的，主要是为了气氛，在这干坐着不是更尴尬吗？好歹找个话题，随便讲讲就行了嘛，如果不想的话，随便讲点别的也行啊。"
    hide xiangimg
    show xiangimg fist laugh behind halfblack at char_right
    xiang_speaking "对了，讲完之后，还可以投票，选出讲得最好的，然后来点奖励。"
    hide meiimg
    show meiimg shirt behind halfblack at char_mid 
    mei_speaking "……"
    mei "怎么反倒是她劝起来了……{p}不知道是不是因为顾虑到我，虽然彭江丽看起来兴致不高，但最终也点了点头。"
    mei "果然……我不知道该庆幸还是该不安。{p}是她的话，即使自己有顾虑，基本上也不会让人为难。"
    stop music fadeout 0.5

    scene bg_emptyroom with fade
    show halfblack
    mei "向夏把放在一旁的小夜灯摆到中央，微弱的光线只能大概照亮我们三个人的下半张脸。\n配合窗外的阴沉天气，暴风骤雨，还真的是很像小说里写的鬼故事场景……"
    show xiangimg fist smile at char_right with dissolve
    xiang_speaking "那，我先开始说啰。"
    peng_speaking "嗯。"
    mei "我跟着点点头。{p}这事谁开头都无所谓，我们没人非得争这个，自然没什么意见。"
    $ renpy.music.set_pause(True, channel="sound")
    $ renpy.music.set_pause(True, channel="nature")
    hide xiangimg

    show xiangimg fist eye_still o at char_right
    xiang_speaking "我想想该怎么说啊，嗯，讲个……主角是小女孩的故事吧。"
    xiang_speaking "有一天，小女孩的家里人带回一个布袋，说那是可以给带来好运的宝藏。"
    xiang_speaking "女孩的家庭不富裕，但生活上也没有太多不便。然而自从有了宝藏，他们像着了魔一样整天围着放着宝藏的房间，把家里有的东西全部投入进去，也不再关注女孩。"
    xiang_speaking "小女孩不敢掺和家里的事，但家里人越来越奇怪，他们的脸变得扭曲，对女孩变得苛刻而暴躁。\n她想求救，可是，除了她以外，所有人都说家人很正常。"
    xiang_speaking "女孩从小习惯忍受，但终于有一个晚上她饿得受不了了，就在家里人睡觉之后起来，想找点吃的。"
    xiang_speaking "那天，房间昏暗，声音却格外清楚。她轻轻挪动脚步，偷偷走进厨房，生怕自己的声音吵醒家人……"
    xiang_speaking "灶台上什么都没有，女孩小心翼翼地在橱柜里翻找，却只翻出一张皱巴巴的，字迹混乱的纸条。"
    xiang_speaking "她会认的字不多，在窗外的月光下野只能勉强辨认出部分文字：……为治……于……方子……成年……处女之血……"
    $ renpy.music.play(music.right_behind_you, channel="music", loop=False)
    xiang_speaking "她想继续读的时候，却发现除了自己轻轻朗读的声音，好像还有别的声音出现在背后。\n然后，很轻的女人的声音从后面响起来。"
    xiang_speaking "那个声音说……"
    xiang_speaking "你是不是，看到了？"
    
    scene bg_black with dissolve
    stop music fadeout 0.5
    "啪。"
    $ renpy.music.set_pause(False, channel="sound")
    $ renpy.music.set_pause(False, channel="nature")
    mei_speaking "嘶……"
    mei "话音刚落，向夏按掉了小夜灯，房间里瞬间变黑，令我不自觉感叹一声。"
    scene bg_emptyroom with fade
    show halfblack
    mei "等了一会，我重新开灯，看到向夏嘿嘿一笑，彭江丽则是双眉微皱，一副思考的样子。"
    show xiangimg fist smile at char_right with moveinright
    xiang_speaking "好了，我讲完了。"
    show pengimg shirt eye_still at char_left with moveinleft
    peng_speaking "所以最后是什么意思？主角怎么样了？"
    xiang_speaking "你猜？"
    show meiimg shirt o at char_mid with dissolve
    mei_speaking "所谓的方子，和主角有关？"
    hide pengimg
    show pengimg shirt eye_care at char_left
    peng_speaking "哇，真恶心。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "你怎么能这么说呢，这叫艺术创作，都是虚构的好嘛。"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "……"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "好吧，别在意这个了，下一个谁讲？"
    hide pengimg
    show pengimg shirt o at char_left
    peng_speaking "我来吧。"
    peng_speaking "对了，这个并不算跟村子有关的故事，就像我之前说的，这里的信仰本质上并不是鬼神一类的东西……"

    $ renpy.music.set_pause(True, channel="sound")
    $ renpy.music.set_pause(True, channel="nature")
    $ renpy.music.play(music.peng_horror_story, channel="music", loop=False, fadein=1.0)
    peng_speaking "有一个少女醒来，发现自己被困在不认识的走廊。\n身后和两边都是墙，只有一条又长又直的路。"
    peng_speaking "她只能前进，每走一步，脚下的地板都在剧烈摇晃，所以她只能加快速度，越来越快。"
    peng_speaking "但是，她走快之后，她发现两边的墙壁也动了起来。\n而且它们是向内收缩的，也就是说……她要被压住了。"
    peng_speaking "她拼命想逃，可是无论怎么跑都看不到走廊的尽头。"
    peng_speaking "最后，她还是没有逃出去，被不断压缩的空间压死了。"
    stop music

    scene bg_emptyroom with fade
    show halfdarkblue
    show xiangimg fist o at char_right with moveinright
    $ renpy.music.set_pause(False, channel="sound")
    $ renpy.music.set_pause(False, channel="nature")
    xiang_speaking "……"
    show meiimg shirt at char_mid with moveinright
    mei_speaking "……"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "就没了？"
    show pengimg shirt at char_left with moveinleft
    peng_speaking "是啊。"
    hide xiangimg
    show xiangimg fist at char_right
    hide meiimg
    show meiimg shirt o at char_mid
    mei_speaking "我还以为，你会讲以前，我们上山的故事。"
    hide pengimg
    show pengimg shirt o at char_left 
    peng_speaking "那个啊……从结尾来看，不算鬼故事吧？"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "也是……"
    mei "可能是那时候还小，所以才吓得不轻。现在想来，确实没什么特别的……{p}况且，最后……"
    hide xiangimg
    show xiangimg fist eye_squint o at char_right
    xiang_speaking "什么啊什么啊，你们怎么还偷偷交流的。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "还有，这根本不算恐怖故事吧。而且你还说我，这个明明更变态好不好！人都被压死了哎。"
    hide pengimg
    show pengimg shirt at char_left 
    peng_speaking "我都说过了，我不会讲恐怖故事。"
    hide meiimg
    show meiimg shirt o at char_mid
    mei_speaking "其实，还行啦……\n到我吗？"
    mei "我生怕她们又吵起来，试探地询问道。{p}不过，她们似乎也没有真的要吵架的打算，只是单纯性格不合，动不动就互呛几句而已。"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "行啊，你继续，讲完了我们再一起投票玩。"
    hide meiimg
    show meiimg shirt at char_mid
    mei_speaking "好。"
    hide meiimg
    show meiimg shirt eye_still at char_mid
    mei_speaking "嗯，我也不会讲，所以只是，随便试试……"
    $ renpy.music.set_pause(True, channel="sound")
    $ renpy.music.set_pause(True, channel="nature")

    scene bg_emptyroom with fade
    show halfdarkblue
    $ renpy.music.play(music.mei_horror_story, channel="music", loop=True, fadein=0.5)
    mei_speaking "住院部的晚上是很安静的，但这一天却不太一样。"
    mei_speaking "少女在换药之前就醒了，她觉得有些奇怪，因为，她是被病床下的摩擦声吵醒的。"
    mei_speaking "刺啦，刺啦……像是撕扯衣服的声音从床下传来，在她愣神的时候，声音还在继续，没有停止的迹象。"
    mei_speaking "少女很害怕，她不敢看发生了什么，只是轻手轻脚地下床。"
    mei_speaking "她缓慢地移动，不敢发出任何声音。直到离开病房，少女才在走廊上拨通值班室的电话。"
    mei_speaking "‘您好，请问……’\n‘快回去吧。’"
    mei_speaking "‘咦？’少女没能说完话就被打断了，她有些困惑，却又感到隐隐的不安从心底滋生。"
    mei_speaking "‘病人，不要擅自离开病房。’"
    mei_speaking "‘可是，有……’"
    mei_speaking "‘要听话哦，快回去吧。快回去吧快回去吧要听话哦快回去吧要听话哦快回去吧快快快快快……’"
    mei_speaking "电话里的声音逐渐加速，变得凌厉而高亢，直至变调。\n少女吓得挂断了电话，也同时发出了巨大的叫声。"
    mei_speaking "糟糕了……少女也意识到自己出声，惊恐地四下张望。还好，仍然是平时的走廊。\n黑暗，空旷，墙上点缀着应急灯，映照出窗户上的朦胧黑影……"
    mei_speaking "不对，这里什么时候有过黑影？\n应该是错觉吧……"
    mei_speaking "她这么想着，就见到窗边那片的影子动了起来。"
    mei_speaking "它倏地开始变形，一团模糊的圆逐渐长出枝叶。细长的，扭曲的长条触手疯狂地蠕动，距离窗沿的位置越来越近。"
    mei_speaking "这，这是什么啊……"
    mei_speaking "巨大的恐惧感令少女完全无法行动，只是呆站在原地看着一切。"
    mei_speaking "如果这是噩梦就好了……她闭上眼睛，狠狠地掐了自己的脸颊。"
    mei_speaking "很痛，痛得她恢复神志，现在，应该逃跑才对……她猛地睁开眼睛。"
    mei_speaking "——密密麻麻的尖牙占据了她的全部视野。"
    $ renpy.music.play(sound.woman_scream, channel="others", loop=False)
    mei_speaking "又一声惊叫传来，但这之后，走廊上再也没有任何声响。"
    stop music

    scene bg_emptyroom with fade
    show halfdarkblue
    show meiimg shirt at char_mid with dissolve
    $ renpy.music.set_pause(False, channel="sound")
    $ renpy.music.set_pause(False, channel="nature")
    mei_speaking "……完。"
    mei "虽然我已经说得很慢，虽然我全程语气平淡，没用任何多余的力气，但这可以说是我第一次说这么多话。"
    mei "因而，我还是觉得有些累，还有些发晕，到结束语的时候就只剩下短短一个字。"
    show xiangimg fist at char_right with dissolve
    show pengimg shirt at char_left with dissolve
    mei "我抬起头，出乎意料的，竟然觉得有些紧张。{p}她们好像都没什么表情，看得我心里一紧。"
    hide meiimg
    show meiimg shirt o at char_mid 
    mei_speaking "呃……"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "哇哦，你这个故事还挺有意思的，不过我还期待后续呢就结束了。"
    hide pengimg
    show pengimg shirt laugh at char_left 
    peng_speaking "是啊，你真的好厉害。"
    hide xiangimg
    show xiangimg fist laugh at char_right
    xiang_speaking "感觉我还是第一次听你说这——么多话，没看出来啊，你平时不说话，还能编出这么好的故事。有一瞬间真的吓到我了诶。"
    mei "向夏还维持捂着胸口的动作，有些夸张地点评道。"
    hide pengimg
    show pengimg shirt at char_left
    peng_speaking "喂，哪有你这样说……"
    mei_speaking "因为，不是我编的。"
    hide xiangimg
    show xiangimg fist eye_shock o at char_right
    xiang_speaking "……哈？"
    hide meiimg
    show meiimg shirt at char_mid 
    mei "抱歉，彭江丽，明明你帮我说话……\n不过这是事实……"
    mei "而且，看到向夏这个反应，真的很有意思……"
    hide xiangimg
    show xiangimg fist at char_right
    hide meiimg
    show meiimg shirt o at char_mid 
    mei_speaking "呃，就是，这是，小说里的。"
    mei "我只是把内容大概背下来而已……不然，怎么可能这么顺畅地说这么长的话。"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "哇，你也太过分了吧，竟然讲别人写好的故事，都不是你自己想的。"
    hide meiimg
    show meiimg shirt at char_mid 
    mei_speaking "不行吗？"
    xiang_speaking "好像，也没有……好吧，早知道我一开始就说一下了！但这个谁能想到啊！"
    mei "我耸耸肩，并不在意她的控诉。反正，要我编的话，我确实编不出来，这能怎么办啊。"
    hide pengimg
    show pengimg shirt o at char_left
    peng_speaking "能背下来也是一种本事啊，如果让你背你就能背吗？"
    hide xiangimg
    show xiangimg fist eye_close o at char_right
    xiang_speaking "那我不能，那，她这个确实厉害好吧！"
    hide meiimg
    show meiimg shirt eye_still at char_mid 
    mei_speaking "……"
    mei "虽然不知道她们把这事想成了什么，不过，真实的事情大概率跟她们想象的不同……"
    mei "身体状态最不好的时候，我总是过分疲惫，很难长时间醒着。但我不服气，就想了个读恐怖故事把自己吓醒的办法。"
    mei "现在想来真是很蠢的行为……"
    mei "不过，虽然效果一般，但唯一一本有恐怖故事的小说已经被读了许多遍，以至于这一段我已经能够背下来了。"

    hide xiangimg
    show xiangimg o at char_right
    xiang_speaking "那我们来投票吧，写自己想投的人，待会一起翻出来。"
    hide meiimg
    show meiimg shirt o at char_mid 
    mei_speaking "然后呢？"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "也不搞什么太过分的，票数最低的人要回答其他人的问题或者听一个小要求，怎么样？"
    hide pengimg
    show pengimg shirt at char_left
    peng_speaking "行啊。"
    mei "向夏从她那不知道装了多少东西的包里掏出便签纸和圆珠笔，我点点头，把东西接过来。"
    mei "虽然很无聊，不过现在本来也没别的事做……投给谁呢？"

    return

