def angle(wm, Tmmax, N):
    _Tm = np.linspace(0, Tmmax, N)
    h = Tmmax / (wm * N)
    _Tpv = [Tpv(0, 0, wm)]
    _Tv = [0]
    for i in range(1, N):
        _Tv.append(_Tv[i-1] + _Tpv[i-1] * h)
        _Tpv.append(Tpv(_Tm[i-1], _Tv[i-1], wm))
    return (_Tm, _Tpv)
