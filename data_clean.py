from pathlib import Path

import pandas as pd

#讀取csv檔案
project_dir = Path(__file__).resolve().parent
raw_dir = project_dir / 'raw_data'
clean_dir = project_dir / 'clean_data'
clean_dir.mkdir(exist_ok=True)

df = pd.read_csv(raw_dir / 'BRENT_Crudeoil.csv')
df2 = pd.read_csv(raw_dir / 'WTI_crudeoil.csv')

#保留日期欄位並轉換為日期型別，價格缺失值以線性插值填補
for data, price_column in ((df, 'brent_price'), (df2, 'wti_price')):
	data['observation_date'] = pd.to_datetime(data['observation_date'].str.replace('/', '-', regex=False))
	data[price_column] = data[price_column].interpolate(method='linear')

#列印清理後的資料架構及缺失值統計
print('\n清理後的BRENT石油:')
print(df.info())
print('\n缺失值統計:')
print(df.isnull().sum())
print('\n清理後的WTI石油:')
print(df2.info())
print('\n缺失值統計:')
print(df2.isnull().sum())
#清理後缺失值為零，資料清理完成

#將清理後的資料存回csv檔案
df.to_csv(clean_dir / 'BRENT_Crudeoil_cleaned.csv', index=False, date_format='%Y-%m-%d', float_format='%.2f')
df2.to_csv(clean_dir / 'WTI_Crudeoil_cleaned.csv', index=False, date_format='%Y-%m-%d', float_format='%.2f')
print('\n清理後的資料已存到乾淨資料的檔案中。')