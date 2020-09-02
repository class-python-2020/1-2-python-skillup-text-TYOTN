import pandas as pd 
df = pd.read_csv('data.csv', encoding='utf-8')
print("----ヘッダ行-----")
print(df.columns) #ヘッダ行
print("----すべてのデータ-----")
print(df) #データ部分全部
print("---- 最高気温 -----")
print(df['最高気温'].values) #列を指定して取り出し
print("--- 清涼飲料売上数 ------")
print(df['清涼飲料売上数'])
print(df.mean())
print(df.describe())
