import string


def greatestLetter(s: str) -> str:
        d = {}
        ans = ''
        for i in s:
                up = i.upper()
                lw = i.lower()
                if i.isupper():
                        if d.get(i):
                                ans = max(ans, lw)
                        else:
                                d[lw] = True
                else:
                        if d.get(i):
                                ans = max(ans, up)
                        else:
                                d[up] = True
        return ans
print(string.ascii_lowercase)