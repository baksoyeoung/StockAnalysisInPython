from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2022-01-01')

print(kospi)

window = 252
peak = kospi['Adj Close'].rolling(window, min_periods=1).max() #kospi 종가 칼럼에서 1년(거래일기준)기간단위로 최고치 peck를 구한다.
drawdown = kospi['Adj Close'] / peak - 1.0 #drawdown은 최고치(peak) 대비 현재 kospi 종가가 얼마나 하락 했는지를 구한다.
max_dd = drawdown.rolling(window, min_periods=1).min()

plt.figure(figsize=(9, 7))
plt.subplot(211)
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212)
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()

print(max_dd.min())
a = max_dd[max_dd == -0.12536631425522216]
print(a)