class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums= sorted(nums)
        result= []
        for i , val in enumerate(nums):
            left= i + 1
            right= len(nums)-1
            while right > left and i < len(nums)-1:
                _sum =  val + nums[left] + nums[right]
                if _sum < 0:
                    left+= 1
                elif _sum > 0:
                    right -=1
                else:
                    data = [val, nums[left], nums[right]]
                    result.append(data) if data not in result else []
                    left += 1
        return result

            
                