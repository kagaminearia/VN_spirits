label chap1_p2:
    show pengimg o at char_right with moveinright
    $ renpy.music.play(music.peng_hanging_out, channel="music", loop=True, fadein=0.5)
    peng_speaking "怎么了？说起来，你要买些什么啊，要我帮你看看吗？"
    show meiimg at char_left with moveinleft
    mei_speaking "嗯……叶成华那个房子缺东西，都得买一些。{p}呃，不过，我没怎么自己买过，所以，不太清楚……"
    mei "我的声音越说越小，刚刚升起的勇气也不由得逐渐消散了。毕竟我这样没有生活经验，实在容易给别人添麻烦。"
    hide pengimg 
    show pengimg smile at char_right 
    peng_speaking "没事，我不就是过来跟你一起看的吗，我自己现在也没什么要买的，跟你一起刚刚好。"
    hide meiimg 
    show meiimg eye_still smile at char_left
    mei_speaking "好啊。"
    mei "我有些如释重负地笑了笑，跟在彭江丽的身后。{p}她对这里如数家珍，几乎在最快时间就列出了所有我可能需要的东西。"
    
    scene bg_store2 with pixellate
    peng_speaking "这个也是……啊。"
    mei_speaking "……啊。"
    mei "流畅的动作突然变得卡顿。"
    show q_p10 at cg_s with dissolve
    mei "在货架间挑选的时候，她的手指偶然和我的对上。靠近，然后触碰到。"
    hide q_p10 with dissolve
    mei "然后，两只手都不约而同地瞬间后撤。然后她愣住，手指就那样悬在半空。"

    show meiimg at char_left with dissolve
    mei_speaking "……"
    show pengimg at char_right with dissolve
    peng_speaking "……"
    mei "我们面面相觑，彼此都看到对方眼神中的惊讶。{p}一瞬间，我无法抑制自己的联想——现在连这样简单的接触也变成如此不熟悉的事。"
    mei "不过……这也正常。不如说，是我不该想这么多才对。"

    hide meiimg with dissolve
    hide pengimg with dissolve
    mei "在我还呆站在原地的时候，彭江丽已经重新在货架上翻找起来，而后拿起两个瓶子给我看。"
    show q_p20 at cg_s with dissolve
    peng_speaking "啊……！这个，洗发水你喜欢哪种？"
    mei_speaking "不知道，我都没用过。\n你帮我选行吗？会不会，太麻烦了。"
    mei "我眨了眨眼，重新聚集起注意力。{p}看得出来，彭江丽在活跃气氛。于是我也想极力配合彭江丽，但语速也因为思绪卡壳变得有些凝滞。"
    mei "好在，她似乎并不在意我的反应，仍然“敬业”地帮我挑选。"

    hide q_p20 with pixellate
    show pengimg smile at char_right with dissolve
    peng_speaking "当然不麻烦了，只要你别嫌弃我选得不好。"
    show meiimg o at char_left with dissolve
    mei_speaking "不，怎么会。"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "就是，我也不知道你现在的习惯……你头发容易翘的话，这几个都可以试试。{p}唔，这个比较好，不过会贵很多。"
    mei_speaking "那，就这个吧，价格都无所谓。"
    hide pengimg
    show pengimg at char_right
    peng_speaking "……那，那好，走吧。"
    hide meiimg
    show meiimg at char_left
    mei_speaking "啊……嗯。"
    mei "为什么，总觉得气氛似乎又冷下来了……是我说错什么了吗……？\n我是想着积极支持彭江丽做的选择，但……做得不对吗？"
    mei "不过，也许是我又想多了也不一定，还是先不要乱想了吧……"

    scene bg_vil5 with pixellate
    show pengimg smile at char_right with dissolve
    peng_speaking "那我今天就回家啦，你要是有什么事，随时找我哦。"
    show meiimg o at char_left with dissolve
    mei_speaking "诶，好。"
    hide pengimg
    show pengimg eye_squint laugh at char_right
    peng_speaking "拜拜！"
    hide meiimg
    show meiimg smile at char_left
    hide pengimg with moveoutright
    mei_speaking "嗯。"
    hide meiimg
    show meiimg eye_close at char_left
    mei "我看着她离开的背影，这才意识到，她的笑容令我的心绪变得轻松不少。{p}也许……她没有像我想的那样讨厌我。那就……太好了。"
    window hide
    pause
    stop music fadeout 1.0
    window auto
