import pandas as pd

from tool.logger import globalLog

df = pd.read_excel('datas.xlsx')
data = df[df['country'].str.contains('Chinese')]
data.to_excel('test.xlsx', index=False)

data = df['occupation'].value_counts()
print(data)

