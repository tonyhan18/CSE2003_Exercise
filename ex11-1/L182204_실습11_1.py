# title : 실습 11 1번(23p)
# Develop by : 20182204 한찬희
# Date : 2021-05-28

# 아래와 같은 집 모양을 그리기
# fd(), rt(), lt(), color(), shape(), begin_fill(), end_fill(), fillcolor() 함수 사용, 각 변의 길이는 100
# 가능한 fd(), rt() 함수를 적게 사용하여 작성
# “YELLOW”, “GREEN”으로 색 표현

from turtle import *

shape("turtle")
pencolor("red")
fillcolor("green")
begin_fill()
right(90)
for i in range(4):
    forward(100)
    if i != 3 : left(90)
end_fill()

fillcolor("yellow")
begin_fill()
for i in range(2):
    right(120)
    forward(100)
end_fill()
done()