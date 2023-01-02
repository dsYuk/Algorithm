import collections

N = int(input())
card = collections.deque([i for i in range(1, N + 1)])

while len(card) != 1:
    card.popleft()
    top = card.popleft()
    card.append(top)
print(card[0])
