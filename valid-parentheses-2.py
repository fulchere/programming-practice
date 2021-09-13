def isValid(s):
    stack = []
    op = "({["
    close = ")}]"

    for ch in s:
        if ch in op:
            stack.append(ch)
        if ch in close:
            if stack and op.index(stack[-1]) == close.index(ch):
                stack.pop()
            else:
                return False

    return False if stack else True


for s in ["()", "()[]{}", "(]", "([)]", "{[]}"]:
    print(isValid(s))
