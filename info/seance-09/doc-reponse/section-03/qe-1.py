def firecrapB(n):
    if (n == 1):
        return ([1, 1])
    l = firecrapB(n-1)
    return [l[1], sum(l)]
