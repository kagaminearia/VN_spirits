define test_text_wave = WaveShader(amp = 0, melt="both", melt_params=(20,5.0,0.1))
label prologue_1:
    scene bg_vil3 with pixellate 
    mei "阳光明媚，道路旁传来淡淡的植物香气，和只有灰尘味的房间完全不同。只是……我们之间的气氛并没有比那样冰冷的房间好多少。"
    mei "彭江丽仍然带着笑容，却似乎变得有些僵硬，只是把步伐放得很慢，时不时朝我瞥来不安的眼神。{p}她长高了许多，长发在身后扎起高昂的马尾，跟着她的动作一晃一晃。"
    mei "原来已经过去了这么久，她和我都长大了……我下意识揪着垂到胸前的发尾，此时此刻才有了一种实感：{p}我们……真的又再见了。"
    mei "只是……"
    show pengimg o at char_right with moveinright
    peng_speaking "……梅雨？"
    show meiimg shirt o at char_left with moveinleft
    stop music
    mei_speaking "……啊！怎，怎么了？"
    mei "我沉浸在混乱的思绪中，一时间竟然没有注意到彭江丽在叫我。"
    peng_speaking "那个，你真的还好吧？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "嗯……真的没事。"
    hide pengimg
    show pengimg at char_right
    peng_speaking "那就好……\n就是，我想跟你说个事情。噢，不是什么重要的事，你别这么看我啊。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "是，是吗……"
    mei "……是我现在的表情很吓人吗？\n还是她终于忍不住了？"
    mei "尽管说着什么“不是重要的事”，可她的语气和神情看起来都完全像是正经的气氛，实在难以不让我联想到不好的预感。"
    $ renpy.sound.play(sound.heartbeat_1, channel="sound", loop=True)
    mei "我似乎开始紧张了……我在害怕，害怕这时隔多年的关系并不似我想的那样……"
    hide pengimg
    show pengimg smile at char_right
    peng_speaking "就是，嗯……关于我跟你——"
    hide pengimg
    show pengimg smile at char_right
    $ renpy.sound.play(sound.heartbeat_2, channel="sound", loop=True)
    mei "不对，不行。\n不能紧张，绝对不能紧张……想点别的，想点别的，控制呼吸……"
    peng_speaking "其实我……"
    mei "……快啊！！想点别的！！别再紧张了！！"
    hide pengimg
    show pengimg o at char_right
    peng_speaking "你……"
    $ renpy.sound.play(sound.heartbeat_3, channel="sound", loop=True)
    mei "不行……这样下去，又要像之前一样了……又是，什么都……"
    hide pengimg
    hide meiimg
    peng_speaking "{wave}{color=4b4b4b}啊——{/wave}" 
    mei "不，不行了……我逐渐什么声音也听不见。\n周围的空气好像被不断压缩，把我压得越来越紧，呼吸变得十分困难。"
    show bg_vil3 with dissolve:
        function WaveShader(period = 1, amp=1.0, repeat='mirrored', double="both")
    mei "然后，眼前的景象也趋于模糊，摇摇晃晃。"
    show bg_vil3 with dissolve:
        function WaveShader(period = 3, amp=2.0, repeat='mirrored', double="both")
    mei "然后……"
    window hide
    show cg_p20 at cg_0, blink
    pause(2)
    scene bg_black with dissolve
    window show
    stop sound
    na "……"

    mei_speaking "……"
    scene bg_meiroom with pixellate
    $ renpy.music.play(music.prologue_ending, channel="music", loop=True, fadein=0.5)
    mei_speaking "……"
    show yeimg at char_right with moveinright
    ye_speaking "现在有什么感觉吗？饿不饿？"
    show meiimg shirt eye_still at char_left with easeinleft
    mei_speaking "不，没事……谢谢。"
    ye_speaking "行，那你……自己待一会？需要什么不？"
    mei_speaking "好。"
    mei "我刚醒来没多久，因而说话也是有气无力。好在叶成华真的没有继续说下去，只是点点头从床边站起身，揉了揉我的脑袋。"
    mei_speaking "……抱歉……给你添麻烦了。"
    hide yeimg
    show yeimg smile at char_right
    ye_speaking "说啥呢。这事你也别想太多，是我要把你带过来，还擅自帮你约了饭局。是我该给你道歉，不好意思啊。\n不过，彭江丽那边，我没说你的事，如果可以跟人家解释一下就好了哦。"
    mei_speaking "嗯……好。"
    hide meiimg
    show meiimg shirt eye_close at char_left
    mei "我的头更低了些，想道歉，却什么别的话也说不出。"
    hide yeimg
    show yeimg laugh at char_right
    ye_speaking "嗨，放轻松点，彭江丽又不会吃了你，没什么大不了的。我也不打扰你了，要是有事用楼下电话打给我就行。"
    hide yeimg with moveoutright

    scene bg_meiroom with fade
    mei "直到关门的声音彻底消失，我才抬起头，怔怔地看着陌生的房间。明亮的日光透过没遮盖严实的窗帘渗入屋内，却完全没有让我变暖。"
    mei "现在是早上七点，也就是说，我完全搞砸了昨天的晚饭，自顾自地完全睡到现在。{p}而且，我又……"
    mei "……{p}此时此刻，我甚至开始庆幸，至少现在不用直接面对彭江丽——当然，这也是我唯一还能庆幸的事。"
    mei "太糟糕了，绝对是最糟糕的重逢……"
    stop music fadeout 1.0
    return