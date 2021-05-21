# title : 실습 10A (19p)
# Develop by : 20182204 한찬희
# Date : 2021-05-21

# 숫자를 n을 입력하고 홀수인지 짝수인지 return하는 프로그램
# checkOddEven(n) function을 작성하여 주어진 숫자 n이 홀수이면 n은 홀수, 짝수이면 n은 짝
# 수를 프린트 할 것

def checkOddEven(n):
    tmp = int(n)
    if tmp % 2 == 0:
        return "짝수"
    else :
        return "홀수"

n = input("입력(짝수 또는 홀수 판별) : ")

if(n.isalpha()): # 문자인지 확인
    print("정수를 입력 바랍니다.")
elif( abs(float(n)) - int(abs(float(n))) > 0): # 소수인지 확인
    print("정수를 입력 바랍니다.")
else:
    print(checkOddEven(n))