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
	print(pages)

def get_jobs():
	last_page = get_last_page()
	return []