def solution(priorities, location):
    answer = 0
    array = [(v, i) for i, v in enumerate(priorities)]

    while array:
        # print(array)
        if array[0][0] == max(array)[0]:
            answer += 1
            # print(answer)
            if array[0][1] == location:
                break
            array.pop(0)
        else:
            array.append(array.pop(0))
    return answer
