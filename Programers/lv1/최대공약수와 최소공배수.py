def solution(n, m):
    answer = []
    for i in range(n, 0, -1):
        if (n % i == 0) and (m % i == 0):
            answer.append(i)
            break
    for i in range(m, n*m+1):
        if (i % n == 0) and (i % m == 0):
            answer.append(i)
            break
    return answer