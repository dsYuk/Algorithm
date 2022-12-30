def solution(sizes):
    answer = 0
    max_w = 0
    max_h = 0
    for w, h in sizes:
        if w > h:
            h, w = w, h
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    answer = max_w * max_h
    return answer