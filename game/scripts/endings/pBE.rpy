label pBE:
    show bg_black with dissolve
    mei "——不，还是，还是让她自己冷静一下吧……"
    mei "我蓦地止住了脚步，膝盖因这硬生生的动作而泛起疼痛。"
    hide bg_black with dissolve
    mei "可，这都比不上……看着她越来越远的背影，我内心无法抑制的恐惧和空虚。"
    mei_speaking "她会没事的吧……"
    mei "我自欺欺人地安慰自己，却再也不敢上前一步。"
    mei "希望，她会没事……"

    scene bg_meiroom with fade
    $ renpy.music.play(music.peng_be, channel="music", loop=True, fadein=0.5, relative_volume=1.5)
    mei "似乎我每次抱有什么期望的时候，总是会事与愿违。\n也许，这是对我自己付出不够，只会祈求的惩罚吧……"
    mei "总之，那天是我和彭江丽最后一次直接说话。"
    mei "在那之后，她总是拼尽全力想要避开我，即使我再次到她家门口，她也不会再出来，只有我和阿姨的尴尬会面。"
    mei "于是……我也不好再打扰她。"

    scene bg_meihome with fade
    mei "我终究不能永远留在这里，离开的日子也很快来临。"
    mei "其实，这还要感谢她……感谢她让我重新鼓起勇气，让我决定再次参加考试。"
    mei "只是现在……我连这句感谢也没有办法跟她说了。"

    scene bg_station1 with fade
    mei "天气不算太好，阴沉沉的云层压住了阳光。到处都湿漉漉的，行李箱的轮子嵌着黏巴的泥土，拉起来有些费力。车站的车晚点了，我只能在这等着。\n还真是，没一件顺心的事情啊……"
    mei "况且……算了，还是不要想那些有的没的了。"
    mei "无聊的等待总是显得格外漫长。等到车来，我把自己重重地扔进有些旧有些硬的座位，终于觉得双腿解放了些。"
    mei "要走了……直到我透过雾蒙蒙的车窗往外看，才体会到了真实感。\n没想到，我竟然真的，可以说是变了很多吧……"
    mei_speaking "……嗯？"
    mei "漫无目的地望着窗外时，我突然发现车站的门口出现了一个熟悉的影子。"
    mei "怎么会……"

    scene bg_station1 with fade
    mei "车已经关门，准备出发了，我不可能让它停下来，更不可能让自己的声音传出去。"
    mei "于是我只能用尽全力睁大双眼，额头贴着汽车的玻璃表面，死死地望着那个方向。"
    mei "那个身影……我看见她走出来，跑了两步。我看见她露出了一个许久不见的笑容。我看见她朝我摆了摆手。"
    mei "我看见她在说话，说得很慢，能够让我读出口型。"
    mei "我第一次这么做，是在电影院，不好打扰别人。第二次这么做，是现在，我已经听不见她的声音。"
    mei "我看见她在说……"
    stop music fadeout 1.0
    scene bg_black with dissolve
    peng_speaking "梅雨……谢谢。"
    $ persistent.pBE = 1
    window hide
    $ renpy.sound.play(sound.rain_after_peng_be, channel="nature", loop=False, fadein=1.0)
    scene bg_white with Dissolve(4)
    pause(0.5)
    show screen endings_screen(endings,"pBE") with Pixellate(3,25)
    pause
    stop nature fadeout 1.0
    return