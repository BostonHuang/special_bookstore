
import streamlit as st
import requests

def getCountyOption(items):
	optionList = [] # 創建一個空的 List 並命名為 optionList
	for item in items:
		if (item['cityName'][:3] in optionList):# 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
			continue
		optionList.append(item['cityName'][:3])
		# hint: 想辦法處理 item['cityName'] 的內容

		# 如果 name 不在 optionList 之中，便把它放入 optionList
		# hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
	return optionList

def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res = response.json() # 將 response 轉換成 json 格式
	return res # 回傳值

def app():
	bookstoreList = getAllBookstore() # 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
	countyOption = getCountyOption(bookstoreList)
 
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList)) # 將 118 替換成書店的數量
	county = st.selectbox('請選擇縣市', countyOption)
	
if __name__ == '__main__':
	app()
