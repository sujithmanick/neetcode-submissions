class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = []
        for i in nums:
            if i in storage:
                return True
            storage.append(i)
        return False