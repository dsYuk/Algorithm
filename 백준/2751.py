import sys

N = int(sys.stdin.readline())

N_list = []

for i in range(N):
    n = int(sys.stdin.readline())
    N_list.append(n)
N_list.sort()
for i in range(len(N_list)):
    print(N_list[i])