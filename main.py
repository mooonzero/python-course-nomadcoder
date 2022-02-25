#2-06_Extracting_Titles
# import requests
# from bs4 import BeautifulSoup
# ==> indeed.py를 import 하니까 requests나 bs4는 따로 import 안해줘도 된다니 .. 신기
from indeed import get_jobs as get_indeed_jobs

indeed_jobs = get_indeed_jobs()

print(indeed_jobs)





#print(max_indeed_page)

# range(max_page)
# #range(n) n크기의 배열을 만들어 줌 
# for n in range(max_page):
# 	print(f"start={n*50}")