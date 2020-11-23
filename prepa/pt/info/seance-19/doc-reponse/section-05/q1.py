from scipy.integrate import quad

res, err = quad(g, 0, 6)
print(res, err)
