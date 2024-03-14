define c0_x1 = 0
define c0_p1 = 0
label prologue:
    call prologue_0
    menu:
        "联系彭江丽":
            call prologue_p1
            $ c0_p1 = 1
            $ p_point += 1
        "自己打发时间":
            call prologue_x1
            $ c0_x1 = 1
            $ x_point += 1  
    call prologue_1

define c1_x1 = 0
define c1_p1 = 0
label chapter1:
    call chap1_1
    menu:
        "提醒她多穿衣服":
            call chap1_x1
            $ c1_x1 = 1
            $ x_point += 1
        "继续忽略":
            call chap1_p1
            $ c1_p1 = 1 
            $ p_point += 1 
    call chap1_2
    if c1_p1 == 1:
        call chap1_p2
    else:
        call chap1_x2