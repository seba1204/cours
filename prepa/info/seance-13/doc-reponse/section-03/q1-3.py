# plot creation
P = pltr('Exercice 6')

# image import
i = np.array(im.open(PHOTO).convert('L'))

# filtered images
o1 = outline(i, THRESHOLD_1)
o2 = outline(i, THRESHOLD_2)

# plot images
P.addSubplot(i, "original")
P.addSubplot(o1, f"outlined: {THRESHOLD_1}")
P.addSubplot(o2, f"outlined: {THRESHOLD_2}")

# show plot
P.show()
