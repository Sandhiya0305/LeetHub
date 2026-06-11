class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = "".join(filter(str.isalnum, s)).lower()
        return r == r[::-1]