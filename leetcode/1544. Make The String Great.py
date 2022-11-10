def makeGood(s: str) -> str:
    stack = [s[0]]
    s, i = list(s), 1
    while i < len(s):
        if stack:
            if abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop(-1)
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
        i += 1
    return ''.join(stack)
print(makeGood('Pp'))
print(ord('B') - ord('b'))