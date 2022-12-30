def solution(s):
    s_u = s.upper()
    p = s_u.count('P')
    y = s_u.count('Y')
    py = p + y
    if p == y:
        answer = True
    elif p != y:
        answer = False
    elif py == 0:
        answer = True
    return answer