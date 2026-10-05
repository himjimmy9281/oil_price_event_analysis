import pandas as pd


#讀取csv檔案
df = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\BRENT_Crudeoil.csv')
df2 = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\WTI_crudeoil.csv')
df3 = pd.read_csv(f'C:\\jimmyrepo\\data\\raw\\international_event.txt')

#列出資料架構資訊，並檢查是否有缺失值
print('\nBrent石油:')
print(df.info())
print('\n缺失值統計:')
print(df.isnull().sum())
print('\nWTI石油:')
print(df2.info())
print('\n缺失值統計:')
print(df2.isnull().sum())
print('\n國際事件:')
print(df3.info())
print('\n缺失值統計:')
print(df3.isnull().sum())
#列印結果顯示
#Brent及WTI的原油價格有缺失需進行資料清理，日期欄位的資料格式為str，需轉換為datetime格式。
#國際事件的資料沒有缺失值，但事件日期欄位的資料格式需要進行轉換，將日期欄位轉換為datetime格式。