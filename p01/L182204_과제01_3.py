bitcoin = 3928
print("500원짜리 동전 :",(bitcoin//500),"개")
bitcoin %= 500
print("100원짜리 동전 :",(bitcoin//100),"개")
bitcoin %= 100
print("남은 금액 :", bitcoin,"원")