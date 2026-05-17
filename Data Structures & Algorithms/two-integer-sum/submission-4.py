class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums = sorted(nums)

        hash_set = {}

        for i in range(len(nums)):
            if nums[i] in hash_set:
                return [hash_set[nums[i]], i]
            hash_set[target - nums[i]] = i
