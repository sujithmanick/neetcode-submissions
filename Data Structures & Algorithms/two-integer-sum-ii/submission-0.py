class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        summ = numbers[left] + numbers[right]
        while summ != target and left < right:
            
            if summ < target:
                left += 1
            else:
                right -= 1
            summ = numbers[left] + numbers[right] 
        return [left+1, right+1]