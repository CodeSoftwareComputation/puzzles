import math

def calculate(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    d1 = x1 - x2
    d2 = y1 - y2

    return math.sqrt(d1 ** 2 + d2 ** 2)
