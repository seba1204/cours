def openCSV(path):
    f = open(path, 'r')
    X = []
    Y = []
    for line in f.readlines():
        try:
            a, b = line.split(',')
            a = float(a)
            b = float(b)
            X.append(a)
            Y.append(b)
        except:
            pass
    return (X, Y)
