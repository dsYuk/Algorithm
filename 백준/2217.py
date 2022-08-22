n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
m.sort()

answers = []
for j in m:
    answers.append(j * n)
    n -= 1
print(max(answers))