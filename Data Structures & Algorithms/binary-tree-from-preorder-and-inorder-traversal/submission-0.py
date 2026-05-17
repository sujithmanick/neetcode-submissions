# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = { v:i for i, v in enumerate(inorder) }

        pre_i = 0


        def helper(left, right):
            nonlocal pre_i
            if left > right:
                return None

            root = TreeNode(val=preorder[pre_i])
            


            idx = inorder_idx[preorder[pre_i]]
            pre_i += 1
            root.left = helper(left, idx-1)
            root.right = helper(idx+1, right)

            return root




            
        return helper(0, len(inorder_idx) -1)