def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    h, l = 0, 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            h += 1
            l += 1
        if lottos[i] == 0:
            h += 1
    
    answer.append(rank[h])
    answer.append(rank[l])
    
    return answer