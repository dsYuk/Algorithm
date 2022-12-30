def solution(s):

    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i, entry in enumerate(num):
        s = s.replace(entry, str(i))

    return int(s)