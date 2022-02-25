#2-04_Extracting_Indeed_Pages_2
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text,'html.parser')

pagination = indeed_soup.find("div",{"class":"pagination"})

links = pagination.find_all('a')

pages = []
# for link in links:
# 	#pages.append(link.find("span").string)
# 	pages.append(int(link.string))
# #.string -> text만 가져옴
# pages = pages[0:-1]
#  ==> 페이지 숫자들을 추출하기 위해 모든 span태그를 배열에 넣어준 후 string만 뽑아서 int형으로 바꾸려고 하니 제일 마지막 span 태그에 있는 text때문에 오류 발생 

# 아래와 같은 식으로 변경해서 for문 자체를 마지막 span태그 전까지 돌려줌
for link in links[:-1]:
	pages.append(int(link.string))

max_page = pages[-1]

