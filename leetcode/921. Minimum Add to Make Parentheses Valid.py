def minAddToMakeValid(s: str) -> int:
    stack = []
    for i in s:
        if stack:
            if stack[-1] == '(' and i == ')':
                stack.pop(-1)
            else:
                stack.append(i)
        else:
            stack.append(i)
    return len(stack)
print(minAddToMakeValid('(())))'))