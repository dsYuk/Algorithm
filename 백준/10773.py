K = int(input())
stack = []

for i in range(K):
    k = int(input())
    if k == 0:
        stack.pop()
    else:
        stack.append(k)
print((sum(stack)))