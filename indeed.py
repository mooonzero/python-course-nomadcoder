#2-06_Extracting_Titles
import requests
from bs4 import BeautifulSoup
LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"
#main.py에서 작성했던 indeed의 페이지를 추출하는 코드들을 하나의 함수로 만들어줌

def extract_indeed_pages():
	result = requests.get(URL)
	soup = BeautifulSoup(result.text,'html.parser')
	pagination = soup.find("div",{"class":"pagination"})
	links = pagination.find_all('a')
	pages = []
	
	for link in links[:-1]:
		pages.append(int(link.string))
	
	max_page = pages[-1]
	return max_page

def extract_indeed_jobs(last_page):
	#for page in range(last_page):
		jobs = []
		result = requests.get(f"{URL}&start={0*LIMIT}")
		soup = BeautifulSoup(result.text,'html.parser')
		#구직 정보가 담겨있는 div의 class 명으로 찾아줌
		results = soup.find_all("div",{"class":"job_seen_beacon"})
		for result in results:
			#title =result.find("h2",{"class":"jobTitle"})
			#anchor = title.find("span")["title"] 로 했을땐 오류 발생
			actual_title = result.find("span",title = True).string
			print(actual_title)
			#jobTitle안의 span title을 가져와야함
		return jobs
		#jobs는 다음 시간에 