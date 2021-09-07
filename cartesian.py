
# TODO: divide into functions
def computeCartesianDistance(x1, y1, x2, y2):
    x = (x2 - x1)**2
    y = (y2 - y1)**2

    return (x + y)**0.5

if __name__ == "__main__":
    dist = computeCartesianDistance(0,5, 7, 8)
    print(dist)