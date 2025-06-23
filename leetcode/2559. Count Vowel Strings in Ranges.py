from typing import List


class Solution:
    def vowel_count(self, s):
        if s[0] in 'aeiou' and s[-1] in 'aeiou':
            return 1
        return 0

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        counted_data = [0]
        for i, v in enumerate(words):
            counted_data.append(self.vowel_count(v) + counted_data[-1])
        return [(counted_data[r+1] - counted_data[l]) for l, r in queries]


a = Solution()
# words = ['aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', ]
# queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# print(a.vowelStrings(words, queries))
print(a.vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]))
words = [
    "bzmxvzjxfddcuznspdcbwiojiqf",
    "mwguoaskvramwgiweogzulcinycosovozppl",
    "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs",
    "uivcdsboxnraqpokjzaayedf",
    "yalc",
    "bbhlbmpskgxmxosft",
    "vigplemkoni",
    "krdrlctodtmprpxwditvcps",
    "gqjwokkskrb",
    "bslxxpabivbvzkozzvdaykaatzrpe",
    "qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi",
    "siqbezhkohmgbenbkikcxmvz",
    "ddmaireeouzcvffkcohxus",
    "kjzguljbwsxlrd",
    "gqzuqcljvcpmoqlnrxvzqwoyas",
    "vadguvpsubcwbfbaviedr",
    "nxnorutztxfnpvmukpwuraen",
    "imgvujjeygsiymdxp",
    "rdzkpk",
    "cuap",
    "qcojjumwp",
    "pyqzshwykhtyzdwzakjejqyxbganow",
    "cvxuskhcloxykcu",
    "ul",
    "axzscbjajazvbxffrydajapweci"
]
queries = [[4, 4], [6, 17], [10, 17], [9, 18], [17, 22], [5, 23], [2, 5], [17, 21], [5, 17], [4, 8], [7, 17], [16, 19],
           [7, 12], [9, 20], [13, 23], [1, 5], [19, 19]]
print(a.vowelStrings(words, queries))
