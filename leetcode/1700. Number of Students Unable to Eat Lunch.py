from typing import List, Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counted_data = Counter(students)
        for i in sandwiches:
            if counted_data[i]:
                counted_data[i] -= 1
            else:
                break
        return counted_data[0] + counted_data[1]

a = Solution()
print(a.countStudents([1,1,0,0], [0,1,0,1]))