class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash_map, window = [0]*26, [0]*26
        m,n = len(s1), len(s2)
        if m>n:
            return False
        for i in s1:
            s1_hash_map[ord(i) - ord('a')] += 1

        for j in range(m):
            window[ord(s2[j]) - ord('a')] += 1

        if s1_hash_map == window:
            return True

        for i in range(m, n):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i-m]) - ord('a')] -= 1
            if s1_hash_map == window:
                return True
        return False
