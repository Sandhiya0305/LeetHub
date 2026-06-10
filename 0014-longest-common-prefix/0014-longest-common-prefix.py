class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = []
        for t in zip(*strs):
            if len(set(t)) > 1: return "".join(r)
            r.append(t[0])
        return "".join(r)