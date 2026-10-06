# 資料取得+清理
## 1.資料來源
在尋找資料的部分，本人詢問ChatGPT能取得此專題可用資料來源來做為參考:

<p align="left">
<img src="image\Ask_sources.PNG" width="40%" height="40%">
</p>

### Brent及WTI歷年石油價格
Brent及WTI的csv原檔皆來自Federal Reserve Economic Data|FRED官網:

URL:
- Brent | https://fred.stlouisfed.org/series/DCOILBRENTEU
- WTI | https://fred.stlouisfed.org/series/DCOILWTICO

### 重大事件表
此資料本人是用ChatGPT下達以下描述並把資訊複製進txt檔。

事件的資料來源皆來自美國能源情報署（U.S. Energy Information Administration）(EIA)官網。

## 2.資料檢查
使用 Python 的 pandas 套件 檢視 Brent、WTI的原油價格資料及國際事件資料的欄位資訊與缺失值統計，確認各資料集的欄位、資料型態及資料完整性。

檢查結果顯示，Brent 與 WTI 原油價格資料有缺失值，且日期欄位是字串格式，需在資料清理時補值並轉換日期型態；國際事件資料沒有缺失值，但事件日期欄位也需轉換為日期型態。

<p align="left">
<img src="image\data_check.png" width="50%" height="50%">
</p>
<p align="left">
<img src="image\data_check02.png" width="50%" height="50%">
</p>

檢查程式：[data_check.py](data_check.py)

## 3.資料清理
原始程式碼一開始只用 Python 的 pandas 進行資料清理，清理完之後發現缺失價格雖補齊了但日期沒了。
所以本人用VScode內建的AI Copilot 協助清理程式的撰寫

<p align="left">
<img src="image\ai_assist.png" width="50%" height="50%">
</p>
<p align="left">
<img src="image\ai_assist3.png" width="50%" height="50%">
</p>

清理程式:[data_clean.py](data_clean.py)