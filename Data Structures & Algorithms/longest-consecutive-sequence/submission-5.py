class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            sub_count = 1
            sub_i = i
            while sub_i - 1 in nums:
                sub_count += 1
                sub_i -= 1
            
            count = max(count, sub_count)
        return count