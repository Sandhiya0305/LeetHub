class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for i in s.lower():
            if i.isalpha() or i.isnumeric(): r += i
        return r == r[::-1]