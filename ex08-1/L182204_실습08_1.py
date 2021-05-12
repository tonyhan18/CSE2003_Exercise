# 05.07.21
# 한찬희(20182204)

employee = {'보검', '두준', '공유', '세윤', '고수', '우종', '준호', '종민', '시우', '태현'}
print("전체 사원 명단 :", employee)
# intersection 사용(공집합)
late = {'우종', '보검'}
print("지각자 명단 :",employee & late)
# intersection 사용(공집합)
absent = {'우종', '보검', '종민', '두준'}
print("결근자 명단 :",employee & absent)
# difference 사용(차집합)
print("보너스 지급 대상자 명단 :",employee - late - absent)
print("야근 대상자 명단 :",(employee&late)&(employee&absent))
# 데이터 입력받음
n1,n2 = input("신입사원 명단 입력 : ").split()
if(n1 in employee or n2 in employee):
    print("신입사원의 이름이 기존 사원의 이름과 중복")
employee.update([n1,n2])
print("전체 사원 명단 :", employee)
