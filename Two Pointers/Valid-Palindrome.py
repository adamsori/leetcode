## Using built-in functions
#class Solution:
#    def isPalindrome(self, s: str) -> bool:
#        clearString = "".join(c for c in s if c.isalnum()).lower()
#        stringSize = len(clearString) - 1
#        
#        for i in range(stringSize):
#            if clearString[i] == clearString[stringSize]:
#                stringSize -= 1
#            else:
#                return False
#        return True
                
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1 
            while right > left and not self.isAlphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
            
        return True
        
    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
         ord('a') <= ord(c) <= ord('z') or
         ord('0') <= ord(c) <= ord('9'))
        