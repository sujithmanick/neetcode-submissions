class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hash_set = {}
        max_len = 0
        for r in range(len(s)):
            if s[r] not in hash_set:
                hash_set[s[r]] = r
            else:
                if l <= hash_set[s[r]]:
                    l = hash_set[s[r]] + 1
                hash_set[s[r]] = r
            max_len = max(max_len, r - l + 1)
        return max_len