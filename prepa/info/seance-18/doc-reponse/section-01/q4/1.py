def tri_rec(A, n, p):
    if n < p:
        # le pivot V=A[n] devient V=A[m] a la bonne place m dans A
        m = partition(A, n, p)
        tri_rec(A, n, m)  # On trie avant A[m]
        tri_rec(A, m+1, p)  # On trie apres A[m]

def tri_rapide(A):
    # A completer !
