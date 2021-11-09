# Ehsan Sumra

def countDown(n):
    print(n)
    if n != 0:
        return countDown(n-1)

def reverse(string):
    if len(string) == 1:
        return string
        
    return reverse(string[1:]) + string[0]

def isPalindrome(string):
    return reverse(string) == string

def palindrome(string):
    # base case 
    if len(string) == 0:
        return True
    
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

if __name__ == "__main__":
    countDown(20)
    print(palindrome("raddar"))