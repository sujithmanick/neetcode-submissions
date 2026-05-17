class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += f"{len(string)}~{string}"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        left = 0
        while left < len(s):
            right= left
            while s[right] != '~':
                right+=1
            length = int(s[left:right])
            decoded_string.append(s[right+1 : right+1+length])
            left=right+1+length
        return decoded_string