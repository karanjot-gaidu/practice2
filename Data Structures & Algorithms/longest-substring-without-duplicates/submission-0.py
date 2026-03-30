class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub_len = 0
        substr_set = set()
        for r in range(len(s)):
            while s[r] in substr_set:
                substr_set.remove(s[l])
                l += 1
            substr_set.add(s[r])
            sub_len = max(sub_len, len(substr_set))
        return sub_len
