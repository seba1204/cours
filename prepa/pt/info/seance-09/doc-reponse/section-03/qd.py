def fibo(n):
    a, b = 1, 1
    for i in range(n):
        c = a + b
        b = a
        a = c
    return c
