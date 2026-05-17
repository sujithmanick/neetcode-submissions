class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_hash = {}
        for index, value in enumerate(nums):
            if value in difference_hash:
                return [difference_hash[value], index]
            difference_hash[target - value] = index