# title : 실습 10B 1번(16p)
# Develop by : 20182204 한찬희
# Date : 2021-05-26

#  Prime number test (소수 확인 프로그램), fill the blank

def chk() :
    if (N < 2): return (False)
    if(N == 2 or N == 3): return (True)
    if(N % 2 == 0 or N % 3 == 0): return (False)
    for i in range(5, int((N**(1/2))) + 1, 6):
        if(N % i == 0 or N % (i+2) == 0):
            return (False)
    return (True)

# main part
N = int(input())
primeChk= chk() # 전역변수
if primeChk == True :
    print("prime")
else :
    print("not prime")