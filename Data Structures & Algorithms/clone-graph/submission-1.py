
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

import copy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldto_new = {}

        def clone(node):
            if node in oldto_new:
                return oldto_new[node]

            copy = Node(node.val)
            oldto_new[node] = copy
            for nbs in node.neighbors:
                copy.neighbors.append(clone(nbs))
            
            return copy

        return clone(node) if node else None