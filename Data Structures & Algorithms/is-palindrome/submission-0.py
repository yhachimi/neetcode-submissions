class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid =  "".join(c.lower() for c in s if c.isalnum())
        if valid == valid[::-1]:
            return True
        return False
        