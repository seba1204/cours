def motorSpeed(wm, Tm):
    A = 2 * (a * d - b * c - d * l * cos(Tm) - c * l * sin(Tm))
    B = 2 * (-a * c - b * d - d * l * sin(Tm) + c * l * cos(Tm))
    C = a**2 + b**2 + c**2 + d**2 + 2 * l * (b * sin(Tm) - a * cos(Tm))
    Ap = 2 * l * wm * (d * sin(Tm) - c * cos(Tm))
    Bp = 2 * l * wm * (- d * cos(Tm) - c * sin(Tm))
    Cp = 2 * l * wm * (a * sin(Tm) + b * cos(Tm))

    return (A, B, C, Ap, Bp, Cp)
