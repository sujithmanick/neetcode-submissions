# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        level = []
        while q:
            sub_level = []

            for i in range(len(q)):
                data = q.popleft()
                if data:
                    sub_level.append(data.val)
                    if data.left:
                        q.append(data.left)
                    if data.right:
                        q.append(data.right)

            level.append(sub_level)
        
        return level

        