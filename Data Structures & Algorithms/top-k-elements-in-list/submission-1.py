class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for i in nums:
            hash_map[i] = 1 + hash_map.get(i, 0)

        bucket = [ [] for i in range(len(nums)) ]

        for number, count in hash_map.items():
            bucket[count-1].append(number)

        res, count = [], 0
        for i in range(len(bucket)-1,-1,-1):
            while bucket[i]:
                if count == k:
                    break
                res.append(bucket[i].pop())
                count += 1
                
        return res

