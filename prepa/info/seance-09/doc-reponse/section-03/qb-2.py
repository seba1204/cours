def firecTime(n):
    T = []
    X = []
    for i in range(1, n+1):
        t1 = t.time()
        firec(i)
        T.append(t.time() - t1)
        X.append(i)
    return (X, T)
