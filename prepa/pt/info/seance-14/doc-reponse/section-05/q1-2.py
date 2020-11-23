# Recentrage ---------------------------------------------------------------
# Pourcentage de l'image
O = 0.25

Lp, Lm, Hp, Hm = recenter(h, w, xi, yi, O)
print(Lp, Lm, Hp, Hm)

# On rajoute le rectangle vert de la 'safezone'
plt.plot([(w/2)*(1-O), (w/2)*(1+O), (w/2)*(1+O), (w/2)*(1-O), (w/2)*(1-O)],
         [(h/2)*(1+O), (h/2)*(1+O), (h/2)*(1-O), (h/2)*(1-O), (h/2)*(1+O)],
         'g')
plt.show()
