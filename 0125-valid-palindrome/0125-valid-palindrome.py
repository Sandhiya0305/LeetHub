class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        s = s.lower()
        for i in s:
            if i.isalnum(): r += i
        return r == r[::-1]