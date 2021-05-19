# title : 실습 09B 3번(14p)
# Develop by : 20182204 한찬희
# Date : 2021-05-19

# 양의 정수 N을 입력으로 받아 1+2+3+ . . . + N 을 구하고 음수가 입력되면 양수를 입력하라는
# 문자열을 출력하고 다시 반복되는 코드를 작성할 것

data = 0
while (True):
    data = int(input("양의 정수를 입력하세요 : "))
    if (data < 0):
        print("양의 정수가 아닙니다.")
    else:
        break

ans = 0 
for i in range(1, data + 1):
    ans += i

print("1... N의 합 : ", ans)