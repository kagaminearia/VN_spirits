label chap1_x1:
    mei "还是说点什么吧……虽然可能有些突兀。毕竟最近都抬头不见低头见，缓和下气氛也可以。"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "要不换厚衣服，这边温差大，早晚很冷。"
    hide xiangimg
    show xiangimg fist o at char_right
    unknown_speaking "噢，谢谢，还真是。\n不过，这可是我最厚的衣服了。嗯……"
    hide meiimg
    show meiimg shirt at char_left
    mei "也许我们对厚的定义不同……我看着她的贴身长袖，一时间不知道该接什么话。"
    hide xiangimg
    show xiangimg o at char_right
    unknown_speaking "要不你借——哦，不，你知道哪里有超市么？"
    hide meiimg
    show meiimg shirt o at char_left
    mei_speaking "嗯……知道。要一起去吗？\n我刚好，也要去。"
    hide xiangimg
    show xiangimg smile at char_right
    unknown_speaking "这么巧，好啊，走吧。\n话说你叫什么来着？一直不知道也挺不方便。"
    mei_speaking "……梅雨。"
    mei "不知道为什么，和她说话总有种费劲的感觉……总觉得，真是个超级自我的人。"
    mei_speaking "呃，你呢？"
    hide xiangimg
    show xiangimg eye_squint laugh at char_right
    xiang_speaking "我叫向夏，方向的向，夏天的夏。\n这也算是认识了，之后多多指教啰。"
    stop sound fadeout 0.5
    $ renpy.sound.set_volume(1.0, 0, channel="sound")
    return
