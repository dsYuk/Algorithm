def solution(a, b, n):
    answer = 0
    while n >= a:
        left = n % a
        n = n // a * b
        answer += n
        n  += left
    return answer