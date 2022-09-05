n = int(input())

for i in range(n):
    x = list(map(int, input().split()))
    x.sort()
    print(x[7])