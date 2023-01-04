N = int(input())

answer = 0

for i in range(1, N + 1):
    n = list(map(int, str(i)))
    if i < 100:
        answer += 1
    elif n[2] - n[1] == n[1] - n[0]:
        answer += 1

print(answer)