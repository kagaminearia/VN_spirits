init python:
    # gallery initialize
    gallery_thumb_size = (192, 108)
    gallery_image_size = (1920,1080)
    ## list off all the gallery image
    ## names we're going to use in this gallery

    ## Set up the gallery
    g = Gallery()
    g.locked_button = Transform("#333", xysize=gallery_thumb_size)

    # declare the various gallery images
    # gallery m
    g.button('cgbtn_m1')
    g.unlock('cg_m10')
    g.image(Transform("images/cg/cg_m10.jpg", xysize=gallery_image_size))

    g.button('cgbtn_m2')
    g.unlock('cg_m20')
    g.image(Transform("images/cg/cg_m20.jpg", xysize=gallery_image_size))

    g.button('cgbtn_m3')
    g.unlock('cg_m30')
    g.image(Transform("images/cg/cg_m30.jpg", xysize=gallery_image_size))
    g.unlock('cg_m31')
    g.image(Transform("images/cg/cg_m31.jpg", xysize=gallery_image_size))

    # gallery p
    g.button('cgbtn_p1')
    g.unlock('cg_p10')
    g.image(Transform("images/cg/cg_p10.jpg", xysize=gallery_image_size))
    g.unlock('cg_p11')
    g.image(Transform("images/cg/cg_p11.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p2')
    g.unlock('cg_p20')
    g.image(Transform("images/cg/cg_p20.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p3')
    g.unlock('cg_p30')
    g.image(Transform("images/cg/cg_p30.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p4')
    g.unlock('cg_p40')
    g.image(Transform("images/cg/cg_p40.jpg", xysize=gallery_image_size))
    g.unlock('cg_p41')
    g.image(Transform("images/cg/cg_p41.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p5')
    g.unlock('cg_p50')
    g.image(Transform("images/cg/cg_p50.jpg", xysize=gallery_image_size))
    g.unlock('cg_p51')
    g.image(Transform("images/cg/cg_p51.jpg", xysize=gallery_image_size))
    g.unlock('cg_p52')
    g.image(Transform("images/cg/cg_p52.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p6')
    g.unlock('cg_p61')
    g.image(Transform("images/cg/cg_p61.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p7')
    g.unlock('cg_p71')
    g.image(Transform("images/cg/cg_p71.jpg", xysize=gallery_image_size))
    g.unlock('cg_p72')
    g.image(Transform("images/cg/cg_p72.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p8')
    g.unlock('cg_p81')
    g.image(Transform("images/cg/cg_p81.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p9')
    g.unlock('cg_p91')
    g.image(Transform("images/cg/cg_p91.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p10')
    g.unlock('cg_p101')
    g.image(Transform("images/cg/cg_p101.jpg", xysize=gallery_image_size))
    g.unlock('cg_p102')
    g.image(Transform("images/cg/cg_p102.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p11')
    g.unlock('cg_p111')
    g.image(Transform("images/cg/cg_p111.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p12')
    g.unlock('cg_p121')
    g.image(Transform("images/cg/cg_p121.jpg", xysize=gallery_image_size))
    g.unlock('cg_p122')
    g.image(Transform("images/cg/cg_p122.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p13')
    g.unlock('cg_p131')
    g.image(Transform("images/cg/cg_p131.jpg", xysize=gallery_image_size))
    g.unlock('cg_p132')
    g.image(Transform("images/cg/cg_p132.jpg", xysize=gallery_image_size))
    g.unlock('cg_p133')
    g.image(Transform("images/cg/cg_p133.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p14')
    g.unlock('cg_p141')
    g.image(Transform("images/cg/cg_p141.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p15')
    g.unlock('cg_p151')
    g.image(Transform("images/cg/cg_p151.jpg", xysize=gallery_image_size))
    g.unlock('cg_p152')
    g.image(Transform("images/cg/cg_p152.jpg", xysize=gallery_image_size))
    g.unlock('cg_p153')
    g.image(Transform("images/cg/cg_p153.jpg", xysize=gallery_image_size))
    g.unlock('cg_p154')
    g.image(Transform("images/cg/cg_p154.jpg", xysize=gallery_image_size))
    g.unlock('cg_p155')
    g.image(Transform("images/cg/cg_p155.jpg", xysize=gallery_image_size))
    g.unlock('cg_p156')
    g.image(Transform("images/cg/cg_p156.jpg", xysize=gallery_image_size))
    g.unlock('cg_p157')
    g.image(Transform("images/cg/cg_p157.jpg", xysize=gallery_image_size))

    g.button('cgbtn_p16')
    g.unlock('cg_p161')
    g.image(Transform("images/cg/cg_p161.jpg", xysize=gallery_image_size))


    # gallery x
    g.button('cgbtn_x1')
    g.unlock('cg_x10')
    g.image(Transform("images/cg/cg_x10.jpg", xysize=gallery_image_size))
    g.unlock('cg_x11')
    g.image(Transform("images/cg/cg_x11.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x2')
    g.unlock('cg_x20')
    g.image(Transform("images/cg/cg_x20.jpg", xysize=gallery_image_size))
    g.unlock('cg_x21')
    g.image(Transform("images/cg/cg_x21.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x3')
    g.unlock('cg_x30')
    g.image(Transform("images/cg/cg_x30.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x4')
    g.unlock('cg_x40')
    g.image(Transform("images/cg/cg_x40.jpg", xysize=gallery_image_size))
    g.unlock('cg_x41')
    g.image(Transform("images/cg/cg_x41.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x5')
    g.unlock('cg_x51')
    g.image(Transform("images/cg/cg_x51.jpg", xysize=gallery_image_size))
    g.unlock('cg_x52')
    g.image(Transform("images/cg/cg_x52.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x6')
    g.unlock('cg_x61')
    g.image(Transform("images/cg/cg_x61.jpg", xysize=gallery_image_size))
    g.unlock('cg_x62')
    g.image(Transform("images/cg/cg_x62.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x7')
    g.unlock('cg_x71')
    g.image(Transform("images/cg/cg_x71.jpg", xysize=gallery_image_size))
    g.unlock('cg_x72')
    g.image(Transform("images/cg/cg_x72.jpg", xysize=gallery_image_size))
    g.unlock('cg_x73')
    g.image(Transform("images/cg/cg_x73.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x8')
    g.unlock('cg_x81')
    g.image(Transform("images/cg/cg_x81.jpg", xysize=gallery_image_size))
    g.unlock('cg_x82')
    g.image(Transform("images/cg/cg_x82.jpg", xysize=gallery_image_size))
    g.unlock('cg_x83')
    g.image(Transform("images/cg/cg_x83.jpg", xysize=gallery_image_size))
    g.unlock('cg_x84')
    g.image(Transform("images/cg/cg_x84.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x9')
    g.unlock('cg_x91')
    g.image(Transform("images/cg/cg_x91.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x10')
    g.unlock('cg_x101')
    g.image(Transform("images/cg/cg_x101.jpg", xysize=gallery_image_size))
    g.unlock('cg_x102')
    g.image(Transform("images/cg/cg_x102.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x11')
    g.unlock('cg_x111')
    g.image(Transform("images/cg/cg_x111.jpg", xysize=gallery_image_size))
    g.unlock('cg_x112')
    g.image(Transform("images/cg/cg_x112.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x12')
    g.unlock('cg_x121')
    g.image(Transform("images/cg/cg_x121.jpg", xysize=gallery_image_size))
    g.unlock('cg_x122')
    g.image(Transform("images/cg/cg_x122.jpg", xysize=gallery_image_size))
    g.unlock('cg_x123')
    g.image(Transform("images/cg/cg_x123.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x13')
    g.unlock('cg_x131')
    g.image(Transform("images/cg/cg_x131.jpg", xysize=gallery_image_size))
    g.unlock('cg_x132')
    g.image(Transform("images/cg/cg_x132.jpg", xysize=gallery_image_size))
    g.unlock('cg_x133')
    g.image(Transform("images/cg/cg_x133.jpg", xysize=gallery_image_size))
    g.unlock('cg_x134')
    g.image(Transform("images/cg/cg_x134.jpg", xysize=gallery_image_size))
    g.unlock('cg_x135')
    g.image(Transform("images/cg/cg_x135.jpg", xysize=gallery_image_size))
    g.unlock('cg_x136')
    g.image(Transform("images/cg/cg_x136.jpg", xysize=gallery_image_size))
    g.unlock('cg_x137')
    g.image(Transform("images/cg/cg_x137.jpg", xysize=gallery_image_size))

    g.button('cgbtn_x14')
    g.unlock('cg_x141')
    g.image(Transform("images/cg/cg_x141.jpg", xysize=gallery_image_size))
    g.unlock('cg_x142')
    g.image(Transform("images/cg/cg_x142.jpg", xysize=gallery_image_size))
    g.unlock('cg_x143')
    g.image(Transform("images/cg/cg_x143.jpg", xysize=gallery_image_size))



    g.transition = dissolve
