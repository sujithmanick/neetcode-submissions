class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash_set = [0] * 26
        window = [0] * 26
        ln_s1 = len(s1)
        ln_s2 = len(s2)
        if ln_s1 > ln_s2:
            return False
        for i in s1:
            s1_hash_set[ord(i) - ord('a')] += 1


        for j in range(ln_s1):
            window[ord(s2[j]) - ord('a')] += 1

        if s1_hash_set == window:
            return True

        for k in range(ln_s1, ln_s2):
            window[ord(s2[k - ln_s1]) - ord('a')] -= 1
            window[ord(s2[k]) - ord('a')] += 1
            if s1_hash_set == window:
                return True
        return False

        
