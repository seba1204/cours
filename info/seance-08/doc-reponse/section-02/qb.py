def sumYears(begin, end):
    A = [k for k in range(begin, end + 1) if bissextile(k)]
    return (A, sum(A))
