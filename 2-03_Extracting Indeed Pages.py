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
#print(pages)
spans = []
for page in pages:
	#print(page.find("span"))
	spans.append(page.find("span"))
# 마지막 페이지 뒤에 다음 페이지 가리키는 버튼 나타내는 span은 생략해야함
#print(spans[-1]) : spans array 제일 마지막 값을 print 하겠다 
#print(spans[:-1]) : 제일 마지막 값은 제외하고 print 하겠다
#print(spans[n:m]) n번째부터 m번째 앞까지 print 하겠다

print(spans)