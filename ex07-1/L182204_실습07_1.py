# 인덱싱만 이용하여 왼쪽으로 한 칸씩 쉬프트
L=[1,3,5,7,9]
tmp = L[0]
L[0] = L[1]
L[1] = L[2]
L[2] = L[3]
L[3] = L[4]
L[4] = tmp
print(L)