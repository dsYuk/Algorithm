def solution(n):
    n_3 = ''
    answer = 0
    while n != 0:
        n_3 += str(n % 3)
        n //= 3
        print(n_3)
        # n을 3진법으로 변환하였을 때 거꾸로 나오는 것을 확인하여 뒤집지 않고 다시 10진법으로 변환
    answer = int(n_3, 3)
    return answer