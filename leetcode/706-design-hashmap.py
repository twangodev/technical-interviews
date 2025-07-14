class MyHashMap:

    def __init__(self):
        self.backing = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.backing[key] = value

    def get(self, key: int) -> int:
        result = self.backing[key]
        return result if result is not None else -1

    def remove(self, key: int) -> None:
        self.backing[key] = None



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)