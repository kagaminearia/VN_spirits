label chap7_p1:
    scene bg_vil6 with fade
    mei_speaking "……"
    $ renpy.music.play(music.peng_poor_little_girl, channel="music", loop=True, fadein=0.5)
    mei "这样真的合适吗……我的脚步在转弯前停下来，就这么停在路口。"
    mei "往前再走一段，就是彭江丽家。\n短短两天时间，我第二次想着到彭江丽家里找她，心情却完全不同了……"
    mei "虽然也有担心，可更多的，却是恐惧。"
    mei "我应该再去找她吗？会不会在这时候冷处理才是更好的办法？我是不是不应该……\n不，不对……"
    mei "至少，我要把我自己的想法原原本本告诉她才行，就算……被她讨厌。"
    mei "没错，我不应该说些冠冕堂皇的大话，而应该承认我之前其实是不敢面对她的事实……"

    scene bg_vil5 with fade
    show pengimg shirt o at char_right with moveinright
    peng_speaking "谁——"
    hide pengimg
    show pengimg shirt eye_still at char_right 
    peng_speaking "啊。"
    mei "彭江丽的音调还没上扬就很快压下了，她下意识地把衣服的领口往上扯，却挡不住表情，也没有继续说话。"
    mei "我硬着头皮，扯出一个不算好看的笑。"
    show meiimg eye_still o shell at char_left with dissolve
    mei_speaking "早，早上好……"
    hide pengimg
    show pengimg shirt eye_still o at char_right 
    peng_speaking "……早上好。怎么了，有什么事吗？我之前好像说过，不用帮我讲题目了吧？"
    mei_speaking "我知道，是，别的事……那，你现在有时间吗？"
    hide pengimg
    show pengimg shirt eye_still at char_right 
    peng_speaking "有，有的。"
    mei_speaking "那……"
    hide pengimg
    show pengimg shirt eye_squint smile at char_right 
    peng_speaking "有什么事情，可以在这里说吗？"
    hide meiimg
    show meiimg eye_still shell at char_left 
    mei_speaking "……"
    mei "虽然她还是和平常一样笑着，我却感到了从未有过的压力。"
    mei "怎么办，该怎么开口……"
    hide pengimg
    show pengimg shirt eye_care at char_right 
    peng_speaking "……"
    hide pengimg
    show pengimg shirt eye_care smile at char_right 
    peng_speaking "对不起，我，今天，可能还是有点忙。\n下次，再说吧。"
    hide pengimg with moveoutright
    na "砰！"
    mei "不等我回话，她就重重地，匆匆地把门再次关上，只留我站在门口不知所措。"
    hide meiimg with dissolve
    show halfblack with dissolve
    mei "以前……\n我站在门口，蓦地想起小时候的事。"
    mei "那时候因为我妈很忙，我总是到她家来住。\n那时候，我们从来不会吵架……"
    mei "现在，为什么会变成这样……"
    mei "或者，其实是她以前一直在迁就我，只是现在，忍不下去了？"
    mei "该怎么办……"

    scene bg_vil5 with pixellate
    mei "太阳逐渐升高，随着时间一起流逝。"
    mei "我换了个位置和姿势，坐在不远处的树下，能隐约看到那栋熟悉的房子的门口。\n同时，从那里出来的人，也能很容易就看到坐着的我。"
    mei_speaking "哼……"
    mei "没想到我还挺卑鄙的……我冲着自己嗤笑，但并不打算改变想法。"
    mei "阳光变强，即使头顶有堆叠的叶片也落下不少热浪。我眯起眼睛，百无聊赖地拨弄着刘海上的发夹。"
    mei "我以前从来不在身上加饰品，这些多余的东西只是让很多事变得麻烦，也没有人会朝它们留下眼神。"
    mei "但这是她送我的……她亲自挑选的。\n她会注意到我戴上发夹，会夸它适合我。"
    mei "我很高兴身上留着她送的东西。但……\n我现在更想见到她。"

    scene bg_vil5 with Fade(0.5,0.5,1,color="#fff"):
        blur 25
    peng_speaking "……为什么还待在这里？"
    mei_speaking "嗯……啊？"
    mei "我有些迷迷糊糊地睁开眼，视线里，有些晃眼的光线被熟悉的身影挡住。\n我仰起头，看着彭江丽定定地俯视坐着的我。"
    stop music fadeout 0.5
    
    scene bg_vil5 with dissolve
    show pengimg shirt at char_right with dissolve
    peng_speaking "不回家吗？"
    $ renpy.sound.play(sound.heartbeat_1, channel="sound", loop=False)
    mei "她没什么表情，语气也平淡无波，我却莫名觉得心脏被揪了一下。"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "现在这么晒，你坐在这里，万一……万一又晕过去怎么办？"
    show meiimg o shell at char_left
    mei_speaking "不会的。我没那么容易晕倒。"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "那你……"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "……"
    hide pengimg
    show pengimg shirt at char_right
    peng_speaking "……{p}先站起来吧？"
    hide meiimg
    show meiimg eye_close shell at char_left
    mei "她的嘴唇微微动了，但最终也没说太多，只是轻轻地抓住我，拉着我站起来。"
    show meiimg eye_close shell at char_mid with moveinleft
    mei "我不知道自己坐了多久，站起来时腿有些麻，险些倒在彭江丽身上，还好我控制住了自己。"
    hide pengimg
    show pengimg shirt eye_still at char_right
    hide meiimg
    show meiimg shell at char_mid
    peng_speaking "对不起，我不该让你等在外面的，是我，刚刚有些草率了。"
    hide pengimg
    $ renpy.music.play(music.peng_hanging_out, channel="music", loop=True, fadein=0.5)
    show pengimg shirt o at char_right
    peng_speaking "现在要回家吗？或者要干什么，我陪你吧？"
    mei "短暂的沉默之后，彭江丽还是笑着看向我。\n我知道的，她就是这样……"
    hide meiimg
    show meiimg shell eye_still o at char_mid
    mei_speaking "我是故意坐在这里的。"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "啊？怎，怎么了……"
    hide meiimg
    show meiimg shell o at char_mid
    mei_speaking "因为我想着，我在烈日下坐着，你看到的话，说不定会心疼的，然后，你就愿意出来跟我说话了。"
    hide pengimg
    show pengimg shirt eye_care at char_right
    peng_speaking "……咦……"
    hide meiimg
    show meiimg shell eye_still o at char_mid
    mei_speaking "我是不是很过分？总是让你迁就……"
    peng_speaking "不，不是……是我……"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "我以为，你再也不会理我了。我以为你肯定很讨厌我。"
    peng_speaking "都怪我不好，我就应该一开始听你说话的，这样你也不用这样才……"
    hide meiimg
    show meiimg shell eye_still at char_mid
    mei_speaking "……"
    mei "她完全不生气吗，为什么……"
    hide meiimg
    show meiimg shell eye_still o at char_mid
    mei_speaking "那，现在可以进屋聊吗？"
    hide pengimg
    show pengimg shirt eye_care smile at char_right
    peng_speaking "当然可以！不过……家里味道可能有点大，你不介意吗？"
    hide meiimg
    show meiimg shell eye_close o at char_mid
    mei_speaking "没关系的。"
    mei "我忙不迭地点头，自然也不在意她说的那些味道。"

    scene bg_pengliv with fade
    mei "不过，虽然这么说……但我在进门后就下意识抽了抽鼻子，也瞬间明白了彭江丽的意思。"
    mei "客厅潮湿的气息中泛着鱼腥味，令我想起那一波一波涌起的海浪。直到走进卧室并且关上门，这味道才消散一些。"
    
    scene bg_pengroom with pixellate
    show pengimg shirt eye_still at char_right with moveinright
    peng_speaking "对不起，很难闻吧，我没来得及完全清理掉……"
    show meiimg shell at char_left with moveinleft
    mei_speaking "啊，没，没事……"
    mei "我更加拘谨了身体，有些不太自然地保持着正坐的姿势。"
    hide pengimg
    show pengimg shirt eye_still smile at char_right
    peng_speaking "最近禁渔期取消了，家里每天都要处理抓来的鱼，就会有这种味道。所以，嗯……你快点说完想说的话，就可以不用闻了。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "诶，就是……"
    mei "我和彭江丽并排坐在床上，在这个位置，我们比之前在门口靠得还要近，在这个距离，我甚至有些不敢看她的脸。"
    mei "不过，都好不容易讲上话了……"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "我之前，是想跟你说话，那个……"
    hide pengimg
    show pengimg shirt eye_still o at char_right
    peng_speaking "为什么？我之前……那样凶你，你不应该根本就不想见到我吗？"
    hide pengimg
    show pengimg shirt eye_care smile at char_right
    peng_speaking "啊，我知道了，你是等着要骂我吗？那……快点吧。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "我没有，而且，我刚刚也利用了你。"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "那怎么能比，完全不一样啊……\n而且……"
    hide pengimg
    show pengimg shirt eye_care smile at char_right
    peng_speaking "其实，你可以不用强迫自己安慰我的。不喜欢的话，直接说就可以了。"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "什么？不是这样的。"
    $ renpy.music.set_pause(True, channel="music")
    hide pengimg
    show pengimg shirt eye_still at char_right
    peng_speaking "……"
    hide meiimg
    show meiimg eye_still shell at char_left
    mei_speaking "……"
    hide meiimg
    $ renpy.music.set_pause(False, channel="music")
    show meiimg eye_still o shell at char_left
    mei_speaking "昨天，我是想着，能够早点见到你，看看你在上学的地方，也不错。"
    hide meiimg
    show meiimg eye_close o shell at char_left
    mei_speaking "但我没想到会发生后来的事……但是，还是对不起。"
    hide pengimg
    show pengimg shirt eye_close at char_right
    peng_speaking "……{size=30}别说了{/size}……"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "所以，我今天来，就是想正式跟你道歉。"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "那不是我的本意，对不起，我真的……不想看到你难过。"
    hide meiimg
    show meiimg eye_still shell at char_left
    mei "终于把这些话说了……我在内心松了口气。\n可……"
    hide pengimg
    show pengimg shirt eye_still at char_right
    mei "彭江丽好像完全没有放松的意思，她只是移开视线，沉默地坐着。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "……彭江丽？"
    peng_speaking "……嗯。"
    hide pengimg
    show pengimg shirt eye_still o at char_right
    peng_speaking "我只是觉得……你不应该讨厌我才对吗？为什么还要对我道歉。"
    mei_speaking "我，我怎么会讨厌你？你这么好……"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "不是的！我——"
    mei "她的声音忽然变大，却戛然而止，像突然被扎破的气球漏了气。"
    hide pengimg
    show pengimg shirt eye_still at char_right
    peng_speaking "我知道的，你也不用为了考虑我的感受做伪装什么的。"
    hide pengimg
    show pengimg shirt eye_still smile at char_right
    peng_speaking "我，应该挺让人看不起的吧。自己就是村里长大的，还觉得村子给自己丢脸。"
    peng_speaking "别人看不起，所以自己也跟着看不起了，还装得很不在乎。"
    peng_speaking "明明是自己又土又穷，没见过世面，喜欢装样子。"
    hide pengimg
    show pengimg shirt eye_care laugh at char_right
    peng_speaking "明明是自己没有什么能力，还总是做白日梦，想要得不到的东西，而且我还总是……"
    hide meiimg
    show meiimg eye_shock o shell at char_left
    mei_speaking "不是啊，才没有！"
    mei "我原本想听她说完话，但她越说越离谱，我还是忍不住直接打断了她。"
    hide pengimg
    show pengimg shirt eye_angry o at char_right
    peng_speaking "本来就是！你直说也没关系的！我知道我根本就——"
    mei_speaking "都说了不是啊！你是我家人以外最重要的人了！"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "——什么……？"
    hide meiimg
    show meiimg eye_shock shell at char_left
    mei_speaking "……啊……"
    mei "糟糕，我又激动了……这句话本来不想这么直接说的……\n这样会不会让她觉得很有压力……"
    hide meiimg
    show meiimg eye_still shell at char_left
    mei "不，我说过要让她知道自己的想法，就这样吧……反正已经说了。"
    hide meiimg
    show meiimg eye_still o shell at char_left
    mei_speaking "所以说，就是，这样……"
    hide pengimg
    show pengimg shirt eye_care at char_right
    peng_speaking "……"
    hide pengimg
    show pengimg shirt eye_care o at char_right
    peng_speaking "真的吗？你不觉得跟我做朋友丢脸吗？不觉得我太麻烦你吗？不讨厌我吗？"
    mei_speaking "是真的，从来没觉得过，不讨厌你。"
    hide pengimg
    show pengimg shirt eye_care smile at char_right
    peng_speaking "……你，真的好笨。"
    hide meiimg
    show meiimg eye_still smile shell at char_left
    mei_speaking "是吗？那就是吧。"
    mei "见到她终于露出笑容，我也终于缓缓呼出一口气。"
    mei "一直紧绷的心脏缓和下来，我才惊讶于刚刚似乎并没有感到疼痛。"
    mei "也许，虽然紧张，但对彭江丽的担心还是占了上风吧……"
    mei "现在她没事，这样就好……"
    stop music fadeout 0.5

    return