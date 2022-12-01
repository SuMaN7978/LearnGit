
def isPalindrome(s):
    return s == s[::-1]

s = "TENET"
print(s)
ans = isPalindrome(s)
 
if ans:
    print(" yes string is palindrome",ans)
else:
    print("No string is palindrome",ans)