label chap6_x3:
    scene bg_meiroom with Fade(0.5,0.5,0.5)
    mei "午觉醒来，疲惫似乎并未完全消去，以至于我的动作变得有些温吞。"
    mei "尽管已经冲过凉了，但……也许是心理作用，总觉得身上还留着黏黏糊糊的感觉。"
    mei "大概是上午跟那群鱼打交道耗费太多心神……想到最后那场乌龙，我有些无语地揪了揪自己的头发。\n还好，没有味道。"
    scene bg_meiliv with pixellate
    show meiimg shirt o at char_left with easeinleft
    mei_speaking "……你在干嘛？"
    mei "我拖着步伐到楼下，准备拿洗完的衣服的时候，正好看到向夏坐在沙发上，手里拿着我昨天穿着的，打算丢掉的毛衣外套。"
    show xiangimg o at char_right with moveinright
    $ renpy.music.play(music.xiang_handing_out, channel="music", loop=True, fadein=0.5)
    xiang_speaking "什么？哦，我之前不是跟你说了吗，帮你补一下这件衣服，保证跟之前一样哦！"
    hide meiimg 
    show meiimg shirt at char_left
    mei_speaking "……哦。"
    mei "她有说过吗？好像……从海边回来的时候是提到过，不过我当时太累了，根本没心思听她说话就胡乱答应一通……"
    mei "不过，让别人拿着我的衣服，总觉得，有些尴尬……"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "要是麻烦，就直接扔了吧。"
    hide xiangimg
    show xiangimg fist eye_squint o at char_right 
    xiang_speaking "啊，那怎么行！你不想穿了吗？可是会很浪费耶……"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei_speaking "……那……{size=30}随你吧。{/size}"
    mei "我懒得跟她为这种无聊的事争论，干脆也在沙发上坐下，视线忍不住朝她的手上瞥。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "怎么补？"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "你看这里，就用刺绣贴！我之前从超市买回来的，只要把开线的地方缝起来就行。"
    hide meiimg
    show meiimg shirt eye_shock o at char_left
    mei_speaking "啊？喔……"
    hide meiimg
    show meiimg shirt at char_left
    mei "一时间，我还以为自己偷看被发现了，差点发出难听的颤音。\n不过，好像她只是在跟我解释。"
    mei "是我想多了啊……\n不知道是出于什么心情，我无声叹了口气。"
    mei "嗯……{p}我挠了挠头，顺手把电视的遥控器打开，免得这空旷的客厅显得太过安静。"
    stop music fadeout 0.5
    $ renpy.sound.play(sound.tv_noise, channel="extra_1", loop=False, fadein=0.5, relative_volume=0.2)
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "你还会缝这个啊。"
    mei "其实，我以为她是会把衣服弄坏的那种类型……看来真是应了那句话，人不可貌相。"
    hide xiangimg
    show xiangimg fist laugh at char_right 
    xiang_speaking "是啊，厉害吧？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "呃……嗯。"
    stop extra_1 fadeout 0.5
    hide xiangimg
    show xiangimg fist o at char_right
    $ renpy.music.play(music.xiang_rainy_talk, channel="music", loop=True, fadein=0.5)
    xiang_speaking "对了，既然你来了刚好问问你，你想要哪个颜色的线，还有刺绣？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "啊？"
    hide xiangimg
    show xiangimg fist laugh at char_right 
    xiang_speaking "红色，黄色，蓝色，绿色，都有哦！"
    mei_speaking "……随便，都可以。"
    mei "实话说……我觉得都很丑。\n但她毕竟也是在帮我补衣服，还是不要说了……"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "那我自己选了，蓝色怎么样？"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "啊，要不就蓝色吧，刚好，很适合你，你的眼睛就是蓝色的嘛。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "欸……"
    mei "我下意识摸了摸自己的眼皮，在那底下就是我的眼珠。"
    show halfblack with dissolve
    $ renpy.music.set_pause(True, channel="music")
    mei "这话没什么特别的，但我的心跳却莫名地停了一拍。{p}真奇怪……"
    mei "似乎……是因为她注意到了，还特地点出来。"
    mei "不过，嗯，我干嘛要因为一句话想这么多……"
    $ renpy.music.set_pause(False, channel="music")
    hide halfblack with dissolve
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "哦，我得跟你打个预防针，其实我也好久没做过这活了，要是不好看你可别怪我啊，不过肯定能穿就是了。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "没事，本来你不缝就要扔的。"
    hide xiangimg
    show xiangimg fist eye_still o at char_right 
    xiang_speaking "啊？那我的技术也没有烂到跟要扔掉的衣服比吧——"
    hide xiangimg
    show xiangimg fist at char_right 
    mei_speaking "也没有……"
    mei "她怎么总是不太正经的样子……不过，虽然向夏夸张地哀嚎起来，手上也没闲着。"
    mei "她的手指灵活地绕起针线，把刺绣贴和毛衣的开线处对准。\n我一时看愣了，甚至忘记移开视线，而是光明正大地盯着她的指尖。"

    scene bg_meiliv with pixellate
    show xiangimg o at char_right with moveinright
    xiang_speaking "搞定！看看怎么样？"
    show meiimg shirt at char_left with moveinleft
    mei_speaking "……"
    mei "向夏放下针线，两只手一起抓起衣服，放在我的身上比较。"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "呃，看看……嗯……你觉得呢？"
    mei_speaking "嗯……"
    hide xiangimg
    show xiangimg fist eye_squint o at char_right
    xiang_speaking "哇，对不起，好丑啊！"
    hide meiimg
    show meiimg shirt eye_wacky smile at char_left
    mei_speaking "……噗。"
    hide meiimg
    show meiimg shirt at char_left
    hide xiangimg
    show xiangimg fist eye_squint at char_right
    mei "随着向夏几次语气的变化，我终于笑出声音，看向那件变得不伦不类的衣服。"
    mei "它原本的颜色很浅，但现在胸口却缝上一朵明亮的蓝色卡通花朵。\n而且，还是用大红色的线缝的。"
    hide meiimg
    show meiimg shirt smile at char_left
    mei_speaking "这，嗯，这是有点……"
    stop extra_1 fadeout 0.5
    stop music fadeout 0.5

    na "“唔嗯~”"
    hide meiimg
    show meiimg shirt eye_wacky o at char_left
    $ renpy.music.play(music.xiang_bath, channel="music", loop=True, fadein=0.5)
    mei_speaking "……哈？"
    mei "没说出口的话被别的声音打了岔，但那莫名奇妙的甜美声音明显不来自于旁边的人。"
    na "“啊啊……嗯，唔……”"
    hide meiimg
    show meiimg shirt eye_wacky at char_left
    mei_speaking "啥……"
    hide xiangimg
    show xiangimg fist eye_still smile at char_right
    xiang_speaking "哇哦。"
    mei "我还没从困惑中反应过来，听到向夏戏谑的语气，我疑惑地跟随她的视线转移。{p}然后……"
    scene cg_x61 at cg_0 with vpunchm
    mei_speaking "这，这什么啊……！"
    mei "电视上，两具赤身裸体的身体紧密相贴，时不时从音响中发出诡异的呻吟。\n原来刚刚的声音是这个……"
    mei "我惊得差点打翻水杯，而后手忙脚乱地抓起杯子旁的遥控器，关掉了电视。"
    show cg_x62 at cg_0 with dissolve
    mei "向夏落在身上的视线有如实质，明明是揶揄的，却让我觉得面上做烧。"
    mei_speaking "咳咳……"

    scene bg_meiliv with fade
    show xiangimg fist eye_still laugh at char_right with moveinright
    xiang_speaking "哎哟，安心啦，又没有不熟悉的人。"
    hide xiangimg
    show xiangimg fist eye_still o at char_right
    xiang_speaking "不过，这玩意是电视广告吗？怎么冒出来的。"
    show meiimg shirt eye_close o at char_left with moveinleft
    mei_speaking "我怎么知道……"
    hide meiimg 
    show meiimg shirt eye_still at char_left
    mei "我整理好心情，终于重新转过头，无语地看着从始至终都毫无反应的向夏。"
    mei "哦，不对，她其实有过反应：在我关机前，嗤笑了两声。"
    hide meiimg 
    show meiimg shirt o at char_left
    mei_speaking "……你不惊讶？"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    xiang_speaking "没有啊，我挺惊讶的。"
    mei_speaking "有吗……"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "对啊，超级惊讶哦。我以前只是听说过。说什么，呃，情到深处的人就会忍不住这么做？没想到是真的。"
    hide xiangimg
    show xiangimg fist eye_close smile at char_right
    xiang_speaking "人跟人居然可以有这么亲近的关系啊，感觉有点恶心。"
    hide meiimg 
    show meiimg shirt eye_wacky at char_left
    mei_speaking "惊讶的点错了吧……"
    hide xiangimg
    show xiangimg fist o at char_right
    xiang_speaking "咦，原来你不是惊讶这个吗？"
    hide meiimg 
    show meiimg shirt eye_close o at char_left
    mei_speaking "呃，嗯，不是，吧……"
    hide xiangimg
    show xiangimg fist at char_right
    xiang_speaking "什么啊，那你吓成那个样子。"
    hide meiimg 
    show meiimg shirt o at char_left
    mei_speaking "……哈哈，意外。"
    mei "我尬笑两声，模糊掉这个话题——虽然是我自己提起的……"
    mei "不过，多亏她的面不改色，让我也冷静下来。\n总觉得，跟她相比，我刚才的反应好挫……"
    stop music fadeout 0.5

    scene bg_meiliv with pixellate
    show meiimg shirt o at char_left with dissolve
    mei_speaking "咳咳，好吧……对了，这衣服……"
    show xiangimg fist at char_right with dissolve
    $ renpy.music.play(music.xiang_first_meet, channel="music", loop=True, fadein=0.5)
    xiang_speaking "哇——别提了，这个真的对不起，要不我……我给你再买一件外套吧。"
    mei "这人刚刚好像诡异地停顿了啊……\n擅自揣度完她的心情后，我在心里默默笑了一声。"
    mei "不过，还是别为难她了。"
    hide meiimg
    show meiimg shirt smile at char_left
    mei_speaking "不……我是说，谢谢，我会穿。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "啊？真的？那个，你也不用逼自己……"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "那也不是……"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "虽然，如果给你买新衣服我是有点心疼钱啦，但这是我应该做的！你买吧！"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "……怎么就成你应该的了？"
    xiang_speaking "都怪我没看好那些鱼啊！"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    mei "怎么她总是能找出理由，还总是看起来很有道理……不对，我不是想说这个。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "我是真的认为可以穿。"
    mei_speaking "总不能浪费吧……而且，缝得很好啊。"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "好吧，只要你能接受就行。"
    hide xiangimg
    show xiangimg fist eye_squint smile at char_right 
    xiang_speaking "都说了，我是有技术在的，以前我给好多人补过衣服的。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "原来你是，嗯，裁缝？"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "不是哦。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "……啥？"
    hide xiangimg
    show xiangimg eye_squint smile at char_right 
    xiang_speaking "都是兼职啦兼职，赚点外快。嘿嘿，这只是我众多技能的其中一种。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "不对，跑题了，这衣服的事算我还欠你一次，你觉得怎么补偿比较好？"
    mei_speaking "哦……嗯？不是都缝好了吗。"
    xiang_speaking "这么丑，完全跟之前的不一样，当然不算了。"
    hide meiimg
    show meiimg shirt eye_wacky smile at char_left
    mei_speaking "噗……"
    hide meiimg
    show meiimg shirt smile at char_left
    mei_speaking "不需要啊。"
    hide xiangimg
    show xiangimg fist at char_right 
    hide meiimg
    show meiimg shirt at char_left
    xiang_speaking "那可不行，我不喜欢欠人情。"
    mei "我丝毫没有头绪，向夏倒是一副苦思冥想的样子。\n好一会儿，不知道她想到什么，整个人忽然显得有些兴奋。"
    hide xiangimg
    stop music
    show xiangimg fist laugh at char_right
    xiang_speaking "我知道了……我带你去山上玩吧！"
    mei_speaking "哈？不要。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "想都没想就拒绝了啊……"
    hide meiimg
    show meiimg shirt eye_wakcy o at char_left
    mei_speaking "这是谁欠谁的啊？"
    hide xiangimg
    show xiangimg fist smile at char_right 
    $ renpy.music.play(music.xiang_first_meet, channel="music", loop=True)
    xiang_speaking "好吧，我开玩笑的。\n不过，感觉你对什么事都没有太多兴趣，还真是难想。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……"
    hide meiimg
    show meiimg shirt eye_close at char_left
    mei "某种程度上，还真的被她说中了。"
    xiang_speaking "哎呀我知道了。要不这样，只要不过分，我就答应你一个要求怎么样？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "都说了不用，我没要求。"
    hide xiangimg
    show xiangimg fist o at char_right 
    xiang_speaking "那就先放着呗，指不定什么时候就用上了，当然，得在我回去之前啊。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……哦。"
    stop music fadeout 0.5
    mei "她不经意的话让我突然意识到一件事，她不是会永远待在这里的，现在这样的情况并不会维持多久。"
    mei "那我呢？我还没有想好之后的事吗？我……"
    

    scene bg_meiliv with pixellate
    show yeimg smile at char_right with moveinright
    $ renpy.sound.play(sound.wind_bell, channel="sound", loop=True, relative_volume=0.3)
    ye_speaking "我回来喽——你们在这干啥呢？"
    show meiimg o flower at char_left with moveinleft
    mei_speaking "诶？"
    mei "这对话好像似曾相识……叶成华的声音打断了我的思绪。"
    mei "我看到她放下包，抬头望向我的时候扑哧一声笑了出来。"
    hide yeimg
    show yeimg laugh at char_right
    ye_speaking "你这衣服……挺有创意啊。"
    hide meiimg
    show meiimg flower at char_left 
    mei "能不能别再提这事了……我有些无奈地搓了搓胸口的刺绣，仿佛这样就能让它的颜色褪掉一些。"
    show xiangimg fist o at char_mid with moveinleft
    xiang_speaking "啊，这事怪我，对不起啊，把衣服弄坏了。"
    hide meiimg
    show meiimg o flower at char_left 
    mei_speaking "别，不是你……"
    hide yeimg
    show yeimg smile at char_right
    ye_speaking "好啦，你们的事情你们自己解决，不用跟我说。\n不过今天我倒是有事想找你们。"
    ye_speaking "——要吃烧烤吗？"
    mei "她刷的举起包里的一袋竹签。"
    mei_speaking "……哈？"
    stop sound fadeout 0.5
    return