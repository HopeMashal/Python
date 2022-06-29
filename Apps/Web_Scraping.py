# first step install and import modules
# pip/pip3 install lxml
# pip/pip3 install requests
# pip/pip3 install beautifulsoup4   --> For more information see { https://www.crummy.com/software/BeautifulSoup/bs4/doc/ }

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
skills = []

# second step use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")   #Website Link

# third step save page content/markup
src = result.content

# 4th step create soup object to prase content
soup = BeautifulSoup(src, "lxml")

# 5th step find the elements containing info we need
# Job titles, job skills, company names, location names
job_titles = soup.find_all("h2", {"class":"css-m604qf"})  #From website (h2 tag) --> class of (h2 tag -> job titles)
# soup.find_all(html_tag , {features} )

company_names = soup.find_all("a",{"class":"css-17s97q8"})
location_names = soup.find_all("span",{"class":"css-5wys0k"})
job_skills = soup.find_all("div",{"class":"css-y4udm8"})

# 6th step loop over returned lists to extract needed info into other lists
for i in range(len(job_titles)):
  job_title.append(job_titles[i].text)
  company_name.append(company_names[i].text)
  location_name.append(location_names[i].text)
  skills.append(job_skills[i].text)

# 7th step create csv file and fill it with values



# 8th step to fetch the link of the job and fetch in page details
# Salary, job requirements

