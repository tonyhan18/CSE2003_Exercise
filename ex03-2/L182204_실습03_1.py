americano = int(input("아메리카노 판매 개수? "))
caffeelatte = int(input("카페라떼 판매 개수? "))
cappuccino = int(input("카푸치노 판매 개수? "))

discount = float(input("카푸치노 할인률? "))

ans = 0.0
ans += americano * 2000
ans += (caffeelatte * 3000) 
ans += (cappuccino * 3500) * (1 - discount)

print("총 매출은", int(ans), "원 입니다")