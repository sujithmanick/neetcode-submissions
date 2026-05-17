class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""

        for i in strs:
            str1 += f"{len(i)}#{i}"

        return str1

    def decode(self, s: str) -> List[str]:
        res =[]
        i = 0



        while i < len(s):
            j = i
            
            while s[j] != '#':
                j+=1
            
            ln = int(s[i:j])

            j = j+1

            res.append(s[j:j+ln])

            i= j+ln
        return res
