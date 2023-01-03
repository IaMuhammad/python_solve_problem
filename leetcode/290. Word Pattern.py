def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()
    if len(pattern) != len(s):
        return False
    d_p, d_s = {}, {}
    ans = ''

    for i, v in enumerate(pattern):
        if d_p.get(v, False):
            if d_p[v] != s[i]:
                return False
        else:
            if d_s.get(s[i], False) and d_s[s[i]] != v:
                return False
            d_s[s[i]] = v
            d_p[v] = s[i]
    return True
