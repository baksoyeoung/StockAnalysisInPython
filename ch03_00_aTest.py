import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore', category=FutureWarning) # FutureWarning 제거

A = np.array([[1,2],[3,4]])
print(A)
print(f'타입:{type(A)}')
print(f'배열의 차원:{A.ndim}') #배열의 차원
print(f'배열의 크기:{A.shape}') #배열의 크기
print(f'원소 자료형:{A.dtype}') #원소 자료형

print(f'최대값:{A.max()}')
print(f'평균값:{A.mean()}')
print(f'최소값:{A.min()}')
print(f'합계:{A.sum()}')

print(A[0])
print(A[1])

print(A[0][0])
print(A[0,0])

print("조건에 맞는 원소들만 인덱싱")
print(A[A>1])

print('전치') #주대각을 기준으로 서로 바꿈
print(A.T)

print('다차원 배열을 1차원 배열 형태로 평탄화')
print(A.flatten())

print('같은 크기의 행렬끼리는 사칙연산을 할 수 있다')
print(A + A)
print(A - A)
print(A * A)
print(A / A)

print('브로드캐스팅')
B = np.array([10, 100])
print(A * B)

print(B.dot(B)) #np.dot(B, B) 와 같다

print(A.dot(B)) #A(2*2) B(2*1)의 내적 곱을 구한다.

s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0]) #리스트로 시리즈 생성
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
s[5.9] = 5.5
ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
s = s.append(ser)
s.index.name = 'MY_IDX'
s.name = 'MY_SERIES'
print(s)

print(s.index[-1]) #마지막 인텍스 값
print(s.values[-1]) #마지막 인텍스의 데이터

print(s.loc[8.0]) #로케이션 인텍서
print(s.iloc[-1]) #인티저 로케이셩 인텍서

print(s.values[:]) #values 는 결과값이 복수 개일 때 배열로 반환
print(s.iloc[:]) #iloc 는 결과값이 복수 개일 때 시리즈변 반환

print(s.drop(8.0)) #s.drop(s.index[-1]) 과 같다.
#출력된 결과에서 마지막 원소가 보이지 않지만 실제로 s 시리즈에는 변화가 없다.
#만일 마지막 원소를 삭제한 결과를 s 시리즈에도 반영 하려면
#s = s.drop(8.0)으로 입력 해야 한다.

print(s.describe())

plt.title("ELLIOTT_WAVE")
plt.plot(s, 'bs--') #시리즈를 bs--(푸른 사각형과 점선) 형태로 출력
plt.xticks(s.index) #x축의 눈금값을 s 시리즈의 인텍스값으로 설정
plt.yticks(s.values) #y축의 눈금값을 s 시리즈의 데이터값으로 설정
plt.grid(True)
#plt.show()

df = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 2467, 2041], 'KOSDAQ': [542, 682, 631, 798, 675]},
                  index=[2014, 2015, 2016, 2017, 2018])
print(df)
print(df.describe())
print(df.info())

koisp = pd.Series([1915, 1961, 2026, 2467, 2041], index=[2014, 2015, 2016, 2017, 2018], name='KOISP')
print(koisp)
kosdaq = pd.Series([542, 682, 631, 798, 675], index=[2014, 2015, 2016, 2017, 2018], name='KOSDAQ')
print(kosdaq)

df = pd.DataFrame({koisp.name: koisp, kosdaq.name: kosdaq})
print(df)

columns = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018]
rows = []
rows.append([1915, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 697])

df = pd.DataFrame(rows, columns=columns, index=index)
print(df)

print('for index순회')
for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])


print('--------------')
for row in df.itertuples(name='KRX'):
    print(row)


print('--------------')
for row in df.itertuples():
    print(row[0], row[1], row[2])

print('--------------')
for row in df.iterrows:
    print(row[0], row[1], row[2])


