from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupped_strs = defaultdict(list)

        for string in strs:
            hash_list = [0] * 26
        
            for char in string:
                hash_list[ord(char) - ord('a')] += 1
            
            groupped_strs[tuple(hash_list)].append(string)

        return list(groupped_strs.values())