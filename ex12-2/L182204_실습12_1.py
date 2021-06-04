# title : 실습 12B 1번(28p)
# Develop by : 20182204 한찬희
# Date : 2021-06-04

# 야후 파이낸스로부터 보고 싶은 임의의 주식 5가지 종류의 정보 일부를 가져오고, 4월 1일부터 5
# 월 21일까지의 시장 종료 시 가격(Close)에 대한 그래프를 그리고, 4월과 5월의 거래량(Volume) 평
# 균에 대한 정보를 출력한다.(아래는 출력에 대한 예시)
  # DataReader로 정보를 가져올 것.(원하는 종목은 자유롭게 가져올 수 있음.)
  # 거래량 평균 표에서 소수점 아래 1자리까지만 출력.
  # 테스트 시 종목, 날짜를 임의로 변경하여 테스트 할 수 있음.
  # 추가 기능 구현 시, 가산 점수 부여 예정.
  # (ex. 그래프 설명 및 디자인, 가격 별 혹은 거래량 별 정렬 등.)

import pandas_datareader.data as pdr
import datetime
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 받아오기
start = datetime.datetime(2021, 4, 2)
end = datetime.datetime(2021,5, 21)
fngu = pdr.DataReader("fngu", "yahoo", start, end)
tqqq = pdr.DataReader("TQQQ", "yahoo", start, end)
soxl = pdr.DataReader("soxl", "yahoo", start, end)
labu = pdr.DataReader("labu", "yahoo", start, end)
aapl = pdr.DataReader("aapl", "yahoo", start, end)

# 필요한 데이터만 추출
plt.title("US Stock Market")
plt.plot(fngu[fngu.index <= "2021-05-21"]["Close"])
plt.plot(tqqq[tqqq.index <= "2021-05-21"]["Close"])
plt.plot(soxl[soxl.index <= "2021-05-21"]["Close"])
plt.plot(labu[labu.index <= "2021-05-21"]["Close"])
plt.plot(aapl[aapl.index <= "2021-05-21"]["Close"])
plt.legend(["fngu","tqqq","soxl","labu","aapl"]) # 종목명
plt.grid(True, axis="y") # 세로축만 나오게
plt.show()

# 새로운 테이블 생성
df_index = ["fngu","tqqq","soxl","labu","aapl"]
df_columns = ["4월","5월","평균"]

temp = [[fngu[fngu.index < "2021-05-01"]["Volume"].mean(),fngu[fngu.index > "2021-04-30"]["Volume"].mean()],
[tqqq[tqqq.index < "2021-05-01"]["Volume"].mean(),tqqq[tqqq.index > "2021-04-30"]["Volume"].mean()],
[soxl[soxl.index < "2021-05-01"]["Volume"].mean(),soxl[soxl.index > "2021-04-30"]["Volume"].mean()],
[labu[labu.index < "2021-05-01"]["Volume"].mean(),labu[labu.index > "2021-04-30"]["Volume"].mean()],
[aapl[aapl.index < "2021-05-01"]["Volume"].mean(),aapl[aapl.index > "2021-04-30"]["Volume"].mean()]]

for i in range(0,5):
    temp[i][2:] = [(temp[i][0]+temp[i][1])/2]
    
ans = pd.DataFrame(temp,index = df_index, columns=df_columns)
pd.set_option('display.float_format', lambda x: '%11.1f' % x)
print(ans)
print()