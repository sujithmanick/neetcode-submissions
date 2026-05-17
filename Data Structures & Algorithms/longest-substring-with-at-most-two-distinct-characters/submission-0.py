from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hash_set = {}
        seen = set()
        l = 0
        max_len = 0
        for r, v in enumerate(s):
            seen.add(v)
            hash_set[v] = 1 + hash_set.get(v,0)
            while len(seen) > 2:
                hash_set[s[l]] -= 1
                if hash_set[s[l]] == 0:
                    hash_set.pop(s[l])
                    seen.remove(s[l])
                l += 1
                
            max_len = max(max_len, ((r - l)+1))

        return max_len
                

       