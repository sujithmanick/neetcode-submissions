class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set = [0] * 26

        for i in s:
            hash_set[ord(i) - ord('a')] += 1

        for j in range(len(t)):
            hash_set[ord(t[j]) - ord('a')] -= 1

        if hash_set != [0]*26:
            return False
        return True