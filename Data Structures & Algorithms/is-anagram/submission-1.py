class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = [0] * 26
        for i in s:
            hash_map[ord(i) - ord('a')] += 1

        for i in t:
            hash_map[ord(i) - ord('a')] -= 1

        if [0]*26 == hash_map:
            return True
        return False