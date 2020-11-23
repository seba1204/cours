def firecrapB(n):
    if (n == 1):
        return ([
            [1, 1],
            [0, 1]
        ])
    l = firecrapB(n-1)
    return [
        [l[0][1], sum(l[0])],
        [1/l[0][1], sum(l[1])]
    ]
