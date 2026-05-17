class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        
        total = len(num1) + len(num2)
        half = (len(num1) + len(num2)) // 2

        if len(num1) > len(num2):
            num1, num2 = num2, num1

        l = 0
        r = len(num1) - 1
        while True:
            mid = (l + r) // 2
            rem_nums = half - mid - 2

            l1 = num1[mid] if mid >= 0 else float("-inf")
            r1 = num1[mid+1] if mid+1 < len(num1) else float("inf")

            l2 = num2[rem_nums] if rem_nums >= 0 else float("-inf")
            r2 = num2[rem_nums+1] if rem_nums+1 < len(num2) else float("inf")

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1,l2) + min(r1,r2)) / 2
                else:
                    return min(r1,r2)
            elif l1 > r2:
                r = mid - 1
            else:
                l = mid + 1




