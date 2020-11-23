def bissextile(a):
    return not(a % 400) or (not(a % 4) and bool(a % 100))
