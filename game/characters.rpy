# main characters
define na = Character(None)
define mei = Character(None,what_color=gui.light_grey,who_color=gui.light_grey)
define mei_speaking = Character("梅雨",what_prefix="“",what_suffix="”",image='meiimg',callback=name_callback,cb_name="mei")
define xiang_speaking = Character("向夏",what_prefix="“",what_suffix="”",image='xiangimg',callback=name_callback,cb_name="xiang")
define peng_speaking = Character("彭江丽",what_prefix="“",what_suffix="”",image='pengimg',callback=name_callback,cb_name="peng")
define ye_speaking = Character("叶成华",what_prefix="“",what_suffix="”",image='yeimg',callback=name_callback,cb_name="ye")
define lu_speaking = Character("路花",what_prefix="“",what_suffix="”",image='luimg',callback=name_callback,cb_name="lu")
define unknown_speaking = Character("？？？",what_prefix="“",what_suffix="”")
define old_speaking = Character("老人",what_prefix="“",what_suffix="”")
define school_boy = Character("男学生",what_prefix="“",what_suffix="”")
define school_girl = Character("女学生",what_prefix="“",what_suffix="”")
define fem = Character("女人",what_prefix="“",what_suffix="”")
define mal = Character("男人",what_prefix="“",what_suffix="”")
define young_peng = Character("小时候的彭江丽",what_prefix="“",what_suffix="”")
define young_mei = Character("小时候的梅雨",what_prefix="“",what_suffix="”")
define stf = Character("工作人员",what_prefix="“",what_suffix="”")


init:
    layeredimage xiangimg:
        at sprite_highlight('xiang')
        group body:
            attribute hand default:
                "images/char/xiang/hand.png"
            attribute fist:
                "images/char/xiang/fist.png"

        group eyes:
            attribute eye_def default:
                "images/char/xiang/eye_def.png"
            attribute eye_close:
                "images/char/xiang/eye_close.png"
            attribute eye_squint:
                "images/char/xiang/eye_squint.png"
            attribute eye_still:
                "images/char/xiang/eye_still.png"
            attribute eye_shock:
                "images/char/xiang/eye_shock.png"

        group mouse:
            attribute def default:
                "images/char/xiang/default.png"
            attribute smile:
                "images/char/xiang/smile.png"
            attribute laugh:
                "images/char/xiang/laugh.png"
            attribute o:
                "images/char/xiang/o.png"

        group mask:
            attribute red:
                "images/char/xiang/red.png"


    layeredimage pengimg:
        at sprite_highlight('peng')
        group body:
            attribute coat default:
                "images/char/peng/coat.png"
            attribute shirt:
                "images/char/peng/shirt.png"

        group eyes:
            attribute eye_def default:
                "images/char/peng/eye_def.png"
            attribute eye_squint:
                "images/char/peng/eye_squint.png"
            attribute eye_angry:
                "images/char/peng/eye_angry.png"
            attribute eye_still:
                "images/char/peng/eye_still.png"
            attribute eye_care:
                "images/char/peng/eye_care.png"

        group mouse:
            attribute def default:
                "images/char/peng/default.png"
            attribute smile:
                "images/char/peng/smile.png"
            attribute laugh:
                "images/char/peng/laugh.png"
            attribute o:
                "images/char/peng/o.png"

        group mask:
            attribute red:
                "images/char/peng/red.png"


    layeredimage meiimg:
        at sprite_highlight('mei')
        group body:
            attribute coat default:
                "images/char/mei/coat.png"
            attribute shirt:
                "images/char/mei/shirt.png"

        group eyes:
            attribute eye_def default:
                "images/char/mei/eye_def.png"
            attribute eye_close:
                "images/char/mei/eye_close.png"
            attribute eye_wacky:
                "images/char/mei/eye_wacky.png"
            attribute eye_still:
                "images/char/mei/eye_still.png"
            attribute eye_shock:
                "images/char/mei/eye_shock.png"
            attribute eye_squint:
                "images/char/mei/eye_squint.png"

        group mouse:
            attribute def default:
                "images/char/mei/def.png"
            attribute smile:
                "images/char/mei/smile.png"
            attribute laugh:
                "images/char/mei/laugh.png"
            attribute o:
                "images/char/mei/o.png"

        group mask:
            attribute flower:
                "images/char/mei/flower.png"
            attribute shell:
                "images/char/mei/shell.png"

        group face:
            attribute red:
                "images/char/mei/red.png"

    
    layeredimage yeimg:
        at sprite_highlight('ye')
        group body:
            attribute ye default:
                "images/char/other/ye.png"

        group face:
            attribute laugh default:
                "images/char/other/ye_laugh.png"
            attribute smile:
                "images/char/other/ye_smile.png"
            attribute o:
                "images/char/other/ye_o.png"

    
    layeredimage luimg:
        at sprite_highlight('lu')
        group body:
            attribute lu default:
                "images/char/other/lu.png"

        group face:
            attribute laugh default:
                "images/char/other/lu_laugh.png"
            attribute smile:
                "images/char/other/lu_smile.png"
            attribute o:
                "images/char/other/lu_o.png"
