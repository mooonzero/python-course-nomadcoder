#2-3 Extracting Indeed Pages
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

#soup : data를 추출하는 애 

#indeed_soup = BeautifulSoup(html_doc,'html.parser')
	#html_doc을 넣어줄거고 html을 사용할거다 

indeed_soup = BeautifulSoup(indeed_result.text,'html.parser')

pagination = indeed_soup.find("div",{"class":"pagination"})
#html 안에서 paging버튼이 들어있는 부분을 찾아주는 ..
	# div 안에 class명을 pagination으로 설정해줌 
#print(pagination)

pages = pagination.find_all('a')
print(pages)