# 내가 생각한 코드
# 공백 처리가 어려움
def solution(s, n):
    answer = ""
    list_s = list(s)
    for i in list_s:
        ord_s = ord(i)
        ascii_s = ord_s + n
        chr_s = chr(ascii_s)
        answer += str(chr_s)
    return answer

# 구글링 참조

def solution(s, n):
    list_s = list(s)
    for i in range(len(list_s)):
        if list_s[i].isupper():
            list_s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif list_s[i].islower():
            list_s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(list_s)
