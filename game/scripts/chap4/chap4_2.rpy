label chap4_2:
    scene bg_black with fade
    "……"

    scene bg_emptyroom with fade
    $ renpy.sound.play(sound.rain_on_window, channel="sound", loop=True, relative_volume=0.5)
    mei_speaking "……"
    mei_speaking "咦……"
    mei "我揉了揉眼睛，一时间有些不适应明亮的房间，大脑还处在宕机阶段。"
    mei "昨天晚上……后来的事我记不太清，这么短的休息时间对我来说还是负担太大了。{p}雷声减弱后，我又回头睡了一觉，直到将近正午才醒来。"
    mei "说是明亮，其实也是偏暗的自然光线。雨还在下，只是没有昨天的乌云压顶，又到了正午，两相对比才显得更加光亮。"
    mei "白天和夜晚完全不同，那些不安定的想法，一旦出现，就会全部在明朗的世界里无所遁形。"
    mei "因此，昨晚的事也随着黑暗一起褪去，我的眼角瞥到房间里的其他人，并不打算再继续回忆。"

    scene bg_emptyroom with pixellate
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "现在……"
    show pengimg shirt o at char_mid with moveinright
    peng_speaking "我去楼下检查一下现在的情况吧。"
    mei "简单吃过午饭——也就是饼干和矿泉水——之后，彭江丽突然开口。"
    hide meiimg
    # show meiimg shirt at char_left with moveinleft
    mei_speaking "啊？我去吧。"
    hide pengimg
    show pengimg shirt at char_mid 
    peng_speaking "我去就可以了，我知道怎么检查更完善，而且，你可能也没那么方便，我弄完会跟你说的。"
    mei_speaking "一起吧。"
    hide pengimg
    show pengimg shirt eye_care o at char_mid 
    peng_speaking "可是，你……{p}我真的很担心，万一又……"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "……"
    mei "她用这个理由，我便不知道怎么反驳。理智上，我当然知道自己不会连这点事都做不了。但是，但是……{p}要是又拖累别人，怎么办……"
    show xiangimg fist o at char_right with moveinright
    xiang_speaking "怎么了怎么了？"
    hide xiangimg
    show xiangimg fist smile at char_right
    xiang_speaking "要现在检查吗？那我也去，人多更方便做事嘛。{p}这房子也没多大，有事叫一声就好了吧？"
    hide meiimg
    show meiimg shirt eye_still o at char_left
    mei_speaking "那……一起去？"
    hide pengimg
    show pengimg shirt eye_care at char_mid 
    peng_speaking "……好吧。{p}不过，你介意换一下我的衣服吗？啊，是最近新买的，我没穿过的。"
    hide meiimg
    show meiimg shirt eye_still at char_left
    mei_speaking "嗯？"
    hide pengimg
    show pengimg shirt o at char_mid 
    peng_speaking "就是，换成裤子的话可能更方便一些吧。"
    mei "我顺着她的目光看向延至膝盖的裙摆，终于理解了她的意思。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "噢，好……谢谢。。"

    scene bg_black with dissolve
    $ renpy.music.play(music.time_alone, channel="music", loop=True, fadein=0.5)
    mei "我重复好几次扎紧系带的动作，堪堪让裤子固定在腰上。接下来，把之前的衣服放好……{p}我拿起裙子，一瞬间有些莫名的恍惚。"
    show cg_m30 at cg_0 with dissolve
    mei "我的衣柜里大多是这样的裙子，宽松，单色，样式一致。{p}和喜好无关，因为平时总是要接受检查，时不时需要住院，这样的衣服穿脱起来更方便，不知道什么时候就习惯了。"
    mei "在那天之后，也没有别的事，更是每天都穿成这样。而现在……"
    show cg_m31 at cg_0 with Dissolve(0.2)
    mei "看着镜子中不太合身的衣服，我久违地感受到——不，应该说是再次注意到被刻意忽略的——{p}格格不入。"
    mei_speaking "……"
    mei_speaking "算了，别再想了。"
    stop music fadeout 0.5

    scene bg_emptyroom with fade
    show pengimg shirt o at char_left with dissolve
    $ renpy.sound.play(sound.wind, channel="others", loop=True, relative_volume=0.5)
    peng_speaking "我去检查后院那一片，向夏你去前门，梅雨去厨房和洗手间看一下吧。"
    show xiangimg o at char_right with dissolve
    xiang_speaking "好，不过要检查什么啊？"
    mei "你都不知道就跟来了吗……"
    peng_speaking "检查门窗的缝隙有没有堵好，然后看地上的排水口还能不能用了，不能的话试着处理一下。{p}虽然用处不大，但进来的水能挡多少挡多少吧。"
    peng_speaking "对了，我之前带了备用的手电筒，给你们用。不用担心电量，一直开着就行。"
    hide meiimg
    show pengimg shirt smile at char_left 
    peng_speaking "要我跟你一起吗，梅雨？"
    mei "我摇摇头，示意她我自己没问题。{p}彭江丽虽然还是犹疑，但还是把手电筒递给了我。"
    hide meiimg
    show pengimg shirt smile at char_left 
    peng_speaking "你们都小心点，尤其是脚底下看不见，如果有事就叫我。"
    hide xiangimg
    show xiangimg smile at char_right
    xiang_speaking "好嘞，没问题。"

    scene bg_meikitc with pixellate
    show halfdarkblue
    mei "有点冰啊……即使做了心理准备，脚伸进水里的时候我还是不可避免地颤抖起来。{p}水大概在脚踝上方五厘米，水势不急，所以我也能控制住脚步。"
    mei "手电筒晃晃悠悠，只能照亮一小块区域。虽然是中午，但仍然没有阳光，即使没拉窗帘也像是已经到了傍晚。"
    mei "我小心探进厨房，这里没什么家具，检查起来也不算难。不出意料，角落的几个出水口都有些阻塞。{p}我有些费劲地弯腰，用手指清理累积起来的细小杂物。"
    
    hide halfdarkblue with vpunchm
    $ renpy.sound.play(sound.thunder, channel="nature", loop=False)
    na "轰隆！！"
    mei_speaking "哇……！"
    show halfdarkblue
    mei_speaking "……哈啊……"
    mei "起身时，另一声巨大雷声吓得我停住动作，好一会才直起身体。\n我靠在墙角，轻轻吐出倦怠的叹息。"
    mei "来回弯腰低头让我的脑袋有些发胀，不过，至少现在暂时没问题了……"

    scene bg_emptyroom with pixellate
    mei "回到二楼，我简单冲了冲身上沾着的泥水，又换回自己的衣服。"
    show pengimg shirt o at char_right with moveinright
    peng_speaking "梅雨你怎么样？没觉得不舒服吧？"
    show meiimg shirt o at char_left with moveinleft
    mei_speaking "没。你们也弄完了？"
    hide pengimg
    show pengimg shirt smile at char_right
    peng_speaking "是啊，我比较熟练嘛，所以之前说都让我做也没关系的。"
    peng_speaking "嗯，待会没事了，你好好休息就好了。"
    hide meiimg
    show meiimg shirt at char_left 
    mei_speaking "噢……好。"
    mei "所以……我自己想着帮忙，实际上只是拖慢了她们的进度吗。"

    scene bg_black with dissolve
    mei "这一天晚上没有打雷，雨势似乎也变小了一些，我也逐渐习惯睡在两人中间，在断断续续的风声和雨声下，竟然获得了很安稳的睡眠。"
    stop music
    stop sound
    stop others
    stop nature

    scene bg_emptyroom with dissolve
    show xiangimg laugh at char_right with moveinright
    xiang_speaking "早啊，我跟你说，我的手机有信号了！"
    show meiimg shirt o at char_left with moveinleft
    $ renpy.sound.play(sound.bird_chirping_1, channel="nature", loop=False)
    mei_speaking "诶？"
    mei "因为太累，我睡得早，也起得早了一些。刚起床，就看到向夏挥着手机，显得比平时还活跃。{p}这也难怪，从开始下雨的时间算，没信号的时间都快持续两天了。"
    hide xiangimg
    show xiangimg o at char_right 
    xiang_speaking "你要打电话吗？应该要的吧？得给你姐姐说一声，不然她肯定担心。"

    