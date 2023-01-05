N = int(input())

A = list(map(int, input().split()))

X = int(input())

A_map = {}

result = []

for i, j in enumerate(A):
    A_map[j] = i

for i, j in enumerate(A):
    if X - j in A_map and i != A_map[X - j]:
        result.append(A_map[X - j])

print(int(len(result) / 2))