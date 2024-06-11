label chap8_x3:
    scene bg_ground3 with fade
    stf "三，二，一——"
    $ renpy.sound.play(sound.shutter, channel="sound", loop=False)
    xiang_speaking "喔——"
    mei_speaking "……"
    mei "我们在超市外面并排站好，很快，两下白光闪过。对面的人从机器里抽出两张卡片，笑着把其中一张递给我们。"
    xiang_speaking "这个是什么啊，照片这么快就能看到吗？"
    stf "这是拍立得，拍完就能拿到照片。\n我们会用一张做宣传，另一张送给你们。"
    xiang_speaking "噢，这样啊，谢谢。"
    mei "工作人员对我们笑了笑，她走到广场，把手里的照片贴在宣传栏上。"
    xiang_speaking "这张也一起贴上去吧。"
    mei_speaking "啊？"
    xiang_speaking "你要吗？不然扔掉也行？"
    mei_speaking "……"

    scene bg_ground3 with fade
    $ renpy.music.play(music.xiang_rainy_talk, channel="music", loop=True, fadein=0.5)
    mei "墙上贴着许多照片，都是两人合照，不知道哪些是情侣，哪些是朋友。\n不过，这不重要……我看着看着，眼神就不自觉飘到一旁。"
    show xiangimg fist eye_still o at char_right with moveinright
    xiang_speaking "怎么了，你不想贴另外一张吗？"
    show meiimg o at char_left with dissolve
    mei_speaking "不，没有……"
    hide xiangimg
    show xiangimg fist eye_still at char_right
    xiang_speaking "噢。"
    hide xiangimg with dissolve
    hide meiimg with dissolve
    show cg_x91 at cg_0 with fade
    mei "我最终没留下相片，只是看向夏把多出的一张也贴在墙上。"
    mei "向夏盯着墙面，不知道是在看我们的照片，还是在看别的地方。"
    mei_speaking "……"
    xiang_speaking "在看什么？"
    mei_speaking "你……不是，我在看你在看什么。"
    xiang_speaking "噗……这也是回答吗？"
    mei_speaking "算是吧……"
    xiang_speaking "唔嗯，好吧。\n看这么久，干脆把照片带回去呗？"
    mei_speaking "啊？是你看得更久吧，你怎么不拿。"
    xiang_speaking "我才没有。"
    mei_speaking "那我也没有。"
    xiang_speaking "……"
    mei_speaking "……"
    scene bg_ground3 with fade
    mei "我们打住了这毫无营养的对话，只是沉默地站在原地。"
    mei "我在心里叹了口气，把视线从向夏身上重新转回墙面。"
    scene bg_black with dissolve
    show halfblack
    show cg_x91 behind halfblack at cg_0 with dissolve:
        blur 15
    mei "那张照片……我和她的照片，在众多亲密的照片里似是毫无违和感。但我们即使凝视许久，也没有人说要把其中一张照片带走。"
    mei "仿佛那不是照片，而是某种神秘的封印，只要揭下，就再也掩饰不住隐匿的秘密。"
    mei "没关系……我在内心说服自己。"
    scene bg_black with dissolve
    mei "留不下也没关系，我和她，本来就应该是这样。"
    stop music fadeout 0.5

    scene bg_station2 with fade
    $ renpy.sound.play(sound.car_pass, channel="sound", loop=False, fadein=0.5)
    show xiangimg o at char_right with dissolve
    xiang_speaking "车还没来吗？我们不会错过了吧。"
    show meiimg shirt o at char_left with dissolve
    mei_speaking "不会的，还没到时间。"
    hide xiangimg
    show xiangimg eye_squint laugh at char_right 
    xiang_speaking "好吧……今天真是感谢你了，偶尔这样出来玩也不错啊。"
    hide xiangimg
    show xiangimg smile at char_right 
    mei "她笑着望向我，一双眼睛显得亮晶晶的。\n我赶紧偏过头，不自然地移开话题。"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei_speaking "嗯，应该感谢路花……说起来，她说有件事想拜托你。"
    hide xiangimg
    show xiangimg o at char_right 
    xiang_speaking "咦？我跟她？我能帮到什么吗？"
    hide meiimg
    show meiimg shirt at char_left
    mei_speaking "嗯，是这样……"
    scene bg_station2 with fade
    mei "我大致复述了一下路花早上的安排。向夏一边听一边点头，最后甚至显得有点兴奋。"
    show xiangimg fist laugh at char_right with dissolve
    $ renpy.music.play(music.xiang_handing_out, channel="music", loop=True, fadein=0.5)
    xiang_speaking "哇，所以我也有戏份吗？"
    show meiimg shirt eye_wacky o at char_left with dissolve
    mei_speaking "……重点是在这里吗？"
    hide xiangimg
    show xiangimg fist smile at char_right 
    xiang_speaking "是啊，不是你说你姐姐的女朋友找你帮忙，然后也需要我当个工具人嘛。"
    hide meiimg
    show meiimg shirt eye_wacky at char_left
    mei_speaking "所以你也愿意当这个工具人？"
    hide xiangimg
    show xiangimg fist eye_squint smile at char_right 
    xiang_speaking "嘿嘿，多有意思啊，凑热闹嘛。"
    mei_speaking "……"
    hide meiimg
    show meiimg shirt eye_close o at char_left
    mei_speaking "好吧。\n我们明天先去那边看一下？"
    hide xiangimg
    show xiangimg fist eye_squint laugh at char_right 
    xiang_speaking "没问题，提前踩点嘛，我懂我懂。"
    mei "为什么被她说得像在做什么不好的事……"
    stop music fadeout 0.5

    scene bg_hill1 with fade
    $ renpy.sound.play(sound.mountain_birds, channel="nature", loop=True, fadein=0.2)
    mei "立涧村的北部不靠海，而是靠着高耸延绵的群山。山上有很多植物，山脚下也有大片的花草和其他设施。"
    xiang_speaking "这里好漂亮啊……我们要上山吗？"
    mei_speaking "不是啊，是要让叶成华自己去花丛那边。就那。"
    mei "我指了指右手边不远处，由几乎与人同高的花朵组成的花海。成百上千的花朵层叠交错，紧密相连，饱满的深绿和金黄仿佛充斥着无尽的活力。"
    xiang_speaking "哇哦。那也不错，看起来就很震撼。\n所以我之后就假装走丢了，你带着你姐姐过来找我吗？"
    mei_speaking "嗯，是这样……"
    xiang_speaking "这怎么显得我像个脑子不好使的？难道我不会自己找人问路吗。"
    mei_speaking "嗯，这个可能……太难的借口不太好演。"
    xiang_speaking "真没办法，唉，只能我委屈下自己了。谁让我也好奇呢？"
    mei_speaking "……我可没看出你哪里委屈。"
    xiang_speaking "别这样说嘛！"
    xiang_speaking "不过，她们看起来感情可真好，前段时间你姐姐不也让我们帮忙吗。"
    mei_speaking "是啊。"
    xiang_speaking "还真是有点令人羡慕。"
    mei_speaking "嗯。是啊。"
    stop nature fadeout 0.5
    return
