import pandas as pd


#讀取csv檔案
df = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\BRENT_Crudeoil.csv')
df2 = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\WTI_crudeoil.csv')

#列出前五筆資料，並檢查是否有缺失值
print('\nBrent石油:')
print(df.head())
print('\n缺失值統計:')
print(df.isnull().sum())
print('\nWTI石油:')
print(df2.head())
print('\n缺失值統計:')
print(df2.isnull().sum())

#列印結果顯示 Brent及WTI的原油價格有缺失所以進行資料清理