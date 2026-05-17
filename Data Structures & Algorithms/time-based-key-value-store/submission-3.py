class TimeMap:

    def __init__(self):
        self.hash_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map.keys():
            self.hash_map[key] = [(value, timestamp)]
        else:
            self.hash_map[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        data = self.hash_map.get(key, [])

        if not data:
            return ""

        l = 0
        r = len(data) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if data[mid][1] <= timestamp:
                res = data[mid][0]   
                l = mid + 1          
            else:
                r = mid - 1

        return res


            
        
