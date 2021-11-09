
def reverseNum(n):
    reverse = 0
    while n != 0:
        remainder = n % 10
        reverse = (reverse * 10) + remainder
        n = n//10
    
    return reverse

def pushDigits(num):

    while num > 0:
        
print(reverseNum(807))
