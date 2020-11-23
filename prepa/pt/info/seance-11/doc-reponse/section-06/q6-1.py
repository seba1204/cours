def repartition(Z, T):
    A = []
    for t in T:
        q = min(len(Z), int(t*espe(Z)) + 1)
        A.append(sum(Z[:q]))
    return A
