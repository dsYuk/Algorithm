import sys

N = int(sys.stdin.readline())

stack = []

def push(n):
    stack.append(n)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

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
    elif order == 'top':
        print(top())