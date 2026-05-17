class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]',"", s).lower()
        l = 0
        r = len(s) -1

        while l < r:
            if s[l] != " " and s[r] != " ":
                if s[l] != s[r]:
                    return False

            l+=1
            r-=1
        return True