class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totallen = len(nums1) + len(nums2)
        half = totallen // 2

        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a

        l = 0
        r = len(a) - 1

        while True:
            a_mid = (l + r) // 2
            b_mid = half - a_mid - 2

            a_l = a[a_mid]  if a_mid >= 0 else float("-inf")
            a_r = a[a_mid + 1] if a_mid + 1 < len(a) else float("inf")

            b_l = b[b_mid] if b_mid >= 0 else float("-inf")
            b_r = b[b_mid + 1] if b_mid +1 < len(b) else float("inf")


            if a_l <= b_r and b_l <= a_r:
                if totallen % 2  != 0:
                    return min(a_r, b_r)
                else:
                    return (max(a_l, b_l) + min(a_r, b_r)) / 2
            elif a_l > b_r:
                r = a_mid - 1
            else:
                l = a_mid + 1

                