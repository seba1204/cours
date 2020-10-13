# Position -----------------------------------------------------------------
X, Y, x, y, xi, yi = position(mask)

plt.plot(X, Y, 'b')
plt.plot(x, y, 'bx')
plt.imshow(i, alpha=0.3)
plt.show()
