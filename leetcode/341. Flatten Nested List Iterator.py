class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self.value = []
        else:
            self.value = value

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.value, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        if self.isInteger():
            return self.value
        else:
            return None

    def getList(self) -> list['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        if not self.isInteger():
            return self.value
        else:
            return None

    def __str__(self):
        if self.isInteger():
            return str(self.value)
        else:
            return "[" + ",".join(str(ni) for ni in self.value) + "]"


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.current = None

    def next(self) -> int:
        if self.hasNext():
            pass
        pass

    def hasNext(self) -> bool:
        if len(self.nestedList.value) != 1:
            return True
        return False


def build_nested_integer(data):
    if isinstance(data, int):
        return NestedInteger(data)
    elif isinstance(data, list):
        nested = NestedInteger()
        for item in data:
            nested.getList().append(build_nested_integer(item))
        return nested


a = [[1, 2], 3, 4, [5, [6]]]
nested = build_nested_integer(a)
answer = NestedIterator(nested)
print(answer.next())
