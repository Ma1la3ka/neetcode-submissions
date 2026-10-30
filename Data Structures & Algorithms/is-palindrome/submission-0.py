class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        
        i = 0
        n = len(s) - 1
        
        while i < n:
            if s[i] != s[n]:
                return False
            i += 1
            n -= 1
            
        return True