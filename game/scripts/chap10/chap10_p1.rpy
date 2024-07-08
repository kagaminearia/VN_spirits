label chap10_p1:
    scene bg_meiliv with fade
    show yeimg smile at char_right with moveinright
    $ renpy.music.play(music.awkward, channel="music", loop=True, fadein=0.5)
    ye_speaking "所以，你姐我为了你的事特意大晚上从家赶过来，你自己说跑就跑了，还不给个消息？"
    show meiimg shell red at char_left with moveinleft
    mei_speaking "呃，这是……"
    mei "叶成华笑眯眯地盯着我，我却只觉得有些尴尬，还浑身发凉。"
    hide meiimg
    show meiimg eye_close shell at char_left
    mei_speaking "这是个意外……嗯。"
    ye_speaking "哈，又是意外？哪来那么多意外？！这意外还这么着急，连个电话都不能打了？！"
    hide meiimg
    show meiimg shell at char_left
    mei_speaking "呃……"
    mei "我难得心虚地看着叶成华。毕竟，她说的完全没错，这事是我给她搞了个大麻烦……"
    mei "我见到彭江丽后，就把其他事情都忘了，直接带她回了家，还是叶成华没找到我，给我打电话我才想起来的。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "对不起，我错了。"
    hide yeimg
    show yeimg o at char_right
    ye_speaking "你……哎！"
    ye_speaking "你真是啊……知不知道有多危险啊？"
    mei "这也确实……我后来才知道，彭江丽是完全认识路的，只是她发现我跟进去了，之后的时间都在用来找我。"
    ye_speaking "你有没有想过，万一你出事了，我咋跟你妈交代啊？"
    hide meiimg
    show meiimg eye_still shell at char_left
    mei "我这算不算弄巧成拙……不过，好在结果是好的……"
    ye_speaking "完了我这么担心你，你就说个意外？你倒是没事了，我担心死了！"
    hide meiimg
    show meiimg eye_close shell at char_left
    mei "……我无奈地听着叶成华的控诉，没有回话。她极少这样，这次也是我太过分了。"
    mei "要不，解释一下……反正她也知道一些……"
    ye_speaking "我不是想骂你，就是想跟你说，在外面的时候要小心一点啊。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "嗯，我知道。"
    ye_speaking "唉，我也不说多的了，你也别有什么添麻烦的破想法，之后有什么事还是可以随时打电话给我。懂不懂？"
    hide meiimg
    show meiimg shell at char_left
    mei_speaking "好。"
    stop music fadeout 0.5
    mei "想了想，我斟酌着，还是决定跟叶成华解释清楚，免得她太担心。"
    mei_speaking "之前，呃……"
    hide meiimg
    show meiimg o shell at char_left
    $ renpy.music.play(music.peng_night_stay, channel="music", loop=True, fadein=0.5)
    mei_speaking "之前在外面的时候，丽丽跟我说她喜欢我，所以我就把其他事都忘了，也忘了打电话。"
    hide meiimg 
    hide yeimg 
    show q_y1 at cg_s with vpunchm
    ye_speaking "{size=48}噗……！！！{/size}"
    mei_speaking "……"
    mei "好像是有点直接……我说完之后，后知后觉地感到有些羞赧。"
    mei "但说都说了……我只好低下头，掩盖住自己的表情，装作冷静的样子。"
    mei_speaking "{size=30}呃我是……实话实说……{/size}"
    ye_speaking "你，你们——咳，咳咳咳！"
    mei_speaking "……小心呛到。"
    hide q_y1 with dissolve
    ye_speaking "……行，我没事，没事——总之呢你之后注意安全就好。"
    ye_speaking "那你们先聊啊我也不打扰了，我先回去了。"
    mei_speaking "……噢，好。"
    mei "等等……她说什么你们先聊？"
    mei "目送叶成华离开之后，我才回味过来她刚刚的话。"
    show pengimg red at char_right with dissolve
    mei "转过头，只见彭江丽站在楼梯口，满脸通红地看着我。"
    show meiimg eye_shock o shell at char_left with dissolve
    mei_speaking "……"
    stop music fadeout 0.5
    hide meiimg
    show meiimg eye_shock shell at char_left
    hide pengimg
    show pengimg o red at char_right 
    peng_speaking "那个，我就是……想来看看你有没有被成华姐骂，想帮你求求情。"
    hide meiimg
    show meiimg eye_shock shell red at char_left
    mei_speaking "……你，你都听到了？"
    hide pengimg
    show pengimg red at char_right 
    peng_speaking "……嗯。"
    scene bg_meiliv with dissolve
    mei_speaking "……"
    mei "我一脸呆滞地站在原地，好一会儿，空白的大脑里跳出突兀的几个字。"
    scene bg_white with dissolve
    mei "天道好轮回……"

    scene bg_meiliv with Fade(0.3,0.5,0.3)
    show meiimg o shell red at char_left with dissolve
    $ renpy.music.play(music.peng_awkward_talk, channel="music", loop=True, fadein=0.5)
    mei_speaking "呃，我刚刚，就是跟叶成华解释一下……没有别的意思。"
    show pengimg o red at char_right with dissolve
    mei "回过神来，我试图说明当时的行为，但彭江丽还是杵在原地，没有反应。"
    hide pengimg
    show pengimg red at char_right
    hide meiimg
    show meiimg eye_still shell at char_left
    mei "也是……我那样说，该不会被认为是在炫耀吧？可我真没有那个意思……"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "我的意思是——"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "我知道的。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "——啊？你知道什么……"
    hide pengimg
    show pengimg eye_still o at char_right
    peng_speaking "就是……是我跟你，嗯，我跟你表白的。你……不用做什么。"
    mei_speaking "……啊？"
    mei "不对，她这是什么意思……"
    peng_speaking "我向你表白是我自己的事，你不用有任何负担的。{nw=0.5}"
    peng_speaking "我不需要回应什么的，或者任何东西，只是……只是想告诉你，你真的是个很好的人，而已。{nw=0.5}"
    peng_speaking "其实……只要还能跟你产生联系我就满足了，我是这么想的。{nw=0.5}"
    peng_speaking "但是，见到你之后，又忍不住想要更加接近你。明知道我根本不应该……{nw=0.5}"
    peng_speaking "如果你没有追过来找我……或者，如果你一开始没有直说，我应该，一辈子也不会告诉你。{nw=0.5}"
    peng_speaking "我本来真的不想说的，我不想让你为难，所以准备永远瞒着你的。{nw=0.5}"
    peng_speaking "结果都怪我不小心，让你听到那些话，现在还得意忘形，直接跟你说。{nw=0.5}"
    peng_speaking "但是现在让你知道……我也不后悔，因为你真的很好。{nw=0.5}"
    peng_speaking "不过我也知道，这都是我自己的事，就算我说了你也不用在意的。{nw=0.5}"
    peng_speaking "我知道你肯定觉得麻烦了，但是你不用做任何事，之后也{nw=0.5}"
    hide meiimg
    show meiimg eye_shock o shell at char_left
    mei_speaking "停停停——"
    hide meiimg
    show meiimg eye_shock shell at char_left
    mei "眼看着彭江丽越说越来劲，我慌忙伸出手晃了晃，她这才回过神，"
    hide pengimg
    show pengimg eye_still at char_right
    peng_speaking "啊……呃，就是，这样……"
    hide meiimg
    show meiimg shell at char_left
    mei_speaking "……怎样？"
    peng_speaking "就是……我跟你说那些，都是我自己的意思，你不用在意……"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "……你怎么知道我不喜欢你？"
    stop music
    scene bg_meiliv with dissolve
    mei "我脱口而出。而后，我们两个人面面相觑，僵硬地杵在客厅。"
    mei "但话都说到这了……我强行让自己冷静下来，而后定定地，认真地看向她。"
    $ renpy.music.play(music.peng_confess, channel="music", loop=True, fadein=0.5)
    mei_speaking "我说真的。我……彭江丽，我喜欢你。"
    peng_speaking "……"
    peng_speaking "怎么可能……"
    peng_speaking "你怎么会……我……"
    mei "和我想象的不一样，彭江丽并没有又变得激动。甚至，她面无血色，怔怔地低下了头。"
    peng_speaking "……不应该这样……我怎么能……"
    mei_speaking "……彭江丽？你……没事吧？"
    mei "我十分担忧地凑上前去，她却轻轻转头，避开了我。我不敢再做什么，只好站在原地。"
    mei "只是……"
    mei_speaking "……"
    mei_speaking "我不知道你是怎么想的。所以……嗯，你是因为，我小时候……突然离开，所以一直在生气吗？"
    mei "这件事我们总是默契地避而不谈，从来没有面对过。现在说出来，我也不免也偏开视线，不敢直接看她。"
    scene bg_black with dissolve
    peng_speaking "……"
    show cg_p151 at cg_0 with dissolve
    peng_speaking "不是这样的。"
    mei "她突然把头转回来，像是下定什么决心，强迫自己直直地看向我。"
    mei_speaking "啊？"
    show cg_p152 at cg_0 with dissolve
    hide cg_p151
    peng_speaking "你还记得，那天早上你看到的东西吗？在我房间抽屉里的那个。"
    mei_speaking "啊？记得啊。"
    mei "我越来越迷茫了，既不知道话题是怎么跳转到这的，也不知道她为什么要跳转。"
    show cg_p153 at cg_0 with dissolve
    hide cg_p152
    peng_speaking "那个，那个是……你以前寄给我的信。"
    mei_speaking "……啊？"
    mei "连续三次疑问让我突然意识到，对某些事情，我和她的理解好像出了偏差。"
    hide cg_p153 with dissolve
    mei "那张被人撕成碎屑后又重新用胶带拼回去的纸，是我写的信？"
    show cg_p152 at cg_0 with dissolve
    peng_speaking "那时候，你突然离开，我真的好生气……你一个人去了大城市，比这里好上千百倍的地方，我真的好嫉妒……我撕了你的信，不想看到它们，也故意没有回复你。\n为什么只有你那么幸运？为什么你不跟我说就走了？……我那时，是这样想的。"
    mei_speaking "……"
    show cg_p153 at cg_0 with dissolve
    hide cg_p152
    peng_speaking "但是……但是我后来才知道，你是去看病了。你只是把好的消息告诉我，没有告诉我其他事情。但是，我……我因为那些可笑的想法，没有在你最痛苦的时候理解你……"
    peng_speaking "而且，知道这件事之后，我也不敢再去联系你。我妈有阿姨的联系方式，但我一次都没尝试过。我只是想着，等我离开这个地方，再去找你道歉……"
    peng_speaking "可是，没想到你……"
    peng_speaking "我做了这么多过分的事情，你根本，不应该喜欢我……"
    show cg_p154 at cg_0 with dissolve
    hide cg_p152
    peng_speaking "你现在，知道了吧……知道这些之后……你还会跟我说同样的话吗？"
    mei_speaking "……啊……"
    mei "我被巨大的信息量轰炸了大脑，一时间竟然说不出任何有意义的话。"
    hide cg_p154 with dissolve
    mei "说起来，之前听到她说“对我做的事”，以她的性格，我以为是指小时候那些抢被子抢零食的小事。\n……原来不是啊。"
    show cg_p155 at cg_0 with dissolve
    peng_speaking "你知道吗，暴风雨的那天，我不小心看到了，看到向夏在偷偷哭。\n我觉得，她应该也经历过很难过的事，才会让她平时装成那种性格。"
    mei_speaking "……向夏？"
    peng_speaking "我那么讨厌她，讨厌她那么自由，谁也不在乎。我嫉妒她，她有我没有的东西，就像……我小时候嫉妒你一样。"
    peng_speaking "可是，可是那都是因为我只看到表面……我其实连嫉妒的资格也没有。"
    show cg_p156 at cg_0 with dissolve
    hide cg_p155
    peng_speaking "我嫉妒不了你，也嫉妒不了她。你们都比我艰难多了，我……"
    show cg_p155 at cg_0 with dissolve
    hide cg_p156
    peng_speaking "我有着健康的身体，妈妈也对我很好，只要在村里生活就不会难过到哪里去。\n我所有的困难都是自己带来的，跟你们根本无法比较，我明明已经有的够多了，却还是不满足……"
    peng_speaking "我什么都比不过你，没有你厉害，没有你聪明，连受的苦都没你多。"
    show cg_p157 at cg_0 with Dissolve(1)
    hide cg_p155
    peng_speaking "我……连痛苦都这么平庸。"

    scene bg_black with dissolve
    mei_speaking "……"
    mei_speaking "你还真的是很会隐藏呀。"
    mei "我突兀地想起小时候的她说绝对不会在别人面前哭，又想到刚刚的“一辈子也不会告诉你”，只觉得无奈……又有些难过。"
    scene bg_meiliv with dissolve
    show meiimg eye_close shell at char_left with dissolve 
    mei_speaking "按理来说，我应该挺生气的吧，你这么久都……"
    show pengimg eye_still at char_right with dissolve
    peng_speaking "是啊，肯定是。我知道的。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "但是我现在只是觉得有些庆幸。因为，你没有生气……真是太好了。"
    hide pengimg
    show pengimg eye_care o at char_right
    peng_speaking "……啊？什么……"
    mei "在彭江丽震惊的眼神中，我顿了顿，尽量控制自己的气息，让它显得冷静，不要太过混乱。"
    hide meiimg
    show meiimg eye_still smile shell at char_left
    mei_speaking "应该是，我真的是非常喜欢你吧？"
    hide pengimg
    show pengimg eye_care at char_right
    peng_speaking "……"
    hide pengimg
    show pengimg eye_care o at char_right
    peng_speaking "为什么，就算听到那些，你也这么想吗？"
    hide meiimg
    show meiimg eye_still shell at char_left
    mei_speaking "就算你那么说……我以前也没有想过找别的办法联系你，不是一样的嘛。"
    hide pengimg
    show pengimg eye_angry o at char_right
    peng_speaking "{size=45}当然不一样！你是被我骗了，你什么都不知道！{/size}"
    mei_speaking "……"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "如果是我骗你，你会怎么想？"
    peng_speaking "那你肯定是有苦衷啊！"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "……所以……因为你会这么想我，我当然也会这么想你。\n你在乎我……我也是。"
    hide pengimg
    show pengimg eye_care o at char_right
    peng_speaking "……"
    hide pengimg
    show pengimg eye_still at char_right
    peng_speaking "那，但是，还是不一样……"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "为什么？"
    hide pengimg
    show pengimg eye_still o at char_right
    peng_speaking "我，我并没有……经历过你那些痛苦。"
    peng_speaking "所以我什么都没资格说。更不应该让你原谅。"
    mei_speaking "……可是那都过去了。"
    hide meiimg
    show meiimg shell at char_left
    mei "出乎意料的，我现在竟然感觉自己很平静，不知道是因为被震惊到麻木，还是终于说开的释然。\n或许，都有吧……"
    hide meiimg
    show meiimg eye_close o shell at char_left
    mei_speaking "如果你经历什么不好的事，你会希望我也经历一遍吗。"
    hide pengimg
    show pengimg eye_care o at char_right
    peng_speaking "我怎么可能会希望那种事？！"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "所以，我也是一样……现在，至少都过去了。"
    hide meiimg
    show meiimg shell at char_left
    hide pengimg
    show pengimg eye_still at char_right
    peng_speaking "不，不是的……我根本配不上你。"
    hide pengimg
    show pengimg eye_still o at char_right
    peng_speaking "你这么温柔，又这么努力，我骗了你你还为我着想，你真的不应该原谅我……"
    peng_speaking "我，我已经很幸运了，能够跟你再次见面，还跟你待了这么长的时间，做了这么多事情……"
    peng_speaking "我没有在假装什么，现在真的已经很满足了。你讨厌我也没关系，我只希望能帮到你，希望你可以顺顺利利的，不要那么难过……"
    peng_speaking "只要你高兴，我就会很高兴。你想让我做什么，我都可以。"
    scene bg_black with dissolve
    peng_speaking "我——"
    mei_speaking "嘶……"
    mei "没想到今天没听到叶成华的教训，倒是听了彭江丽不少的长篇大论……"
    show movie_side
    show bg_meiliv with dissolve
    mei_speaking "等等……你先等等。"
    peng_speaking "啊？……嗯。"
    mei "我用力地，深深地吸了一口气，然后缓缓吐出。"
    mei_speaking "能不能别总是擅自揣测别人的想法？"
    peng_speaking "……咦？"
    stop music fadeout 0.5
    mei "彭江丽完全呆住了，像是不敢相信自己听到的话。"
    mei_speaking "擅自觉得对方会生气，擅自觉得对方讨厌自己，擅自觉得我在意什么，不在意什么，啊啊，反正就是擅自想那么多！"
    peng_speaking "啊？"
    mei_speaking "自顾自地想那么多，又从来不说出真实的想法……我哪里猜得出来啊！！"
    peng_speaking "怎么，呜，怎么这样……好凶……"
    mei_speaking "……我也不想的，但是我发现有时候就是要这样你才会听啦。"
    mei_speaking "真是的，每次都自己地做完一切，连让人考虑一下的余地都没有，我根本不想一直受你单方面的照顾啊！"
    peng_speaking "呜……"
    mei_speaking "遇到问题就回避，觉得只要我没事就好，觉得我讨厌你也没关系，就这样把自己的内心关起来，有没有想过我其实也！\n……喜欢你啊。"
    mei "我又重复了一遍这句话，比我听到她对我说的次数还多得多。"
    mei_speaking "我也在乎你啊……"
    mei "凭着一股脑的勇气带来的气势完全消失，我用气声说完最后一句话，然后移开了视线。"
    mei "呵呵……就算是我，把这些话都说出来也还是很难为情。"
    mei "这么一想，会不会不要太过逼迫彭江丽比较好……"
    mei "……呢？"
    mei "我正想继续说点什么找补的时候，彭江丽猛的一下扑过来，紧紧抱住了我，阻断了我的所有思绪。"
    hide movie_side
    show q_p40 at cg_s with vpunchm
    $ renpy.music.play(music.peng_love_you, channel="music", loop=True, fadein=0.5)
    peng_speaking "{size=42}呜……\n呜哇哇哇哇哇！！！！{/size}"
    peng_speaking "哇啊啊啊对不起！我，我呜呜呜我又说谎了！对不起！"
    peng_speaking "我，我才不是无所谓呢！我最——喜欢你了，喜欢得不得了！绝对不想让你讨厌我！"
    peng_speaking "我呜呜呜对不起，我太贪心了！但是我就是，就是想要你高兴，想要你幸福，想要你喜欢我，还想要跟你一直一直在一起！永远在一起！！"
    peng_speaking "呜呜呜哇啊啊啊啊啊——"
    mei "彭江丽大声哭嚎着，她死死抱着我，用力到我的身体开始发疼，但我并没有任何反应，只是抱着她，同样紧紧地抱着她。"
    hide q_p40 with dissolve
    mei_speaking "好。"
    peng_speaking "呜，呜呜呜……呜呜，呜啊啊啊……"
    stop music fadeout 0.5
    return