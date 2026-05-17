# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf') 
        def dfs(root):
            
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal max_sum
            max_sum = max(max_sum, (root.val + max(left,0) + max(right,0)))

            return root.val + max(max(left,0), max(right,0))

            
        
        dfs(root)
        return max_sum

        