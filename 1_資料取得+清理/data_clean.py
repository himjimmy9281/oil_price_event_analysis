from pathlib import Path

import pandas as pd

#指定檔案路徑(此區段由AI生成，原始程式碼中缺少此部分)
project_dir = Path(__file__).resolve().parent
#指定原始資料與清理後資料的資料夾路徑
raw_dir = project_dir / 'raw_data'
clean_dir = project_dir / 'clean_data'
#建立清理後資料的資料夾
clean_dir.mkdir(exist_ok=True)

#讀取原始資料檔案
df = pd.read_csv(raw_dir / 'BRENT_Crudeoil.csv')
df2 = pd.read_csv(raw_dir / 'WTI_crudeoil.csv')
df3 = pd.read_csv(raw_dir / 'international_event.txt')

#保留日期欄位並轉換為日期型別，價格缺失值以線性插值填補(此段由AI生成，原始程式碼中缺少此段)
for data, price_column in ((df, 'brent_price'), (df2, 'wti_price')):
	data['observation_date'] = pd.to_datetime(data['observation_date'].str.replace('/', '-', regex=False))
	data[price_column] = data[price_column].interpolate(method='linear')

#轉換國際事件資料的欄位型別(此段由AI生成，原始程式碼中缺少此段)
df3['event_id'] = pd.to_numeric(df3['event_id'], errors='raise').astype('int64')
for date_column in ('事件日期', '發生日、公告日或市場反應日'):
	df3[date_column] = pd.to_datetime(df3[date_column], errors='raise').dt.date
for text_column in df3.columns.difference(
	('event_id', '事件日期', '發生日、公告日或市場反應日')
):
	df3[text_column] = df3[text_column].astype('string')

#列印清理後的資料架構及缺失值統計
print('\n清理後的BRENT石油:')
print(df.info())
print('\n缺失值統計:')
print(df.isnull().sum())
print('\n清理後的WTI石油:')
print(df2.info())
print('\n缺失值統計:')
print(df2.isnull().sum())
#清理後缺失值為零
print('\n清理後的國際事件:')
print(df3.info())
#欄位型別轉換完成，全部資料清理完成

#將清理後的資料存回csv檔案(此段由AI協助生成，改善原始程式碼中缺少的部分)
df.to_csv(clean_dir / 'BRENT_Crudeoil_cleaned.csv', index=False, date_format='%Y-%m-%d', float_format='%.2f')
df2.to_csv(clean_dir / 'WTI_Crudeoil_cleaned.csv', index=False, date_format='%Y-%m-%d', float_format='%.2f')
df3.to_csv(clean_dir / 'international_event_cleaned.csv', index=False, date_format='%Y-%m-%d')
print('\n清理後的資料已存到乾淨資料的檔案中。')