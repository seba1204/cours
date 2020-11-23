# plot creation
P = pltr('Exercice 5')

# image import
i = np.array(im.open(LENA).convert('L'))

# filtered images
f1 = filtre(i)
f1 = filtre(i, 'GAUSSIAN')

# plot images
P.addSubplot(i, "without filter")
P.addSubplot(f1, "regular filter")
P.addSubplot(f1, "gaussian filter")

# show plot
P.show()
