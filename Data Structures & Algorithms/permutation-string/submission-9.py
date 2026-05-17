class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash_set = [0] * 26
        hash_set2 = [0] * 26
        a = ord('a')
        for i in s1:
            hash_set[ord(i) - a] += 1

        for j in range(len(s1)):
            hash_set2[ord(s2[j]) - a] += 1

        if hash_set2 == hash_set:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            hash_set2[ord(s2[l]) - a] -= 1
            l += 1
            hash_set2[ord(s2[r]) - a] += 1

            if hash_set2 == hash_set:
                return True
        return False



        
