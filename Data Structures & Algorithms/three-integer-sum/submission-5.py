class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, v in enumerate(nums):

            if v > 0:
                break
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum_ = nums[l] + nums[r] + v
                if sum_ < 0:
                    l+=1
                elif sum_ > 0:
                    r-=1
                else:
                    res.append([v, nums[l], nums[r]])

                    l+=1
                    r-=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
        return res