from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counted_data = Counter(word)
        return