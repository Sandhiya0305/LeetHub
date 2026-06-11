class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        f, l = 0, len(s) - 1
        while f < l:
            t = s[f]
            s[f] = s[l]
            s[l] = t
            f += 1
            l -= 1

            