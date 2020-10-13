def init(x):
    if (x < 0):
        return-(init(-x))
    elif (x <= 7):
        return x/7
    return -(x-10)/3
