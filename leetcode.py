
    
def isPalindrome( x: int) -> bool:
    newx= str(x)
    return str(x) == newx[::-1]

print(isPalindrome(1212))

s='huy'
print(s[::-1])