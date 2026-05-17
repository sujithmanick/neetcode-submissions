class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from itertools import permutations

        perm = permutations(s1)
        for i in perm:
            if "".join(i) in s2:
                return True

        return False