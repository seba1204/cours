def dicho(f, a, b, eps):
    if(abs(a-b) < 2*eps):
        return((a+b)/2)
    m = (a+b)/2
    if(f(a)*f(m) < 0):
        return (dicho(f, a, m, eps))
    return (dicho(f, m, b, eps))
