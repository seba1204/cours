def firec(n):
    if (n == 0 or n == -1):
        return 1
    return firec(n-1) + firec(n-2)
