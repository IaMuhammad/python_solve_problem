class MyCalendar:

    def __init__(self):
        self.books = []

    # def binary_search(self, se):

    #     if high >= low:

    #         mid = (high + low) // 2

    #         if arr[mid] == x:
    #             return mid

    #         elif arr[mid] > x:
    #             return binary_search(arr, low, mid - 1, x)

    #         else:
    #             return binary_search(arr, mid + 1, high, x)

    #     else:

    def book(self, start: int, end: int) -> bool:
        for l, r in self.books:
            if l < end and r > start:
                return False
        self.books.add((start, end))
        return True
    def __str__(self):
        return f'{self.books}'

a = MyCalendar()
print(a.book(47, 50))
print(a.book(33, 41))
print(a.book(39, 45))
print(a.book(33, 42))
print(a.book(25, 32))
print(a.book(26, 35))
print(a.book(19, 35))
# [47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]