label chap7_x2n:
    xiang_speaking "所以，我绕了一大个弯，就是想跟你说，那天我不是故意的，我只是……很怕会爆炸的火。怕得要死，哈哈。"
    mei_speaking "……我，知道。"
    $ renpy.music.play(music.xiang_rainy_talk, channel="music", loop=True, fadein=1.0)
    mei "向夏笑着结束了这段回忆，但我却笑不出来。"
    xiang_speaking "抱歉啦，很无聊是吧？"
    mei_speaking "不，没有……"
    mei "她说一句，我应一句，但我的话干巴巴的，语气也平淡到僵硬。"
    mei "客厅的顶灯在此刻亮得晃眼，仿佛能够把我的所有小动作照得无所遁形。因而我只是直直坐着，控制自己的视线对着前方，甚至不敢转头看她。"
    mei "我该作出怎样的回应……"

    xiang_speaking "好啦，我说完了，{size=30}有没有什么漏的……{/size}啊对了，你还有什么想问的吗？"
    mei_speaking "……没有。"
    xiang_speaking "……"
    xiang_speaking "那，现在也不早了，我回去睡觉咯？"
    mei_speaking "嗯。"
    mei_speaking "……晚安。"
    xiang_speaking "晚安~"
    mei_speaking "……"
    stop music fadeout 1.0

    mei "我直直地盯着她的背影，直到她转身消失在墙的后面。然后，我偏过头，看向饭桌旁边的另一把椅子。"
    mei_speaking "……呵……"
    $ renpy.music.play(music.xiang_be, channel="music", loop=True, fadein=0.5)
    mei "人都走了，现在看有什么用。\n我暗暗嘲笑自己的虚伪，在再次发出声音之前死死咬住嘴唇。"
    mei "总觉得，我似乎理解向夏那套理论了……我也许，不该顺从她，开启这个话题的。"
    mei "现在的我们，并不适合聊完这些……但，某种微妙的平衡已经被打破了。"
    mei "而重要的是，我并不想……不对，是并没有勇气把自己的事和盘托出。"
    mei "所以，尽管她说的是所谓的“要求”，但这完全不等价的结果已经让我亏欠她了。"
    mei "所以……我无法面对她。\n这样的关系，已经不能继续了。"
    stop music fadeout 0.5


    return