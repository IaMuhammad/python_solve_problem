def isValid(s: str) -> bool:
    stack = []
    if len(s) == 1:
        return False
    d = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    for i in s:
        if i in '([{':
            stack.append(i)
        elif not stack:
            return False
        else:
            if d.get(stack[-1]) == i:
                del stack[-1]
            else:
                return False
    if stack:
        return False
    return True

print(isValid('()'))