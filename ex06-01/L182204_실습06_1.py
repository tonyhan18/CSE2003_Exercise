input_data = input("세 개의 정수를 입력하시오 : ")

# 갯수가 3개인지 검사
if(len(list(int(x) for x in input_data.split())) != 3):
    print("정수의 갯수가 다릅니다")
# 정렬
else:
    a,b,c = (int(x) for x in input_data.split())
    print("내림차순 정렬: ",end="")
    if(a > b):
        if(a > c):
            if(b > c):
                print(a, b, c)
            else:
                print(a, c, b)
        else:
            print(c, a, b)
    else:
        if(b > c):
            if(a > c):
                print(b, a, c)
            else:
                print(b, c, a)
        else:
            print(c, b, a)
