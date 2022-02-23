#2-08_Extracting_Location&Finishing_up
import requests
from bs4 import BeautifulSoup
LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"
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

def extract_job(html):
	title = html.find("span",title = True).string
	company = html.find("span",{"class":"companyName"})
	company_anchor =  company.find("a")
	if company_anchor is not None:
		company = company_anchor.string
	else:
		company = company.string
	location = html.find("div",{"class":"companyLocation"}).string
	#location = html.select_one("pre>div").text
	job_id = html.parent['data-jk']
	#print(location)
	return {'title':title,'company': company,'location':location,'link': f"https://kr.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"}


def extract_indeed_jobs(last_page):

	jobs = []
	for page in range(last_page):
		print(f"******Scrapping page {page}******")
		result = requests.get(f"{URL}&start={page*LIMIT}")
		soup = BeautifulSoup(result.text,'html.parser')
		#구직 정보가 담겨있는 div의 class 명으로 찾아줌
		results = soup.find_all("div",{"class":"slider_container"})
		for result in results:
			job = extract_job(result)
			jobs.append(job)
	return jobs
		