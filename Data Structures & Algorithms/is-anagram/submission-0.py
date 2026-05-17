class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_frequency, t_frequency = {}, {}
        if s_len != t_len:
            return False
        for index in range(s_len):
            s_frequency.setdefault(s[index], 0)
            s_frequency[s[index]] += 1

            t_frequency.setdefault(t[index], 0)
            t_frequency[t[index]] += 1
        if s_frequency == t_frequency:
            return True
        return False