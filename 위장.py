import collections
import math


def solution(clothes):
    cloth = []

    for i in range(len(clothes)):
        cloth.append(clothes[i][1])

    cloth = collections.Counter(cloth)
    # print(cloth)
    value = []
    for v in cloth.values():
        value.append(v)

    for i in range(len(value)):
        value[i] = value[i] + 1

    return math.prod(value) - 1