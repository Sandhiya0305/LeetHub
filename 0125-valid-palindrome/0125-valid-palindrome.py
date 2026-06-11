class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        s = s.lower()
        for i in s:
            if i.isalpha() or i.isnumeric(): r += i
        return r == r[::-1]