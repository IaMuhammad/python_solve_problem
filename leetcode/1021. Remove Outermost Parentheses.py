def removeOuterParentheses(s: str) -> str:
    stack, answer = [], []
    for i in s:
        if i == '(':
            if stack:
                answer.append(i)
            stack.append(i)
        else:
            stack.pop()
            if stack:
                answer.append(i)
    return ''.join(answer)
    pass


def solve(s):
    stack, cache = '', ''
    c1 = 0
    for i in s:
        if cache != '(':
            if i == '(' and (not stack or stack[-1] == ')'):
                cache = '('

        elif c1 == 0 and i == ')' and (not stack or stack[-1] == ')'):
            cache = ')'
        elif i == '(':
            c1 += 1
            stack += i
        else:
            c1 -= 1
            stack += i
    return stack
print(removeOuterParentheses('()(())'))