import os
from bs4 import BeautifulSoup
import requests
import time

print('Put some skills you are not familiar with')
unfamiliar_skill = input('->')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    if not os.path.exists('posts'):
        os.makedirs('posts')
    html_txt = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_txt, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
    for index, job in enumerate(jobs):
        publish = job.find('span', class_='sim-posted').span.text.replace('Posted', '')
        if 'few' in publish:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/job{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Skills Required: {skills}\n")
                    f.write(f"More Info: {more_info}\n")
                
                print(f"File Saved: job{index}.txt")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print('Waiting...')
        time.sleep(time_wait * 60)
