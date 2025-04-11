class Solution(object):
    def checkStrs(self, new, pre):
        i = 0
        while i < min(len(new), len(pre)):
            if new[i] != pre[i]:
                return pre[:i]
            i += 1
        else:
            if len(new) < len(pre):
                return new[:i]
            elif len(pre) < len(new):
                return pre[:i]
        return pre

    def longestCommonPrefix(self, strs):
        answer = strs[0]
        for i in strs[1:]:
            answer = self.checkStrs(i, answer)
        return answer


class Solution2(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        shortest_string: str = min(strs, key=len)
        for i, v in enumerate(shortest_string):
            for other_words in strs:
                if other_words[i] != v:
                    return shortest_string[:i]
        return shortest_string


a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
print(a.longestCommonPrefix(["do", "d"]))
