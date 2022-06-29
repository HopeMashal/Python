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
links = []
salary = []
responsibilities = []

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
  links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
  company_name.append(company_names[i].text)
  location_name.append(location_names[i].text)
  skills.append(job_skills[i].text)

for link in links:
  result_link = requests.get(link)
  src_link = result_link.content
  soup_link = BeautifulSoup(src_link,"lxml")
  #! I have a problem with salaries and requirement
  #salaries = soup_link.find("span",{"class":"css-4xky9y"}) #? Because it's not a unique value, there is a problem with it
  #requirements = soup_link.find("div",{"class":"css-1t5f0fr"}).find("ul")
  #salary.append(salaries.text.strip())
  salaries = "Confidential"
  salary.append(salaries.strip())
  #requirements= soup_link.find("div",{"class":"css-1t5f0fr"}).ul
  #respon_text =""
  #for li in requirements.find_all("li"):
  #  respon_text += li.text+"| "
  #respon_text = respon_text[:-2]
  #responsibilities.append(respon_text)
  requirements = "Bachelor/Master of Science in relevant area or equivalent formal education."
  responsibilities.append(requirements)

# 7th step create csv file and fill it with values
file_list = [job_title,company_name,location_name,skills, links, salary, responsibilities]
exported = zip_longest(*file_list)  #* (*->UNPACKING)
""" 
  Ex :
    x=[1,2,3]
    y=["a","b","c"]
    z = [x,y]
    zip_longest(*z) => result { [1,"a"][2,"b"][3,"c"] }
"""

with open("jobstest.csv","w") as myfile:
  wr = csv.writer(myfile)
  wr.writerow(["Job Title","Company Name","Location","Skills","Job Link","Salary","Job Requirements"])
  wr.writerows(exported)

# 8th step to fetch the link of the job and fetch in page details
# Salary, job requirements


# 9th step is to do the above for all pages


# 10th step is to optimize code and clean data

