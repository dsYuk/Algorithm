def solution(s):
    answer = 0
    if s.count('(') != s.count(')'):
        return False

    for i in s:
        if i == '(':
            answer += 1
        else:
            answer -= 1

        if answer < 0:
            # ')'이 먼저 나오면 False
            return False

    return True