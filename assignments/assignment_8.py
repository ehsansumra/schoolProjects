# Assignment 8
# Ehsan Sumra

# Using recursion and slicing, reverse the string.
def reverseStr(string):

    if len(string) == 1:
        return string
    
    newStr = string[1:]
    return (reverseStr(newStr)) + string[0]

# Using recursion, prints the string in the specified output
def recString(string,  temp=''):
    
    if len(string) == 1:
        return string
    
    newStr = string[-1] + temp
    if len(newStr) == 1:
        print('*')
    print(newStr)
    return  recString(string[:-1], newStr) + string[-1]


# multiples of b are subtracted from a until the remainder is less than b
# quotient remainder theorem
# a/b = (a = b*Q + R)
def euclid(a, b):
    
    # Base case: If the remainder passed in 0, then "a" is the gcd
    # Prevents divide by 0
    if b == 0:
        return max(a, -a)

    else:
        R = a % b
        print(f"call euclid({b},{R})")
        # Divide the second term by the remainder of a/b, recursively until the remainder is 0.
        return euclid(b, R)

if __name__ == "__main__":
    print("Reverse 'Hello!': ", reverseStr("Hello!"), "\n" )
    print(recString("abcde"), "\n")
    print(recString("abc"), "\n")
    print("gcd =", euclid(1071, 462))
    print("gcd =", euclid(462, 1071))
    print("gcd =", euclid(68, 102))
    print("gcd =", euclid(102, 68))
