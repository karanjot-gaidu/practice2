class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = []
        n, m = len(word1), len(word2)
        for i in range(max(n,m)):
            if i < n:
                new_string.append(word1[i])
            if i < m:
                new_string.append(word2[i])
        return "".join(new_string)