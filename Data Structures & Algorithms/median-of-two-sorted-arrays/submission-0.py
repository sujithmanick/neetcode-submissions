class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totallen = len(nums1) + len(nums2)
        half = totallen // 2

        min_arr, max_arr = (nums1, nums2) 
        if len(nums1) > len(nums2):
            min_arr, max_arr = (nums2, nums1)

        l = 0
        r = len(min_arr) - 1 

        while True:
            mid = (l + r) // 2
            j = half - mid - 2
            l1 = min_arr[mid] if mid >= 0 else float("-inf")
            l2 = max_arr[j] if j >= 0 else float("-inf") 

            
            r1 = min_arr[mid + 1] if mid + 1 < len(min_arr) else float("inf")
            r2 = max_arr[j + 1] if j + 1 < len(max_arr)  else float("inf")

            if l1 <= r2 and l2 <= r1:
                if totallen % 2 :
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = mid - 1
            else:
                l = mid + 1

                    

