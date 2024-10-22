from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    # tags = soup.find('h5') # finds the first tag
    # courses=soup.find_all('h5') #finds all the tags
    # for i in courses:
    #     print(i)

    course_card= soup.find_all('div', class_='card')
    for course in course_card:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]
        print(f'{course_name}for {course_price}')