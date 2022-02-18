#2-2 navigating with Python
# 1. URL로 접근 (indeed,stackOverFlow)
# 2. 각 사이트의 페이지가 몇개인지 파악해야 함
	# 2.1 각 페이지마다 들어와서 스크랩 해줘야하니까
	# 2.2 indeed는 맞춤검색에 들어가서 한 페이지에 몇개의 게시글을 나타낼지 설정할 수 있음

#import requests를 사용하기 위해선 설치해줘야하지만 repl.it에선 다른 방법 사용
#package -> requests 검색 Python HTTP for Human 찾아서 install
import requests

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
#requests.get 이 method는 플젝 끝나고 설명해줄게 - nico

print(indeed_result)
#print(indeed_result.text)로 RUN하면 해당 페이지의 HTML을 전부 긁어옴

#beautifulsoup : library의 일종
	#html에서 정보를 추출하기 유용한 package
	#requests와 같은 방법으로 다운 받아줌 (ver4로)

#python만을 사용해 urls을 가져올 수 있음 ? Y
 	# + 온라인 library를 통해 더 강력한 기능도 사용 할 수 있음(requests)
