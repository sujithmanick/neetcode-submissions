class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                break
            elif matrix[mid][-1] > target:
                r = mid - 1
            else:
                l = mid + 1

        left_sub = 0
        right_sub = len(matrix[mid]) -1
        while left_sub <= right_sub:
            sub_mid = (left_sub + right_sub) // 2

            if matrix[mid][sub_mid] == target:
                return True
            elif matrix[mid][sub_mid] > target:
                right_sub = sub_mid - 1
            else:
                left_sub = sub_mid + 1

        return False