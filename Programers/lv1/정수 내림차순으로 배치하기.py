def solution(n):
    a = str(n)
    answer = int(''.join(sorted(a, reverse = True)))
    return answer