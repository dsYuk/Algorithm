def solution(a, b):
    answer = 0
    day = {2:"SUN", 3:"MON", 4:"TUE", 5:"WED", 6:"THU", 0:"FRI", 1:"SAT"}
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(a - 1):
        answer += month[i]
    answer += b - 1
    answer = day[answer % 7]
    return answer