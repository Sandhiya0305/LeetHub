class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = ''
        while columnNumber > 0:
            columnNumber -= 1
            r = chr(65 + columnNumber % 26) + r
            columnNumber //= 26
        return r