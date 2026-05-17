class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hash_set = {}
        max_freq = 0
        ln = 0
        for r in range(len(s)):
            hash_set[s[r]] = hash_set.get(s[r], 0) + 1

            max_freq = max(max_freq, hash_set[s[r]])

            while (r - l + 1) - max_freq > k:
                hash_set[s[l]] -= 1
                l+= 1
            
            ln= max(ln, (r - l + 1))
        return ln
