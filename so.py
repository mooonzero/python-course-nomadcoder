import requests
from bs4 import BeautifulSoup
LIMIT = 10
URL = f"https://stackoverflow.com/jobs?q=python"

# step.1 get the page
# step.2 make the request 
# step.3 extract jobs

def get_last_page():
	result = requests.get(URL)
	soup = BeautifulSoup(result.text,"html.parser")
	pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
	last_page = pages[-2].get_text(strip=True)
	#pages의 제일 마지막이 next btn이므로 그걸 빼고 출력해주려고 -2
	return int(last_page)
#last_page = pages[-2].string 으로 print 했을때는 None이 나옴 차이를 명확하게 알기!
# .get_text(는 bs4의 함수 .. 
#.get_text(strip=True) -> get_text안의 whitespace 제거
#int(page)로 return 해준 이유 :
	# range는 string이 아닌 int값만을 받기 ㄸㅐ문 ; 

def extract_jobs(last_page):
	jobs =[]
	for page in range(last_page):
		print(page)

def get_jobs():
	last_page = get_last_page()
	jobs = extract_jobs(last_page)
	return jobs