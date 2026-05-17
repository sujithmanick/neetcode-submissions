class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hash_map = {}
        max_len = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] in hash_map:
                if l <= hash_map[s[r]]:
                    l = hash_map[s[r]] + 1

            hash_map[s[r]] = r
            max_len = max(max_len, r - l + 1)
                
            r += 1
            
        return max_len

