import sys

N = int(sys.stdin.readline())

result = []

def push(x):
    result.append(x)

def pop():
    if len(result) == 0:
        return -1
    return result.pop(0)

def size():
    return len(result)

def empty():
    if len(result) == 0:
        return 1
    return 0

def front():
    if len(result) == 0:
        return -1
    return result[0]

def back():
    if len(result) == 0:
        return -1
    return result[-1]

for i in range(N):
    n = sys.stdin.readline().split()
    order = n[0]
    if order == 'push':
        push(n[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())