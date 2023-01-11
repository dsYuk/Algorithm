from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    time = 0
    count = 0

    while progresses:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        else:
            time += 1
            if count > 0:
                answer.append(count)
                count = 0

    answer.append(count)
    return answer