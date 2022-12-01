
def isPalindrome(s):
    return s == s[::-1]
 
 
#
s = "TENET"
ans = isPalindrome(s)
 
if ans:
    print(" yes string is palindrome")
else:
    print("No string is palindrome")