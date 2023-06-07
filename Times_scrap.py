import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
times=[]
for i in range(1,101):
    url=rf"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence={i}&startPage=1"
    # print(requests.get(url))
    code=requests.get(url).content
    soup=BeautifulSoup(code,'lxml')
    jobs=soup.find_all('li','clearfix job-bx wht-shd-bx')

    for job in jobs:
        d={}
        company=job.find('h3','joblist-comp-name').get_text().strip("\r\n").strip()
        role=job.find('h2').get_text().replace('\n\r\n',"").replace("\n\n",'').replace('"','').strip()
        d['Company']=company
        d['Role']=role


        details=job.find_all('ul','top-jd-dtl clearfix')
        for detail in details:
            data=detail.text.strip("\n").replace("\n",'|').replace('card_travel','').replace("₹",'').split("|")
            d['Exeperience']=data[0]
            d['Salary']=data[1]
            d['Location']=data[-1]
        details2=job.find_all('ul','list-job-dtl clearfix')
        # print(diss)
        for detail2 in details2:
            dis=detail2.find("li").get_text().strip("\n\r")
            key_skill=detail2.find('span','srp-skills').get_text().strip('\r\n').strip().split(",")
            key_list=[]
            for i in key_skill:
                k=i.strip('''"''').strip().strip('''"''')
                key_list.append(k)
            d["Key Skill"]=str(key_list).replace('[','').replace(']','').replace("'",'')

        details3=job.find_all('div','list-job-bt clearfix')
        for detail3 in details3:
            day=detail3.find("span",'sim-posted').get_text()
            d['Post_Day']=day.strip('\n').replace('\r\n\t\t    \t\n','& ')
        times.append(d)
        
df=pd.json_normalize(times)
df.to_excel(r"C:\Users\Goutam\OneDrive\Desktop\WebScrapping\TimeJobs_dataset.xlsx",index=False)
