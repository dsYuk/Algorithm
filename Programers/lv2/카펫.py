# first try

import itertools


def solution(brown, yellow):
    answer = []
    b_list = [i for i in range(1, brown + 1)]
    y_list = [i for i in range(1, yellow + 1)]
    c = list(itertools.product(b_list, repeat=2))

    for i in range(len(c)):
        if c[i][0] * c[i][1] == brown + yellow and c[i][0] >= c[i][1]:
            answer.append(list(c[i]))

    if (answer[0][0] - 2) * (answer[0][1] - 2) == yellow:
        return answer[0]
    return answer[1]

# test case 4, 6, 7 failed

# second try

def solution(brown, yellow):
    answer = []
    yellow_w = 0
    yellow_h = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_w = int(yellow / i)
            # print(yellow_w)
            yellow_h = i
            # print(yellow_h)
            if yellow_w * 2 + yellow_h * 2 + 4 == brown:
                answer.append(yellow_w + 2)
                answer.append(yellow_h + 2)
                
                return sorted(answer, reverse=True)

    return answer