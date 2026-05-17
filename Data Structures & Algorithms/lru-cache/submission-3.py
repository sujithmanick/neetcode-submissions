from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = OrderedDict()
        

    def get(self, key: int) -> int:
        data = self.hash_map.get(key, -1)
        if data == -1:
            return -1
        self.hash_map.move_to_end(key)
        return data
        

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value
        self.hash_map.move_to_end(key)

        if len(self.hash_map) > self.capacity:
            self.hash_map.popitem(last = False)
        return None
            
        
