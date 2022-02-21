#2-06_Extracting_Titles
# import requests
# from bs4 import BeautifulSoup
# ==> indeed.py를 import 하니까 requests나 bs4는 따로 import 안해줘도 된다니 .. 신기
from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_page)

#print(max_indeed_page)

# range(max_page)
# #range(n) n크기의 배열을 만들어 줌 
# for n in range(max_page):
# 	print(f"start={n*50}")