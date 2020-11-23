r, t = E.GetPolar()
b = E.GetPetitRayon(-t)

E.Rotate(-t)
E.Tracer()


print(b)
