class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.generate(nums, 0)
        return self.res

    def generate(self, nums, idx):
        if idx == len(nums):
            self.res.append(nums.copy())
            return

        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.generate(nums, idx+1)
            nums[idx], nums[i] = nums[i], nums[idx]