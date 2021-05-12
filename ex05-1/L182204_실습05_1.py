in_data = input("정수 숫자 3개를 입력 : ")
print("입력 받은 값 : {:s}".format(in_data))

d1, d2, d3 = in_data.split()
sum = int(d1) + int(d2) + int(d3)

print("총합 : {:3d}".format(sum))
print("평균 : {:3.1f}".format(sum / 3))