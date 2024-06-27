label pNE:
    show bg_black with dissolve
    mei "但是……"
    mei "……果然……我还是没有勇气直接说出口……"
    hide bg_black with dissolve
    hide pengimg
    show pengimg eye_care behind halfyellow at char_right
    hide meiimg
    show meiimg shell behind halfyellow at char_left
    mei_speaking "没有的事，我没这么觉得。刚刚我只是刚睡醒，没反应过来。"
    hide meiimg
    show meiimg eye_close o shell behind halfyellow at char_left
    mei_speaking "嗯，这几天没怎么睡好，所以可能显得精力不够……"
    mei "我尽力让自己的语气显得平淡，好像真的什么都没有发生。"
    hide pengimg
    show pengimg eye_care o behind halfyellow at char_right
    peng_speaking "啊？怎么会……真的不是因为我麻烦到你了吗？"
    hide meiimg
    show meiimg o shell behind halfyellow at char_left
    mei_speaking "真的没有——\n不用担心的，我没事。"
    hide pengimg
    show pengimg behind halfyellow at char_right
    peng_speaking "那好吧……那，今天就这样吧？我先送你回家。"
    hide meiimg
    show meiimg smile shell behind halfyellow at char_left
    mei_speaking "啊，嗯，等等，我自己回去就可以了，现在这么晚，你也不要在外面待太久比较好吧。"
    hide meiimg
    show meiimg shell behind halfyellow at char_left
    hide pengimg
    show pengimg o behind halfyellow at char_right
    peng_speaking "啊？可是……"
    hide pengimg
    show pengimg eye_squint smile behind halfyellow at char_right
    peng_speaking "好吧。那你路上要小心哦。"
    mei "不知道是想到什么，彭江丽的表情有些纠结，但还是点了点头。"
    hide meiimg
    show meiimg eye_close shell behind halfyellow at char_left
    mei_speaking "好。今天……谢谢你。"
    mei "我不敢看她的眼睛，只是尽量快速解决了对话。"

    scene bg_black with dissolve
    mei "后来我才意识到，那天说不定就是最好的坦白时机。"
    mei "第一次没能说出口，之后我再也不敢承认自己偷听到的对话，也不敢接受太多她的好意。"
    mei "不过，她仍然是我最好的朋友。\n……至少在我看来是这样。"

    scene bg_station1 with fade
    show pengimg shirt o at char_right with moveinright
    peng_speaking "你应该保存了我的号码对吧？"
    show meiimg shell at char_left with moveinleft
    mei_speaking "嗯，是啊。"
    hide pengimg
    show pengimg shirt eye_still o at char_right 
    peng_speaking "不会像之前那样吧，什么都不说……就走了。"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "不会的，现在，不就在跟你说嘛。"
    hide meiimg with dissolve
    hide pengimg with dissolve
    mei "我和彭江丽并排走着，行李箱在身后发出轮子摩擦地面的响声，喀拉喀拉。"
    mei "我当然知道自己不会一直待在立涧村，但没想到，离开的时候竟然会是这种心情。"
    mei "放松，高兴，还有……庆幸。高兴我还能和彭江丽保持联系，也庆幸自己不用跟她更加拉近距离。"
    mei "实在是……很卑鄙。"
    show meiimg o shell at char_left with dissolve
    mei_speaking "我在这等就好了，今天这么晒，你也要待在这里吗？"
    show pengimg shirt smile at char_right with dissolve
    peng_speaking "说好要送你的，当然是跟你一起等了，毕竟，之后就见不到你了啊。\n况且，现在这么早，就算晒也不热。"
    hide meiimg
    show meiimg shell at char_left 
    mei_speaking "……\n嗯，好。"
    hide meiimg
    show meiimg eye_close shell at char_left
    hide pengimg
    show pengimg shirt at char_right
    mei "我们并排坐在树下的长椅上，阳光从树叶的缝隙中侵入，带来淡淡的暖意。"
    mei "彭江丽和我都没有说话，她只是静静地看着前方，不知道在想些什么。"
    hide pengimg
    show pengimg shirt o at char_right
    peng_speaking "我们之后，还能联系吗？"
    hide meiimg
    show meiimg o shell at char_left
    mei_speaking "嗯？当然了，我们不是都交换过号码了吗。"
    hide pengimg
    show pengimg shirt smile at char_right
    peng_speaking "是啊，只是……好吧，我只是有点担心，担心我们跟之前一样。"
    hide meiimg
    show meiimg shell at char_left
    mei_speaking "不会的。"
    hide pengimg
    show pengimg shirt eye_still smile at char_right
    peng_speaking "嗯。"
    hide pengimg
    show pengimg shirt laugh at char_right
    peng_speaking "我会努力的，就算没有你给我补课，我也会好好学习的。\n之后，我要考到你在的城市去。"
    hide meiimg
    show meiimg eye_still shell at char_left
    mei_speaking "……"
    hide meiimg
    show meiimg smile shell at char_left
    mei_speaking "不管你的目标是什么，你肯定都能做到的。你真的非常优秀，只是需要时间和机会而已。"
    hide pengimg
    show pengimg shirt eye_squint smile at char_right
    peng_speaking "谢谢你。"
    hide meiimg
    show meiimg eye_close smile shell at char_left
    mei_speaking "嗯，你……要加油啊。"
    scene bg_black with dissolve
    mei "只是，直到最后，我也没有正面回答彭江丽的第二句话。"
    $ persistent.pNE = 1
    window hide
    scene bg_white with Dissolve(4)
    pause(0.5)
    show screen endings_screen(endings,"pNE") with Pixellate(3,25)
    pause
    return