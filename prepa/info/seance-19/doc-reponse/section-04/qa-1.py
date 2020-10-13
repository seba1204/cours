def simpson(f, n, a, b, M):
    pas = (b-a)/n
    S = 0
    for k in range(n):
        S += pas*(f(a+k*pas)+4*f(a+(k+1/2)*pas)+f(a+(k+1)*pas))/6
    return int(S*10**16)/10**16, (b-a)*pas**4*M/2880
