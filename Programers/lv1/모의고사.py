def solution(answers):
    answer = []
    correct = [0, 0, 0]
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == a1[i%5]:
            correct[0] += 1
        if answers[i] == a2[i%8]:
            correct[1] += 1
        if answers[i] == a3[i%10]:
            correct[2] += 1

    win = max(correct)
    for i in range(len(correct)):
        if correct[i] == win:
            answer.append(i + 1)
    return answer