class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_length = 0
        for i in nums:
            if i-1 not in hash_set:
                length=1
                while i+length in hash_set:
                    length+=1
                max_length = max(length, max_length)
        return max_length