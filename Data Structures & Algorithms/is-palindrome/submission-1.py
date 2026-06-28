class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()])
        if s.lower() == s[::-1].lower():
            return True
        return False
        