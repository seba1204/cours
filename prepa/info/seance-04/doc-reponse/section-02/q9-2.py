def lim_el(sigma, epsilon, E, sigm0):
    iMax = len(epsilon) - 1
    i = 0
    while (not test(sigma, epsilon,  E, sigm0) and i <= iMax - 10):
        i += 1
    if (i != 0):
        return(sigma[i])
    else:
        return (0)
