# image import
i = np.array(im.open(GREY_CAT))

# plot creation
P = pltr('Exercice 4')

# contrasted images
c1 = contraste(i, RATE_1)
c2 = contraste(i, RATE_2)

# plot images
P.addSubplot(i, "contrast=0")
P.addSubplot(c1, "contrast={}".format(RATE_1))
P.addSubplot(c2, "contrast={}".format(RATE_2))

# show plot
P.show()
