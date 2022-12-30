def solution(x, n):
    answer = []
    for i in range(n):
        a = x + x * i
        answer.append(a)
    return answer