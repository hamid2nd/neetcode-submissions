class MyHashMap:

    def __init__(self):
        self.h = {}

    def put(self, key: int, value: int) -> None:
        self.h[key] = value 

    def get(self, key: int) -> int:
        x = self.h.get(key, -1)
        return x

    def remove(self, key: int) -> None:
        check = key in self.h
        if check == True: 
            del self.h[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)