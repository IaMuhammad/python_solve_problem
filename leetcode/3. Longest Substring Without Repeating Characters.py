class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length, substr = [0], ''
        for i in s:
            if i in substr:
                substr = substr[substr.index(i)+1:] + i
                length.append(len(substr))
            else:
                substr += i
                length[-1] += 1
        return max(length)
a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))