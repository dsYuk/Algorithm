import pandas as pd

# Series 객체 생성
temp = pd.Series([-20, -10, 10, 20])
temp[0] # 1월 온도

# Series (Index 지정)
temp = pd.Series([-20, -10, 10, 20], index = ['Jan', 'Feb', "mar", "Apr"])
temp['Jan'] # Jan 데이터 출력