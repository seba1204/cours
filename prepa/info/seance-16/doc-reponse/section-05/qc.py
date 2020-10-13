def resoudre():
    a = dicho(h, -1, 0)
    b = dicho(h, 0, 1)
    c = dicho(h, 3, 4)
    return a, b, c

a, b, c = resoudre()
A = int(a*b*c*10**6)/10**6
print(A == -1.559156)
