def circularite(Xc, Yc, R, X, Y):
    # On calcule la norme de CM_i
    R_mes = np.sqrt((Xc-X)**2 + (Yc-Y)**2)

    E_min = R - np.min(R_mes)
    E_max = np.max(R_mes) - R

    dc = E_max + E_min
    return(E_max, E_min, dc)
