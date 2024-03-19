define c0_x1 = 0
define c0_p1 = 0
label prologue:
    call prologue_0
    menu:
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
        "转头看彭江丽":
            $ p_point += 1
            call chap3_p1
        "转头看向夏":
            $ x_point += 1
            call chap3_x1
    call chap3_2
    menu:
        "投给彭江丽":
            $ x_point += 1
            call chap3_x2
        "投给向夏":
            $ p_point += 1
            call chap3_p2

    return