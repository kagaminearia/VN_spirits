label prologue_p1:
    mei "其实我并没有不想和彭江丽见面。但叶成华说出那句话时我的下意识反应确实是抗拒……这也是没办法的事情。"
    mei "一起经过的时间不是假的，即使记忆模糊，现在我也能回想起那种朦胧的快乐。{p}但……我们分开的时间也太久了，久到我几乎忘了她是什么样子。"
    mei "更何况，当时我一走了之，最后也没有成功跟她说一声，现在再出现，她应该会很生气吧……"
    mei "反正晚上也要一起吃饭，总要面对的，就当事情提前了吧……{p}我慢吞吞地下楼，找到电话和旁边写着号码的便签条。"
    $ renpy.sound.play(sound.ringtone, channel="sound", loop=True, fadein=0.5)
    na "嘟，嘟，嘟……"
    stop sound
    $ renpy.sound.play(sound.phone_pick_up, channel="sound")
    pause
    peng_speaking "你好？哪位？"
    show meiimg shirt o at char_mid with dissolve
    mei_speaking "……\n我是梅雨。"
    peng_speaking "……"
    show meiimg shirt o at char_mid with hpunch
    peng_speaking "梅雨？！\n最，最近还好吗？怎么会想到打电话给我……"
    hide meiimg
    show meiimg shirt eye_still smile at char_mid 
    mei "短暂的沉默后，声音从听筒里传来，有些惊讶，但也带着令人安心的熟悉感，令我的嘴角不自觉从绷紧的状态放下一些。"
    $ renpy.music.play(music.summer_wind, channel="music", loop=True, fadein=0.5)
    mei_speaking "嗯，是啊……那个，是叶成华硬拉着我回来的。她说这里更适合我，可以待一阵子，然后……嗯……"
    mei "我没能想到合适的词——毕竟，像我这样的人，还有什么好……"
    peng_speaking "……噢对！我把这事都给忘了，成华姐之前跟我提过来着，今晚要一起吃饭的嘛。\n……啊，你现在是不是特别无聊？要不我去找你玩吧？"
    hide meiimg
    show meiimg shirt o at char_mid
    mei_speaking "好，你知道是哪里么？"
    peng_speaking "当然啦，我一直在这里住哎。"
    mei_speaking "对，对哦……嗯……那我，在这等你？"
    peng_speaking "没问题。"
    hide meiimg
    show meiimg shirt eye_close o at char_mid
    mei "呼……我挂下电话，长长地喘出一口气，这才发现桌子上的小纸条已经被我攥得糊成一团。"

    scene cg_p10 with slideright
    na "……"
    show cg_p10 at cg_0 with irisout
    peng_speaking "……"
    show cg_p11 at cg_0
    peng_speaking "嗨！"
    mei_speaking "……嗨……啊，好久不见……"
    mei "我打开门，和门口的人忽然四目相对。彭江丽愣了愣，随后很快露出温柔的笑容。{p}我没想过这份冲击是如此直接，十分生涩地接上打招呼的话语。"

    scene bg_vil6 with pixellate
    show pengimg smile at char_right with moveinright 
    peng_speaking "真的好久不见了……"
    show meiimg shirt eye_still smile at char_left with moveinleft 
    mei_speaking "是啊……有多少年了？"
    hide pengimg
    show pengimg laugh at char_right
    peng_speaking "嗯，好像是快八年了吧，没想到，没想到……\n对了，你回来有多长时间了？怎么突然想着回来？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "是今天刚到……"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "感觉会不会不习惯？"
    mei_speaking "嗯，现在，还好……"
    hide pengimg
    show pengimg at char_right
    peng_speaking "嗯，那就好。"
    hide pengimg
    show pengimg eye_still at char_right
    hide meiimg
    show meiimg shirt at char_left
    peng_speaking "……"
    mei "我们一边走路一边寒暄，来回都在讲关于我回镇上的客气话，热情的笑容在断断续续的节奏中逐渐变得有些无奈。"
    mei "我终于明白，现实中的重逢并不总是像小说里那样充满美好或是戏剧性，也没有自然而然的激烈火花。"
    mei "对于我和彭江丽，这数年的间隔足以将我们之间的所有故事抹平。\n没有什么爱与恨，甜或苦，什么都没有。"
    mei "但不约而同地保持着这时表面的欣喜，或许也是我们之间的默契。{p}不过……我这应该算是，在自我安慰吧……"
    
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "对了，叶成华没跟你说过吗？"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "说什么？她没说什么啊。嗯，成华姐只是说……她说你身体不舒服，回来休息一段时间，约我今晚吃饭，没说别的。"
    hide meiimg
    show meiimg shirt eye_still o at char_left
    mei_speaking "哦……"
    mei "这样，的确也不奇怪……我一直以为叶成华只是粗暴地把我拎回来而已，但她也许比我考虑得更多，包括一些不太能注意到的细节……"
    mei "不过，至少身体的大概状况她应该会说，也许是怕出事吧……既然是彭江丽，没什么不能说的，尽管有些尴尬……"
    mei "只要不说那些最丢人的事就好……"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "其实就是……叶成华拉我回来的。{p}她是说，觉得我的身体适合在这里休养一段时间，吧……"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "噢，对哦，那个……那你的身体真的是……？"
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    mei "谈到这方面，她的声音骤然放低不少，带着明显的小心翼翼。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……我也不清楚，不过应该没事。"
    hide pengimg
    show pengimg eye_still o at char_right
    peng_speaking "这，这样啊……"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "嗯……"
    hide pengimg
    show pengimg eye_still at char_right
    mei_speaking "……"
    peng_speaking "……"
    mei "一时间，本就开始降温的气氛更加僵硬，我也不由得开始唾弃自己。{p}为什么非要多嘴呢？明明和彭江丽好久不见，为什么非得说些让人不高兴的话？"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "那要回去吗……？去海边的话，之后去也一样的，你现在有没有不舒服？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "我没事啦。"
    hide pengimg
    show pengimg smile at char_right
    peng_speaking "好，那我们再走慢点吧。如果不舒服的话，什么时候回去都可以。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "……嗯。我知道。"
    peng_speaking "……好。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "……"
    mei "我的语气不可控地变得生硬，阻断了重新开启的话头。\n不该是这样的……"
    mei "只是，那样小心翼翼的语气，从她的嘴里说出来……实在令我难以忍受，不自觉就……"
