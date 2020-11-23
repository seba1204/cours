def openCSV(path):

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)

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
