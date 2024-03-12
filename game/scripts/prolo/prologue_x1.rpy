label prologue_x1:
    scene bg_meiliv with pixellate
    mei "我走到楼下，无言地盯着桌上的电话和贴在上面的纸条看了好一会，最终只是把写着号码的纸条塞下来收好。"
    mei "还是……算了吧。\n反正，不管怎么样，晚上也会见面的。"
    mei "距离晚饭还有一段时间，我已经睡饱，至少现在没有太累的感觉……要不，出门看看吧——十一岁之后，我就再没来过这里了，不知道现在变了多少。"

    scene bg_vil1 with pixellate
    mei "早就过了中午，阳光却依然不显颓势，热烈地展现自己的存在感。{p}我缓慢地在砂石路上踱步，没碰到几个人，也没人在意我，实在令人安心许多。"
    mei "说不定，叶成华的方法真的有效，她硬是把我拉回这个地方……我不由得再次展开幻想。{p}……明知道，不切实际。"

    scene bg_station with pixellate
    mei_speaking "……嗯？"
    mei "竟然走回这里了……大概是下意识顺着熟悉的路。就在上午，我才和叶成华在这里下了大巴，换成她的破三轮。"
    mei "被生锈的栏杆歪歪斜斜地围住，车站门口褪色的“欢迎光临”也显得并不那么欢迎。比起这个年代久远的招牌，边缘的一抹亮色更加吸引我的视线。"
    
    scene cg_x10 with wiperight
    mei "波浪卷头发，繁复的裙褶边，少见的长筒袜，倚靠在身侧的巨大行李箱……从上而下，她显得比我更加格格不入。\n即使在我上学的时候，也很少见到这样的打扮，更不要说在这样偏僻的地方。"
    show cg_x11 at cg_0 with pixellate
    hide cg_x10
    mei "以至于我看得愣了神，直到对方明显察觉到我的目光，转过头来。\n……感觉我这样有些没礼貌，我赶紧瞥开视线，避免产生多余的交流。"
    show cg_x10 at cg_0
    mei "——然而还是太晚了。"

    scene bg_station with pixellate
    show xiangimg laugh at char_right with moveinright
    unknown_speaking "打扰一下，你知道这个地方怎么走吗？"
    show meiimg o at char_left with moveinleft
    mei_speaking "……呃，抱歉，不知道。"
    hide xiangimg
    show xiangimg o at char_right 
    unknown_speaking "我看你好像是从那边过来的呀。这里有好几个地方，可以再看一下吗？还有——"
    mei_speaking "我也是刚来这里，所以真的不清楚。"
    hide meiimg
    show meiimg at char_left 
    mei "虽然感到抱歉，但我的确什么都不知道，只好直接打断了她的话。然而她只是停住一瞬间，却仍然有要继续说话的迹象。"
    mei "在这种时候，我也只能佩服自己的直觉……本能地觉得应付不来这个人，只可惜还是没能躲掉。"
    hide xiangimg
    show xiangimg laugh at char_right 
    unknown_speaking "那你是认识这里其他人的吧，有没有知道的人可以帮忙问一下呀？"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "……啊？"
    mei_speaking "呃，我想不太方便……抱歉，我还有事。"
    mei "她怎么能如此自然地说出这种话？我无法理解，也不想这尴尬的对话持续下去。"
    hide xiangimg
    show xiangimg smile at char_right 
    unknown_speaking "好吧好吧，那抱歉了，还是谢谢你。"
    hide meiimg
    show meiimg at char_left 
    mei_speaking "没事……"

    scene bg_station with pixellate
    mei "好累……结束莫名其妙的对话后，我开始感到疲乏，不知道是说话太累还是走路太累了。\n也许今天不适合出门，还是先回去吧。"
    mei "只是，我的预感也许真的只有在这种时候格外准确。"

    scene bg_vil1 with pixellate
    show pengimg o at char_right with moveinright
    unknown_speaking "梅雨……吗？！你，你是……？"
    show meiimg at char_left with easeinleft
    mei_speaking "……啊。"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "那个，好久不见……\n了……{size=30}彭江丽。{/size}"
    hide pengimg
    show pengimg smile at char_right 
    peng_speaking "嗯，好久不见啊。"
    mei "我们能说的，好像只剩下这些——仅限礼貌的打招呼。{p}也许是因为是意外遇到，连提前的准备都没有，就变成了这样。当然，也是最真实的模样……"
    hide meiimg
    show meiimg at char_left
    mei_speaking "……"
    hide pengimg
    show pengimg at char_right 
    peng_speaking "……"
    hide pengimg
    show pengimg smile at char_right 
    peng_speaking "……对了，成华姐之前说你下午在家。你现在出来身体还好吗？会不会——"
    hide meiimg
    show meiimg o at char_left
    mei_speaking "我没事的。"
    mei "糟糕，又提前打断了她的话……都怪之前那个人……不，是我自己太过敏感吧。"
    hide pengimg
    show pengimg eye_squint smile at char_right 
    peng_speaking "噢，这样……那，那要不要一起走走，去海边看看？或者，我们就一起回去？"
    hide meiimg
    show meiimg eye_still at char_left
    mei "她在努力维持话题，即使我如此失礼。只是不知为何，她的笑容——那样礼貌而标准——并没有宽慰到我。\n我真是个糟糕的人……"
    hide meiimg
    show meiimg at char_left
    mei_speaking "都可以。\n就，走走吧。"
    hide pengimg
    show pengimg laugh at char_right 
    peng_speaking "嗯，好！"