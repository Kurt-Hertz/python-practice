
def inter(x1, x2, y1, y2):
    #m = (y1 -y2) / (x1 -x2)
    return (y2 ** 3  - y1 ** 3) * (x1 -x2) / (3 * (y1 -y2))
    return y2 ** 3 / (3 * (y1 -y2) / (x1 -x2)) - y1 ** 3 / (3 * (y1 -y2) / (x1 -x2))
    #return ((m * (x1 - x2) + y2) ** 3) / (3 * m) - ((y2) ** 3) / (3 * m)

print(inter(0, 6, 0, 3))