class Node:
    def __init__(self, key = None, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

        self.hash_dict = {}

    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev

        return True

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next, nxt.prev = node, node

        node.next = nxt
        node.prev = prev

        return True
        

    def get(self, key: int) -> int:
        data_node = self.hash_dict.get(key, -1)
        if data_node == -1:
            return -1
        self.remove(data_node)
        self.insert(data_node)
        return data_node.val
        

    def put(self, key: int, value: int) -> None:



        data_node = self.hash_dict.get(key, -1)
        if data_node != -1:
            self.remove(data_node)
        


        node = Node(key, value)


        self.hash_dict[key] = node
        self.insert(node)


        if len(self.hash_dict) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hash_dict[lru.key]
        return None
            
        
