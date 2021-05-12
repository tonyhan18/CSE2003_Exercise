L = [1,2,3,4,5]
temp = input("리스트 L에 추가할 data를 입력 : ")
if(len(temp.split()) != 1):
    print("숫자를 한개만 입력해 주세요")
else:
    data = int(temp.split()[0])
    L.append(data)
    print(L)