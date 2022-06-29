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
date = []

page_num = 0

while True:

  try:
    # second step use requests to fetch the url
    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}")   #Website Link

    # third step save page content/markup
    src = result.content

    # 4th step create soup object to prase content
    soup = BeautifulSoup(src, "lxml")

    page_limit = int(soup.find("strong").text)
    if(page_num > page_limit//15):
      print("Pages ended, terminate!!")
      break

    # 5th step find the elements containing info we need
    # Job titles, job skills, company names, location names
    job_titles = soup.find_all("h2", {"class":"css-m604qf"})  #From website (h2 tag) --> class of (h2 tag -> job titles)
    # soup.find_all(html_tag , {features} )

    company_names = soup.find_all("a",{"class":"css-17s97q8"})
    location_names = soup.find_all("span",{"class":"css-5wys0k"})
    job_skills = soup.find_all("div",{"class":"css-y4udm8"})
    posted_new = soup.find_all("div",{"class":"css-4c4ojb"})
    posted_old = soup.find_all("div",{"class":"css-do6t5g"})
    posted = [*posted_new,*posted_old]

    # 6th step loop over returned lists to extract needed info into other lists
    for i in range(len(job_titles)):
      job_title.append(job_titles[i].text)
      links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
      company_name.append(company_names[i].text.replace("-","").strip())
      location_name.append(location_names[i].text)
      skills.append(job_skills[i].text)
      date.append(posted[i].text.strip())

    page_num += 1
    print("Page switched!")

  except:
    print("ERROR!!")
    break


for link in links:
  result_link = requests.get(link)
  src_link = result_link.content
  soup_link = BeautifulSoup(src_link,"lxml")
  #! I have a problem with salaries and requirement
  #salaries = soup_link.find("span",{"class":"css-4xky9y"}) #? Because it's not a unique value, there is a problem with it
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
file_list = [job_title,company_name,date,location_name,skills, links, salary, responsibilities]
exported = zip_longest(*file_list)  #* (*->UNPACKING)
""" 
  Ex :
    x=[1,2,3]
    y=["a","b","c"]
    z = [x,y]
    zip_longest(*z) => result { [1,"a"][2,"b"][3,"c"] }
"""

# SEE { https://github.com/HopeMashal/Python/blob/master/jobstest.csv }
with open("jobstest.csv","w") as myfile:
  wr = csv.writer(myfile)
  wr.writerow(["Job Title","Company Name","Date","Location","Skills","Job Link","Salary","Job Requirements"])
  wr.writerows(exported)

# 8th step to fetch the link of the job and fetch in page details
# Salary, job requirements

# 9th step is to do the above for all pages


