def solution(s):
    count, c = 0, 0

    while s != '1':
        c += 1

        if '0' in s:
            count += s.count("0")
            s = s.replace("0", "")
        s = format(len(s), 'b')

    return [c, count]