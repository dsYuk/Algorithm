num = 0
result = 0

for _ in range(10):
    o, i = list(map(int, input().split()))
    num += (i - o)
    result = max(num, result)

print(result)