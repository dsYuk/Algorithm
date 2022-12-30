def solution(s):
    s_sp = s.split(" ")

    for i in range(len(s_sp)):
        s_li = list(s_sp[i])

        for j in range(len(s_li)):
            if j % 2 == 0:
                s_li[j] = s_li[j].upper()
            else:
                s_li[j] = s_li[j].lower()

        s_sp[i] = "".join(s_li)
    return " ".join(s_sp)
