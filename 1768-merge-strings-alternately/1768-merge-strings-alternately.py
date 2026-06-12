class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = len(word1), len(word2)
        r = ""
        if w1 == w2:
            for i in range(0, w1):
                r += word1[i] + word2[i]
        elif w1 < w2:
            i = 0
            for i in range(0, w1):
                r += word1[i] + word2[i]
            r += word2[i + 1:]
        else:
            i = 0
            for i in range(0, w2):
                r += word1[i] + word2[i]
            r += word1[i + 1:]
        return r