class MyHashSet:

    def __init__(self):
        self.d = {}

    def add(self, key: int) -> None:
        if not self.d.get(key):
            self.d = {
                key
            }


    def remove(self, key: int) -> None:
        pass

    def contains(self, key: int) -> bool:
        pass
