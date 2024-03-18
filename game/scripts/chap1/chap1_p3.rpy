label chap1_p3:
    hide meiimg
    show meiimg shirt eye_wacky o at char_left
    mei_speaking "不，等等，我……送你回去吧？"
    hide meiimg
    show meiimg shirt at char_left
    hide pengimg
    show pengimg eye_care o at char_right
    peng_speaking "啊……你不，先吃饭吗？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "没关系的……我还没那么饿。"
    mei "我似乎隐约能感觉到向夏在一旁注视着我们，又或是觉得这拉扯的气氛令人难受，干脆猛地站起来，跟着彭江丽往外走。"
    mei_speaking "走吧！"
    hide meiimg with moveoutright
    hide pengimg with moveoutright
    
    scene bg_vil6 with fade
    show halfyellow
    $ renpy.music.play(music.peng_hanging_out, channel="music", loop=True, fadein=0.5)
    mei "这个季节的太阳还没有早早落山，此时此刻仍然有浅浅的日光落在树叶上、道路上、以及身旁的彭江丽身上。\n只是，刚才的冲动和勇气已经结束，我现在又不知道该怎么面对她了。"
    show pengimg eye_care o at char_right with dissolve
    peng_speaking "梅雨……你真的不饿吗？是不是我做得太难吃了？"
    hide meiimg
    show meiimg eye_shock o at char_left
    mei_speaking "啊？怎么会，我……"
    hide meiimg
    show meiimg eye_shock at char_left
    na "咕噜——"
    hide meiimg
    show meiimg eye_wacky at char_left
    mei "我急忙否认，下一刻却有响亮的叫声从我的肚子传出。{p}喂，这也太不给面子了……"
    hide meiimg
    show meiimg at char_left
    mei "实话说，之前和向夏折腾了那么久还没吃到饭，我的确是很饿……但是……"
    hide pengimg
    show pengimg eye_care at char_right
    peng_speaking "好吧，真的是因为太难吃啊……要不你说下，我下次改改？"
    hide meiimg
    show meiimg eye_wacky at char_left
    mei_speaking "没有，不是这样……"
    hide pengimg
    show pengimg eye_care smile at char_right
    peng_speaking "别担心，我不会在意的。我本来就不是很擅长做饭，就是，你不喜欢的话，我之后就……"
    hide meiimg
    show meiimg eye_wacky o at char_left
    mei_speaking "我说了不是！"
    mei_speaking "我只是想找机会跟你说话！"
    stop music
    hide meiimg
    show meiimg eye_shock at char_left
    hide pengimg
    show pengimg eye_care at char_right
    peng_speaking "……"
    mei_speaking "……"
    hide meiimg
    show meiimg eye_still at char_left
    hide pengimg
    show pengimg at char_right
    mei "糟糕，我怎么直接跟她这么说了……我飞快低下头，不敢抬头看她的表情。"
    hide meiimg
    show meiimg eye_still o at char_left
    mei_speaking "……呃，那个……"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "梅雨。"
    hide meiimg
    show meiimg at char_left
    mei_speaking "嗯？"
    hide pengimg
    show pengimg eye_care o at char_right
    $ renpy.music.play(music.peng_hanging_out, channel="music", loop=True, fadein=0.5)
    peng_speaking "啊，就是……你刚刚说的……是真的吗？"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "是，是啊……"
    mei "彭江丽的身上反射着淡淡的夕阳光晕，将她明亮的眼睛衬得愈发动人，我一时间看得愣在原地，竟然忘了说话。"
    hide pengimg
    show pengimg eye_care smile at char_right
    peng_speaking "谢谢你。"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "嗯……啊？"
    hide pengimg
    show pengimg smile at char_right
    peng_speaking "就是，我怕你会……嫌弃我。但是你没有，你真的很温柔……"
    hide meiimg
    show meiimg at char_left
    mei_speaking "不，我……"
    mei "我有些紧张，但并不像之前那样感到将要窒息的程度。也许，是因为看到了她温柔的表情……"
    mei "我从未从这样的角度看过她，因而，不知道为什么，被她看着，我竟然有些害羞。\n实在是太奇怪了……我顿了顿，努力不让自己的话语变得磕磕巴巴。"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "我怎么会那样想……"
    hide pengimg
    show pengimg laugh at char_right
    peng_speaking "不过，你这么饿还不吃我做的饭，不就是觉得难吃嘛。"
    mei_speaking "诶，那，那是……"
    hide meiimg
    show meiimg at char_left
    hide pengimg
    show pengimg eye_care laugh at char_right
    peng_speaking "那个……我开玩笑的。"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "没，我知道……\n嗯……今天，真的很谢谢你。"
    hide pengimg
    show pengimg smile at char_right
    peng_speaking "那个，没事啦……"
    mei "她连开玩笑都小心翼翼，我有些无奈，不过，总比一开始的气氛好多了。{p}说不定，真的能回到以前的关系呢……"

    scene bg_vil2 with pixellate
    show halfyellow
    show pengimg o at char_right with moveinright
    peng_speaking "所以，成华姐真的就让你和那个陌生人一起住吗？"
    show meiimg at char_left with moveinleft
    mei_speaking "嗯……不知道她怎么想的。"
    hide pengimg
    show pengimg eye_care o at char_right
    peng_speaking "嗯，这样的话……就是，要不，你住我家？"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "诶……？不用……"
    mei "有那么一瞬间，我的确有些心动这个提议。但，仔细想想的话，还是不合适，也只能拒绝了。"
    mei_speaking "我又不是只住两天，总不能一直打扰你……反正，房间有锁，跟她互不干涉，也无所谓。"
    hide pengimg
    show pengimg eye_care at char_right
    peng_speaking "这样啊，那，你觉得没关系就好……我没别的意思，就是有点担心，因为，也不知道那个人到底是来干嘛的。"
    hide meiimg
    show meiimg at char_left
    mei_speaking "我知道，不过，不影响我就没事。"
    hide pengimg
    show pengimg eye_care smile at char_right
    peng_speaking "嗯……也是。"
    mei "尽管这么说，她的表情仍然是有些纠结。\n要不，我之后还是去问一问向夏好了……"

    scene bg_vil5 with pixellate
    show halfblack
    mei "天色还没有完全昏暗，但已经能够清晰看到空旷天际线附近的星星了。\n光芒的颜色由温暖变得清冷，温度也自然下降许多，我不由得拢了拢外套。"
    show pengimg smile at char_right with dissolve
    peng_speaking "那我就回家啦。\n啊……谢谢你，送我回来。"
    show meiimg at char_left with dissolve
    mei_speaking "嗯。"
    peng_speaking "别着凉了，你快回去吧，还有事可以之后找我。或，或者，我们可以打电话。"
    mei "我确实想说些什么，可又觉得似乎无话可说。况且，我也的确有些冷了。"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "那，之后见。"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "……诶？"
    mei_speaking "嗯……之后，我找你。"
    hide pengimg
    show pengimg eye_squint laugh at char_right
    peng_speaking "啊，好……！\n什么时候都可以！"
    scene bg_vil5 with pixellate
    show halfblack
    mei "我朝她挥挥手，转过头之前看到的最后一个画面，是彭江丽怔愣后在脸上炸开的笑容。"
    stop music fadeout 0.5
    return