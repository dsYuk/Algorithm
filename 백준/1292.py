a, b = map(int, input().split())

t = []

for i in range(1, 46): # 46번째까지 반복해서 실행하게 되면  1000을 넘는 최소가 됨
    t += [i] * i

print(sum(t[a-1 : b]))