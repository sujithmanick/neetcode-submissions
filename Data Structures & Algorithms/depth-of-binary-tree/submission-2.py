# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        mxdepth = 0

        def dfs(root, depth):
            nonlocal mxdepth
            if not root:
                return 0
            
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)

            mxdepth = max(mxdepth, max(left, right) + 1)

            return max(left, right) + 1

        dfs(root, mxdepth)
        return mxdepth


            
