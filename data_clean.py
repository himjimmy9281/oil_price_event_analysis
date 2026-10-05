import pandas as pd

#讀取csv檔案
df = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\BRENT_Crudeoil.csv')
df2 = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\WTI_crudeoil.csv')

#複製原始資料以進行清理
df_copy = df.copy()
df2_copy = df2.copy()

#用插值法填補缺失值
df_clean = df_copy['brent_price'].interpolate(method='linear')
df2_clean = df2_copy['wti_price'].interpolate(method='linear')

#列印清理後的資料及缺失值統計
print('\n清理後的BRENT石油:')
print(df_clean.head())
print('\n缺失值統計:')
print(df_clean.isnull().sum())
print('\n清理後的WTI石油:')
print(df2_clean.head())
print('\n缺失值統計:')
print(df2_clean.isnull().sum())
#清理後缺失值為零，資料清理完成
