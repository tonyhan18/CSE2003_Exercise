fp_r = open("L_In.txt",'r')
fp_w = open("L_Out.txt","w")
line = int(fp_r.readline())

# for loop를 위해 ord로 문자를 저장했습니다.
charOne = ord("A")
ans = 0
print("index = ",line,file=fp_w)

# for loop를 돌면서 문자와 숫자들을 출력하고 2번째 인덱스 값을 더합니다.
# ord 문자를 변경시킵니다.
for s in fp_r:
    num = list(int(x) for x in s.split())
    ans += num[2]
    print(chr(charOne),"=",num, file = fp_w)
    charOne += 1
    
# 마지막에 A[2]와 B[2]의 합을 출력합니다.
print("A[2] + B[2] =", ans, file = fp_w, end = "")

fp_r.close()
fp_w.close()
    
