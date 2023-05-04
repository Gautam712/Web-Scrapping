import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
# blog_dict={}
# name_l=[]
# date_l=[]
# category=[]
# for i in range(1,21):
#     url=rf'https://blog.consoleflare.com/category/data-science/page/{i}/'
#     code=requests.get(url).content
#     soup=BeautifulSoup(code,'lxml')
#     full_page=soup.find_all('div','mt-page-content-wrapper')
#     # print(full_page)
#
#     for t_part in full_page:
#         titles=t_part.find_all('h2','entry-title')
#         for title in titles:
#             name=title.get_text()
#             name_l.append(name)
#
#         dates=t_part.find_all('time',"entry-date published")
#         for date in dates:
#             date1=date.get_text()
#             date_l.append(date1)
#
#         cat=t_part.find('div','post-cats-list').get_text().replace('\n',',')
#         category.append(cat)
# # print(category)
#
#
# # # Truncate the longer list to match the length of the shorter list
# # if len(name_l) != len(date_l):
# #     min_len = min(len(name_l), len(date_l))
# #     name_l = name_l[:min_len]
# #     date_l = date_l[:min_len]
#
# Keep the maximum length of the two lists ### both are useful for us as of requirnment###
# max_len = max(len(name_l), len(date_l))
# name_l += [''] * (max_len - len(name_l))
# date_l += ["Not Define"] * (max_len - len(date_l))
# blog_dict['Title']=name_l
# blog_dict['Date']=date_l
# #
# # df=pd.DataFrame(blog_dict,columns=["Date",'Title'],['Category'])
# # df.to_excel(r"C:\Users\Goutam\OneDrive\Desktop\WebScrapping\Consoleflare_blogs.xlsx",index=False)
# # print(df.info())
# print(len(name_l))
# print(len(date_l))
# print(len(category))
blogs=[]
for i in range(1,21):
    url=rf'https://blog.consoleflare.com/category/data-science/page/{i}/'
    h_text=requests.get(url).content
    soup=BeautifulSoup(h_text,'lxml')
    articles=soup.find_all('article')
    d={}
    for article in articles:
        time=article.find('time').get_text()
        title=article.find('h2','entry-title').get_text()
        cat=article.find('div',"post-cats-list").get_text().strip("\n").replace("\n",",")
        T_link=article.find('a')['href']
        d["Date"]=time
        d['Title']=title
        d['Category']=cat
        d['Title_link']=T_link
        blogs.append(d)

df=pd.json_normalize(blogs)
df.to_excel(r"C:\Users\Goutam\OneDrive\Desktop\WebScrapping\Consoleflare_blogs.xlsx",index=False)
