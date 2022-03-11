import csv

def save_to_file(jobs):
	file = open("jobs.csv", mode="w")
	#open 해당 파일을 열어주는 함수,만약 해당 파일이 없다면 생성까지 해줌 
	writer = csv.writer(file)
	writer.writerow(["title", "company", "location", "link"])
	for job in jobs:
		#writer.writerow(job.values())
		writer.writerow(list(job.values()))
	return
	