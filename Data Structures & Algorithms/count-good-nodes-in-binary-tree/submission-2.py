# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good_node = 0
        stack = [(root, root.val)]

        while stack:
            sub_list = []
            node, mx_val = stack.pop()

            if node.val >= mx_val:
                good_node += 1 
            mx_val = max(node.val, mx_val)

                
            if node.left:
                stack.append((node.left, mx_val))
            if node.right:
                stack.append((node.right, mx_val))
        return good_node
            