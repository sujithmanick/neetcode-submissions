class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        visited = []
        for i in nums:
            if i not in visited:
                bucket[nums.count(i)].append(i)
                visited.append(i)
        res = []
        count = 0
        for i in range(len(bucket) -1, -1, -1):
            while bucket[i]:
                if count == k:
                    break
                res.append(bucket[i].pop())
                count+=1

        return res
                


