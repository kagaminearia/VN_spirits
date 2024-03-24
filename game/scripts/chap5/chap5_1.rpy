label chap5_1:
    scene bg_meiroom
    show yeimg smile at char_right with moveinright
    ye_speaking "对了，那你现在打算回去吗？我这边没问题，随时都能送你回去。"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "啊，不……"
    mei "咦，我……{p}指关节被捏到有些疼痛，我才后知后觉反应过来，在叶成华问我的时候，我下意识就拒绝了她。"
    mei "为什么……{p}我不是觉得，在这里也没有用的吗，为什么还拒绝了回去的建议……"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "不……不知道。"
    ye_speaking "没关系，我就问问啊，就是看你好像最近也没什么兴趣。你别紧张，也别想太多。"
    ye_speaking "暂时没想法呢也没啥，咱们这又不急。像我之前说的，你什么时候想回去了，想做啥，找我就行。"
    mei "不知道为什么，但，我还……不想回去。\n这一次，我清晰地听到了自己心底的声音。"
    mei "原来，是这样啊……"
    mei "我一直在逃避，在迷茫中不知所措，在恐惧任何尝试，找不到任何方向。{p}但即使如此，却还是贪婪地希望……希望有人能救我。"
    
    scene bg_meiroom with pixellate
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "不想。"
    show yeimg laugh at char_right with moveinright
    ye_speaking "嗯？你刚说什么了吗？我没听清。"
    mei "叶成华本来已经站起来，就要离开饭桌，听到我的声音之后，又停住了动作。"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "我暂时应该，不回去。"
    ye_speaking "……"
    mei "我是不是说错话了……\n正当我思考要不要再说些什么的时候，她好像终于反应过来似的笑了。"
    hide yeimg
    show yeimg smile at char_right 
    ye_speaking "嗯，好啊。\n你能这么说，我很高兴。"
    mei_speaking "……嗯？"
    ye_speaking "没什么。总之，之后你就这样，想做什么去做就好啦。"
    ye_speaking "今天就是来找你吃个饭，你要没别的事，我先回去了啊。给你的电话记得要用，有事打我电话啊。"
    mei_speaking "嗯，好。"
    scene bg_meiroom with dissolve:
        blur 20
    mei "想做什么就去做吗……\n的确，就算妄想着，就算贪心着，自己不动的话，别人做再多也没用……我当然明白这一点。"
    mei "但是，我还是不知道，自己想做什么，能做什么啊……"
    return
