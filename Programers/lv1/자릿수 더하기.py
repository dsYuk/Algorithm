def solution(n):
    answer = 0
    N = list(str(n))
    for i in N:
        answer += int(i)
    return answer