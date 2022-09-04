h = [int(input()) for _ in range(9)]
h.sort()
a, b = 0, 0

for i in range(9):
    for j in range(i+1, 9):
        if (sum(h) - (h[i] + h[j])) == 100:
            a = h[i]
            b = h[j]

h.remove(a)
h.remove(b)

for i in h:
    print(i)