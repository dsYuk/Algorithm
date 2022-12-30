def solution(x):
    answer = True
    a = 0
    N = list(str(x))
    for i in N:
        a += int(i)
    return a
    if x % a == 0:
        answer = True
    else:
        answer = False