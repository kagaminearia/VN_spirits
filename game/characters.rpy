# main characters
define mei = Character("")
define mei_speaking = Character("梅雨",what_prefix="“",what_suffix="”")
define xiang_speaking = Character("向夏",what_prefix="“",what_suffix="”")
define peng_speaking = Character("彭江丽",what_prefix="“",what_suffix="”")
define ye_speaking = Character("叶成华",what_prefix="“",what_suffix="”")
define lu_speaking = Character("路花",what_prefix="“",what_suffix="”")



init:
    layeredimage xiangimg:
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
        group body:
            attribute coat default:
                "images/char/mei/coat.png"
            attribute shirt:
                "images/char/mei/coat.png"

        group eyes:
            attribute eye_def default:
                "images/char/mei/eye_def.png"
            attribute eye_close:
                "images/char/mei/eye_close.png"
            attribute eye_wacky:
                "images/char/mei/eye_wacky.png"
            attribute eye_still:
                "images/char/mei/eye_still.png"

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

    
    layeredimage yeimg:
        group body:
            attribute ye default:
                "images/char/other/ye.png"

        group face:
            attribute laugh default:
                "images/char/other/ye_laugh.png"
            attribute smile:
                "images/char/other/ye_smile.png"

    
    layeredimage luimg:
        group body:
            attribute lu default:
                "images/char/other/lu.png"

        group face:
            attribute laugh default:
                "images/char/other/lu_laugh.png"
            attribute smile:
                "images/char/other/lu_smile.png"
