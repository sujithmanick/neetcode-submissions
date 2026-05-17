# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced_ = True
        def dfs(root):
            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if left_height - right_height not in [-1, 0, 1]:
                self.isBalanced_  =False


            return max(left_height, right_height) + 1

        dfs(root)
        return self.isBalanced_

        