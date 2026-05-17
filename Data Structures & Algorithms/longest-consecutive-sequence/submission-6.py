class Solution:
    def longestConsecutive(self, nums):
        count = 0
        st = set(nums)
        for i in st:
            if i + 1 not in st:
                sub_count = 1
                sub_i = i
                while sub_i - 1 in st:
                    sub_count += 1
                    sub_i -= 1
                
                count = max(count, sub_count)
        return count