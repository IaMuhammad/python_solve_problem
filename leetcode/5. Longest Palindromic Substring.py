from collections import Counter


class Solution(object):
    def get_indexes(self, s):
        indexes = {}
        for i, v in enumerate(s):
            if indexes.get(v):
                indexes[v].append(i)
            else:
                indexes[v] = [i]
        return indexes

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        indexes = self.get_indexes(s)
        print(indexes)


a = Solution()
a.longestPalindrome('bacadda')
