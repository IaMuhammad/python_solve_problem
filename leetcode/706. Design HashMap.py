class MyHashMap:

    def __init__(self):
        self.d = {}

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        return self.d.get(key, -1)

    def remove(self, key: int) -> None:
        if self.get(key) != -1:
            self.d.pop(key)

    def __repr__(self):
        return f'{self.d}'

my = MyHashMap()
my.put(1,2)
my.remove(2)
print(my.get(2))