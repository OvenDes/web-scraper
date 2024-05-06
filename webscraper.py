from bs4 import BeautifulSoup
import requests

print("what type of working environemnt would you like?")
work_envo= input(">")
print()


html_text = requests.get("https://www.builtinaustin.com/jobs/internships").text
soup= BeautifulSoup(html_text, 'lxml')
jobs= soup.find_all("div", class_="row")

for job in jobs:
    name = job.find("h2", class_="fw-extrabold fs-md fs-xl-xl")
    company = job.find("div", class_="font-barlow fs-md fs-xl-xl d-inline-block m-0 hover-underline")
    posted_date= job.find("span", class_="font-barlow text-gray-03")
    headers=soup.find("div", class_="d-flex gap-md")
    type1= headers.find("span", class_="font-barlow text-gray-03")
    #skills= job.find("div", class_="font-barlow fw-medium mb-md")
    #if work_envo==type:
    if type1 and work_envo.lower() in type1.text.lower():
        if name:
            print("Company:"+ company.text)
            print("Position:"+ name.text)
            print("Posted Date:" + posted_date.text)
            print("Type: "  + type1.text)
            print()



