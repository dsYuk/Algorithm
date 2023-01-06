def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
            # print(stack)
        elif stack[-1] == i:
            stack.pop()
            # print(stack)
        else:
            stack.append(i)
            # print(stack)
    if len(stack) == 0:
        return 1
    else:
        return 0