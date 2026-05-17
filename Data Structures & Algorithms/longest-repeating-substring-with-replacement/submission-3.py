class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        hash_set = {}
        l = 0
        max_count = 0
        for r in range(len(s)):
            if s[r] not in hash_set.keys():
                hash_set[s[r]] = 1
            else:
                hash_set[s[r]] += 1

            max_count = max(max_count, hash_set[s[r]])

            while l < r and ((r - l + 1) - max_count) > k:
                hash_set[s[l]] -= 1
                l += 1


            result = max(result, r - l + 1)
        return result