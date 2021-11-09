import time
def factorial(num):


    if num == 1:
        return 1
    
    return num * factorial(num - 1)


def iterfactorial(num):
    startTime = time.time()
    
    product = 1
    for i in range(1, num + 1):
        product*= i
    
    endTime = time.time()
    executionTime = endTime - startTime
    print("iterative runtime: %4.20f seconds" %(executionTime))
    
    return product

def test():
    startTime = time.time()
    factorial(100)
    endTime = time.time()
    executionTime = endTime - startTime

    print("recursive runtime: %4.20f seconds" %(executionTime))
    iterfactorial(100)

if __name__ == "__main__":
    test()