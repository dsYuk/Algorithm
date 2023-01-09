def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        # print(i, citation)
        if i >= citation:
            # print(i)
            return i
    return len(citations)

solution([3, 0, 6, 1, 5])