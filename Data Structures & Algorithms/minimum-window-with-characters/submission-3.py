class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "" or len(s) < len(t):
            return ""

        l = 0
        t_map = {}
        for i in t:
            t_map[i] = 1 + t_map.get(i, 0)

        have = 0
        required = len(t_map)
        rlen = float("inf")
        res = [-1,-1]
        
        window = {}
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)

            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
                have += 1

            while have == required:
                if rlen > (r - l + 1):
                    rlen = (r - l + 1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
            r+=1
        l,r = res
        return s[l:r+1] if rlen != float("inf") else ""

                    

