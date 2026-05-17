class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for number in nums:
            if number not in hash_map.keys():
                hash_map[number] = 1
            else:
                hash_map[number] += 1
        
        bucket_sorting = [ [] for _ in range(len(nums) + 1)]

        for number, count in hash_map.items():
            bucket_sorting[count].append(number)

        result = []
        for m in bucket_sorting[::-1]:
            for n in m:
                result.append(n)
                if len(result) == k:
                    return result

