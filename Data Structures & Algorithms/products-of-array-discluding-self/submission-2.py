class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pfx = [1]
        for i in range(len(nums)-1):
            pfx.append(pfx[-1] * nums[i])


        pofx = [1]
        for i in range(len(nums)-1, 0,-1):
            pofx.insert(0,pofx[0] * nums[i])


        res = []
        for i in range(len(nums)):
            res.append(pfx[i] * pofx[i])
        
        return res
