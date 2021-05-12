# title : 실습 08B 2번(43p)
# Develop by : 20182204 한찬희
# Date : 2021-05-21

# D = {'c': 7, 'f': 3, 'a': 5} 인 사전에서 (key, value) 쌍의 데이터를 구해 오름차순으로 정렬하여
# 다음과 같이 결과를 출력하는 script 작성할 것 ( 튜플 데이터는 리스트에 저장. “items” method 활용)(사전의 원소는 바꿔서 테스트 가능.)

D = {'c':7,'f':3,'a':5}
#D = sorted(D #그냥 sorted를 돌리면 key값으로만 정렬된 리스트가 반환된다.
D = sorted(D.items())
print("After sort : ", D)