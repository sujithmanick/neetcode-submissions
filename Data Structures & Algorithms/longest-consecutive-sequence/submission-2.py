class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_seq = -999999
        for i in nums:
            count = 1
            while i - count in nums:
                count += 1
            max_seq = max(max_seq, count)
        return max_seq