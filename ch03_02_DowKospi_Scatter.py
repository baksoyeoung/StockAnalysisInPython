import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

#현재종가를 특정 시점의 종가로 나누어 변동률을 구한다.(지수화) 일간 변동률의 누적합을 구하는 것보다 수월하게 처리할 수 있다.
# d = (dow.Close / dow.Close.loc['2000-01-04']) * 100 #금일 다우존스 지수를 2000-01-04 다우존스 지수로 나눈 뒤 100곱
# k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100
#
# plt.figure(figsize=(9, 5))
# plt.plot(dow.index, d, 'r--', label='Dow Jones Industrial')
# plt.plot(kospi.index, k, 'b', label='KOSPI')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

print(len(dow)); print(len(kospi))

df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')
print(df)

plt.figure(figsize=(7, 7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()