def solution(d, budget):
    answer = 0
    d.sort()      # 오름차순으로 정렬해야 최대한 많은 물품을 지원할 수 있음
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
    return answer