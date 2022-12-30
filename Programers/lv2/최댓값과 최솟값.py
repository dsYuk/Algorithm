def solution(s):
    answer = ''
    s = s.split()
    int_s = list(map(int, s))
    answer = str(min(int_s)) + ' ' + str(max(int_s))
    return answer