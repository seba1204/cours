def diff(a, b):
    result = a.copy()
    for el in b:
        if (el in result):
            result.remove(el)
    return (a, b, result)


# ----- Tests  -----
if __name__ == "__main__":
    a = [2, 7, 8, 15, 2, 3, 4, 5, 2, 3]
    b = [2, 13, 8, 3, 2, 7, 8, 3]
    d = diff(a, b)
    print(
        'liste a :\n\t{}\nliste b :\n\t{}\ndiff(a, b) :\n\t{}'
        .format(a, b, d[2])
    )
