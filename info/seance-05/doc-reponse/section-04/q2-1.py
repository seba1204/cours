def Tpv(Tm, Tv, wm):
    A, B, C, Ap, Bp, Cp = temporalData(wm, Tm)
    return (Ap * cos(Tv) + Bp * sin(Tv) + Cp) / (A * sin(Tv) - B * cos(Tv))
