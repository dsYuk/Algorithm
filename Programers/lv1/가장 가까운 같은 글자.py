def solution(s):
    answer = []
    s_list = []
    for i in range(len(s)):
        if s[i] not in s_list:
            answer.append(-1)
            s_list.append(s[i])
        else:
            answer.append(i - s_list[s[i]])
            s_list.append(s[i])

    return answer