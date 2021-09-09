
# TODO: divide into functions

def square(num):
    return num * num

def squareRoot(num):
    return num**0.5
    
def computeCartesianDistance(x1, y1, x2, y2):
    
    return squareRoot(square(x2 - x1) + square(y2 - y1))

if __name__ == "__main__":
    dist = computeCartesianDistance(-7, -4, 17, 6.5)
    print(dist)