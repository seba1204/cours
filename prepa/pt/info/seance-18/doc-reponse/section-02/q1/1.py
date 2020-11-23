from time import perf_counter

def temps(n):
    A = [r.randint(0, 50) for k in range(n)]
    B = A[:]
    t1 = perf_counter()
    tri_rapide(A)
    t_rap = perf_counter() - t1

    t1 = perf_counter()
    tri_insertion(B)
    t_ins = perf_counter() - t1

    return (t_ins/t_rap)
