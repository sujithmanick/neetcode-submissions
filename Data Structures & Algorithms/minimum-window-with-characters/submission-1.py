class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or s == "" or t == "":
            return ""

        t_map = {}
        for i in t:
            t_map[i] = 1 + t_map.get(i,0)

        l = 0
        req_char = len(t_map)
        res = [-1,-1]
        rlen = float("infinity")
        window = {}
        have = 0

        for r, c in enumerate(s):
            window[c] = window.get(c,0) + 1

            if c in t_map and window[c] == t_map[c]:
                have += 1

            while have == req_char:
                if rlen > (r-l+1):
                    rlen = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in t_map and t_map[s[l]] > window[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        return s[l:r+1] if rlen != float("infinity") else ""





