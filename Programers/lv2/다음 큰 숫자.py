def solution(n):
    answer = n + 1

    while 1:
        if format(n, 'b').count('1') == format(answer, 'b').count('1'):
            return answer
        answer += 1