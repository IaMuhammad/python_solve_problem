def diStringMatch(self, s: str) -> list[int]:
    ans = []
    l = 0
    r = len(s)
    i = 0
    while l < r:
        if s[i] == 'I':
            ans.append(l)
            l += 1
        else:
            ans.append(r)
            r -= 1
        i += 1
    ans.append(l)
    return ans

def di_string_match_recur(s: str):
    if not s:

