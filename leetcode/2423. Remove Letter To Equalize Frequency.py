from collections import Counter


# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         counted_data = Counter(word)
#         values = counted_data.values()
#         first = second = None
#         for i in values:
#             if first is None:
#                 first = i
#             elif second is None and i != first:
#                 second = i
#             else:
#                 if i not in (first, second):
#                     return False
#         counted_values = Counter(values)
#         if len(counted_values) == 1:
#             return True if counted_values[1] else False
#         min_, max_ = sorted(counted_values.values())
#         if min_ == 1 and max_ == 2:
#             return True
#         return False
class Solution:
    def check(self, word):
        return len(set(Counter(word).values())) == 1

    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            if self.check(word[:i] + word[i+1:]):
                return True
        return False
class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            n=word[:i]+word[i+1:]
            d={}
            for i in n:
                d[i]=d.get(i,0)+1
            if len(set(d.values()))==1:
                return True
        return False
a = Solution()
# print("aca ", a.equalFrequency("aca") == True)
# print("ddaccb ", a.equalFrequency("ddaccb") == False)
# print("abcc ", a.equalFrequency("abcc") == True)
# print("aazz ", a.equalFrequency("aazz") == False)
# print("ac ", a.equalFrequency("ac") == True)
print("aaccc ", a.equalFrequency("aaccc") == False)
print("abbccc ", a.equalFrequency("abbccc") == False)
print("abbcbcc ", a.equalFrequency("abbcbcc") == True)
print("ababcbcc ", a.equalFrequency("ababcbcc") == True)
