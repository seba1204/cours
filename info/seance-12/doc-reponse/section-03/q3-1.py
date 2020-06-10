def rotation(greyScaleArray, percentage):
    height, width = greyScaleArray.shape
    alpha = (percentage / 100) * (np.pi / 2)
    c, s = cos(alpha), sin(alpha)
    w = int(width * c + height * s)
    h = int(height * c + width * s)
    newArray = np.full((h, w), 255)
    rMatrix = np.array(np.array(((c, -s), (s, c))))
    for y in range(height):
        for x in range(width):
            try:
                nY, nX = np.dot(rMatrix, np.array((y, x)))
                nY = nY + width * s
                newArray[int(nY), int(nX)] = greyScaleArray[y][x]
            except IndexError:
                pass
    return (newArray)
