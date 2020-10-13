def getMaxSpeed(borneMin, borneMax, pas, N):
    Vd, wm = 0, borneMin

    # Pour sauvegarder les anciennes valeurs
    Vd_o, wm_o = 0, borneMin

    while (Vd < Vmax and wm <= borneMax):

        # On sauvegarde les anciennes valeurs
        # Sinon on fait un tour de trop
        Vd_o, wm_o = Vd, wm

        TpvMax = abs(max(angle(wm, Tmmax, N)[1]))
        Vd = L * TpvMax
        wm += pas

    return (Vd_o, wm_o)
