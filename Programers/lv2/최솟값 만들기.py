def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    s = []

    for i in range(len(A)):
        s.append(A[i] * B[i])

    answer = sum(s)
    return answer