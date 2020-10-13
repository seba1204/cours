def test(A, B, E, sigm0):
    for i in range(10):
        valTh = E * A[i] + sigm0
        valRel = B[i]
        if(valRel < 1.05 * valTh):
            return False
        return True
