# title : 실습 09B 2번(14p)
# Develop by : 20182204 한찬희
# Date : 2021-05-19

# 사용자로부터 임의의 개수의 성적을 받아서 평균을 계산하기 음수의 값이 입력되면 종료
# 입력 값(정수)을 받아들이고 합계를 구함
# 음수가 나오면 중단, break문을 사용

print("종료하려면 음수를 입력하시오")
i = 0
hap = 0
while True:
    tmp = int(input("성적을 입력하시오: "))
    if tmp < 0 :
        if i == 0 : i = 1
        print("평균은 %d입니다."%(hap/i))
        break
    i += 1
    hap += tmp
    
