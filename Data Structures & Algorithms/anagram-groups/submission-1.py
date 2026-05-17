class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_dict = defaultdict(list)

        for i in strs:
            temp = [0] * 26
            for k in i:
                temp[ord(k) - ord('a')] += 1
            st_key = tuple(temp)
            hash_dict[st_key].append(i)

        return list(hash_dict.values())