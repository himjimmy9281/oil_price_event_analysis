import pandas as pd


#讀取csv檔案
df = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\international_event.csv')
df2 = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\BRENT_Crudeoil.csv')
df3 = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\WTI_crudeoil.csv')

#列出前五筆資料，並檢查是否有缺失值
print('\nInternational Event Data:')
print(df.head())
print('\n缺失值統計:')
print(df.isnull().sum())
print('\nBRENT Crude Oil Data:')
print(df2.head())
print('\n缺失值統計:')
print(df2.isnull().sum())
print('\nWTI Crude Oil Data:')
print(df3.head())
print('\n缺失值統計:')
print(df3.isnull().sum())