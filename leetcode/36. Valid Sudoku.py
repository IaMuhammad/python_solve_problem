from collections import Counter
from typing import List


class Solution:
    def check_row(self, board):
        for row in board:
            counted_data = Counter(row)
            for k, v in counted_data.items():
                if v > 1 and k != '.':
                    return False
        return True

    def check_col(self, board):
        for i in range(len(board)):
            counted_data = Counter([j[i] for j in board])
            for k, v in counted_data.items():
                if v > 1 and k != '.':
                    return False

        return True

    def check_box(self, board):
        for i in range(3):
            a = [row[i * 3:i * 3 + 3] for row in board]
            _ = []
            for index, value in enumerate([row[i * 3:i * 3 + 3] for row in board]):
                if index % 3 == 2:
                    if not self.check_row([_ + value]):
                        return False
                    _ = []
                else:
                    _ += value
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.check_row(board):
            return False
        if not self.check_col(board):
            return False
        if not self.check_box(board):
            return False
        return True


a = Solution()
print(a.isValidSudoku([
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
