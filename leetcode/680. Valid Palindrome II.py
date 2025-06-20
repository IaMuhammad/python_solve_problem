# def validPalindrome(s: str) -> bool:
#     l, r, c = 0, len(s) - 1, 0
#     while l <= r:
#         ls, rs = s[l], s[r]
#         if s[l] == s[r]:
#             l += 1
#             r -= 1
#         elif not c:
#             return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
#
#     return True

# print(validPalindrome("ebcbbececabbacecbbcbe"))


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        _left, _right = 0, 0
        _ = 0
        while left < right:
            if s[left] != s[right]:
                if _ == 0:
                    if s[left + 1] == s[right]:
                        _left, _right = left, right
                        left += 1
                        _ = -1
                    elif s[left] == s[right - 1]:
                        _left, _right = left, right
                        right -= 1
                        _ = 1
                    else:
                        return False
                elif _ == -1:
                    left, right = _left, _right
                    right -= 1
                    _ = 2
                elif _ == 1:
                    left, right = _left, _right
                    left += 1
                    _ = 2
                else:
                    return False
            left += 1
            right -= 1
        return True


a = Solution()
print(a.validPalindrome("axbcbaba"))
# print(a.validPalindrome("abc"))
# print(a.validPalindrome("lcuppucul"))
# print(a.validPalindrome("avca"))
print(a.validPalindrome("lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul"))
print("lcupuufxoohd"[::-1])
