def recenter(h, w, x, y, O):
    Lp, Lm, Hp, Hm = False, False, False, False
    if (x > O*w):
        Lp = True
    elif (x < -O*w):
        Lm = True

    if (y > O*h):
        Hp = True
    elif (y < -O*h):
        Hm = True

    return Lp, Lm, Hp, Hm
