# titles of each chapter
define c_title = [
    "“已经无所谓了”", # ch0
    "“随便相处一下”", # ch1
    "“万物有灵”", # ch2
    "“个人的意志”", # ch3
    "“白天和夜晚完全不同”", # ch4
    "“无法消除的刻痕”", # ch5
]

define p_title = [
    "“什么都不知道”", # ch6
    "“完美的笑容”", # ch7
    "“她的眼睛”", # ch8
    "“沉淀的记忆”", # ch9
    "“愿望”" # ch10
]

define x_title = [
    "“谁特别倔强”", # ch6
    "“欠你一个要求”", # ch7
    "“控制心跳”", # ch8
    "“讨厌你”", # ch9
    "“一点也不温暖”" # ch10
]

define endings = {
    "NE": "待定",
    "xBE": "好人",
    "xNE": "再见",
    "xHE": "触碰",
    "pBE": "谢谢",
    "pNE": "回避",
    "pHE": "成真"
}


define c0_x1 = 0
define c0_p1 = 0
label prologue:
    call prologue_0
    menu:
        mei "窗外的日光晃了晃眼，我回想起先前叶成华的话。距离晚上还有一段时间，我现在应该……？"
        "联系彭江丽":
            $ c0_p1 = 1
            $ p_point += 1
            call prologue_p1
        "自己打发时间":
            $ c0_x1 = 1
            $ x_point += 1  
            call prologue_x1
    call prologue_1
    return

define c1_x1 = 0
define c1_p1 = 0
label chapter1:
    call chap1_1
    menu:
        mei "说起来，她这件衣服可能也不够厚……"
        "提醒她多穿衣服":
            $ c1_x1 = 1
            $ x_point += 1
            call chap1_x1
        "继续忽略":
            $ c1_p1 = 1 
            $ p_point += 1 
            call chap1_p1
    call chap1_2
    if c1_p1 == 1:
        call chap1_p2
    else:
        call chap1_x2
    call chap1_3
    menu:
        mei "彭江丽犹豫的声音打断了我的思考，抬头一看，向夏正专心吃饭，而彭江丽也已经穿好外套，只有我还呆呆地站在原地。"
        "送彭江丽回家":
            $ p_point += 1 
            call chap1_p3
        "和彭江丽说再见":
            $ x_point += 1
            call chap1_x3
    call chap1_4
    return

label chapter2:
    call chap2_1
    menu:
        xiang_speaking "这可怎么办……我让她这么生气，那我的问题岂不是问不了了？我还能挽回一下吗，找点什么办法？"
        "“你只在意这个？”":
            $ p_point += 1 
            call chap2_p1     
        "“想办法道歉吧”":
            $ x_point += 1
            call chap2_x1
    call chap2_2
    return

label chapter3:
    call chap3_1
    menu:
        mei "不知道为什么，彭江丽和向夏都睡在这里。{p}估计……她们也是累了吧，不知道，现在怎么样……"
        "转头看彭江丽":
            $ p_point += 1
            call chap3_p1
        "转头看向夏":
            $ x_point += 1
            call chap3_x1
    call chap3_2
    menu:
        mei "虽然很无聊，不过现在本来也没别的事做……投给谁呢？"
        "彭江丽":
            $ x_point += 1
            call chap3_x2
        "向夏":
            $ p_point += 1
            call chap3_p2
    call chap3_3
    return

define c4_x1 = 0
define c4_p1 = 0
label chapter4:
    call chap4_1
    menu:
        mei "果然还很早，难怪会感觉有点头晕……{p}不过，她们这是都没睡吗……"
        "劝彭江丽睡觉":
            $ x_point += 1
            $ c4_x1 = 1
            call chap4_x1
        "和彭江丽聊天":
            $ p_point += 1
            $ c4_p1 = 1
            call chap4_p1
    call chap4_2
    menu:
        xiang_speaking "你要打电话吗？给你姐姐说一声，不然她肯定担心。"
        "答应":
            $ x_point += 1
            call chap4_x2
        "拒绝":
            $ p_point += 1
            call chap4_p2
    call chap4_3
    return

define route = "n"
label chapter5:
    call chap5_0
    if c4_x1 == 1 and c0_x1 == 1 and x_point > p_point:
        $ route = "x"
    elif c4_p1 == 1 and c0_p1 == 1 and x_point < p_point:
        $ route = "p"
    
    if route == "n":
        jump NE
        return
    call chap5_1
    if route == "x":
        call chap5_x1
    else:
        call chap5_p1
    call chap5_2
    return

# Test sub chapters inside chapter 5
label chapter5_x:
    call chap5_0
    call chap5_1
    call chap5_x1
    call chap5_2
    return

label chapter5_p:
    call chap5_0
    call chap5_1
    call chap5_p1
    call chap5_2
    return

label chapter5_ne:
    call chap5_0
    jump NE
    return
    
label chapter6:
    call chap6_1
    if route == "x":
        call chapter6x
    else:
        call chapter6p
    return


label chapter6x:
    call chap6_1
    call chap6_x1
    call chap6_x2
    call chap6_x3
    call chap6_x4
    return

label chapter6p:
    call chap6_1
    call chap6_p1
    call chap6_p2
    call chap6_p3
    return


define x_end = "n"
label chapter7:
    if route == "x":
        call chapter7_x
    else:
        call chapter7_p
    return


label chapter7_x:
    call chap7_x1
    menu:
        mei "不过……"
        "答应":
            call chap7_x1n
        "拒绝":
            $ x_end = "h"
            call chap7_x1h
    call chap7_x2
    if x_end == "n":
        call chap7_x2n
        jump xNE
    else:
        call chap7_x2h
    return

label chapter7_p:
    call chap7_p1
    call chap7_p2
    call chap7_p3
    return

label chapter8:
    if route == "x":
        call chapter8x
    else:
        call chapter8p
    return

label chapter8x:
    call chap8_x1
    call chap8_x2
    call chap8_x3
    call chap8_x4
    return

label chapter8p:
    call chap8_p1
    call chap8_p2
    return

label chapter9:
    if route == "x":
        call chapter9x
    else:
        call chapter9p
    return

label chapter9x:
    call chap9_x1
    call chap9_x2
    return

label chapter9p:
    call chap9_p1
    menu:
        mei "不能这样……"
        "说实话":
            call chap9_p2
            menu:
                "停下来":
                    jump pBE
                "追上去":
                    call chap9_p3
        "搪塞过去":
            jump pNE
    return

label chapter10:
    if route == "x":
        call chapter10x
    else:
        call chapter10p
    return

label chapter10x:
    call chap10_x
    menu:
        "答应":
            jump xHE
        "拒绝":
            jump xBE
    return

label chapter10p:
    call chap10_p1
    jump pHE
    return

label test:
    call chap10_x1
    return