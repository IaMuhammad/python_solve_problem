from typing import List, Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        data = Counter(words[0])
        for word in words[1:]:
            if not data:
                return []
            _counter = Counter(word)
            _data = {}
            for k, v in data.items():
                if _counter[k]:
                    _data[k] = min(_counter[k], v)
            data = _data
        answer = []
        for k, v in data.items():
            answer += [k] * v
        return answer

    # def commonChars(self, words: List[str]) -> List[str]:
    #     data = Counter(words[0])
    #     for word in words[1:]:
    #         data &= Counter(word)  # intersect: keeps min count per char
    #     return list(data.elements())


a = Solution()
print(a.commonChars(["bella", "label", "roller"]))
