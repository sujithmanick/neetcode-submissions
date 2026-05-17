class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_set = {}

        l = 0
        ln=0
        for r in range(len(s)):
            if s[r] not in hash_set:
                hash_set[s[r]] = 1
            else:
                hash_set[s[r]] += 1

            max_occ_elements = max(hash_set.values())

            while l < r and ((r - l + 1) - max_occ_elements) > k:
                if hash_set[s[l]] > 0:
                    hash_set[s[l]] -= 1
                else:
                    hash_set.pop(s[l])
                l+=1

            ln = max(ln, (r - l + 1))
        return ln
            