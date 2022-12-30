def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr1[i] = arr1[i].rjust(n, "0")
        arr2[i] = bin(arr2[i])[2:]
        arr2[i] = arr2[i].rjust(n, "0")

        arr = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                arr += '#'
            else:
                arr += ' '
        answer.append(arr)
    return answer