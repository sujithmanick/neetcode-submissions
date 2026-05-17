"""
# Definition for a Node. """
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_data = {None:None}
        h1 = head
        while h1:
            hash_data[h1] = Node(h1.val)
            h1 = h1.next

        current = head
        while current:
            hash_data[current].next = hash_data.get(current.next)
            hash_data[current].random = hash_data.get(current.random)
            current = current.next
        return hash_data[head]





