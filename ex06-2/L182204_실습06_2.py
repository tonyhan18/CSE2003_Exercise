in_data = input("수식 입력(예: 20 * 40) : ")

# 오직 실수와 수식을 포함한 3개의 데이터만이 들어온다고 가정
if (len(list(in_data.split())) != 3):
    print("인자의 갯수가 3개가 아닙니다.")
else:
    op1, mnemonie, op2 = in_data.split()
    op1 = float(op1)
    op2 = float(op2)
    if(mnemonie == '+'):
        print("{:.6f} {:s} {:.6f} = {:.6f}".format(op1,mnemonie,op2,(op1 + op2)))
    elif(mnemonie == '-'):
        print("{:.6f} {:s} {:.6f} = {:.6f}".format(op1,mnemonie,op2,(op1 - op2)))
    elif(mnemonie == '*'):
        print("{:.6f} {:s} {:.6f} = {:.6f}".format(op1,mnemonie,op2,(op1 * op2)))
    elif(mnemonie == '/'):
        if(op2 == 0): print("{:.6f} 로 나누기를 수행할 수 없습니다.".format(op2))
        else : print("{:.6f} {:s} {:.6f} = {:.6f}".format(op1,mnemonie,op2,(op1 / op2)))
    else:
        print("%s 지원하지 않는 연산자입니다." %mnemonie)