def temps_rapide(n):
    A = [r.randint(0, 50) for k in range(n)]
    t1 = t.time()
    tri_rapide(A)
    return t.time()-t1
