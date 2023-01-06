N, K = map(int, input().split()) 
arr = [i for i in range(1, N + 1)]
result = []
n = 0

for i in range(N):
    n += K - 1
    if n >= len(arr):
        n %= len(arr)
    result.append(arr.pop(n))

print("<", ", ".join(str(i) for i in result), ">", sep='')