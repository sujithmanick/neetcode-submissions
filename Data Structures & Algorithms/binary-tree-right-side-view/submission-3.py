# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        
        if not root:
            return res

        while q:
            rightmost = q[-1]
            res.append(rightmost.val)

            for i in range(len(q)):
                data = q.popleft()
                if data.left:
                    q.append(data.left)
                if data.right:
                    q.append(data.right)

        return res