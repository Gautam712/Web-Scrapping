import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# page_no=int(input("please enter the total page number :"))
flipkart={}
name_l=[]
rating_l=[]
price_l=[]
ram_l=[]
rom_l=[]
exp_l=[]
display_l=[]
camera_l=[]
battery_l=[]
processor_l=[]
warranty_l=[]
for i in range(1,10):
    url=fr"https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=521e5c69-9870-4329-82fe-ca42ac030707&page={i}"
    html_code=requests.get(url).content
    soup=BeautifulSoup(html_code,'lxml')
    # print(soup)

    phones=soup.find_all('div',"_3pLy-c row")

    for phone in phones:
        name=phone.find("div","_4rR01T").get_text()
        rating=phone.find('div',"_3LWZlK")
        if(rating is None):
            rating=0.0
        else:
            rating=float(rating.get_text())

        price=int(phone.find('div',"_30jeq3 _1_WHN1").get_text().replace("₹",'').replace(",",''))
        # details=phone.find_all("ul",'_1xgFaf')
        # print(details)
        # for detail in details:
            # memory=detail.find("li",'rgWa7D').get_text().split("|")
            # print(memory)
            # if(len(memory)==3):
            #     ram=memory[0]
            #     rom=memory[1]
            #     expandable=memory[2]
            #     # print(expandable)
            # elif(len(memory)==2):
            #     if(memory[1].endswith("GB" or "TB")):
            #         ram="-"
            #         rom=memory[0]
            #         expandable=memory[1]
            #     elif(memory[0].endswith("ROM" or "Rom" or "rom")):
            #         ram="-"
            #         rom=memory[0]
            #         expandable=memory[1]
            #     else:
            #         ram=memory[0]
            #         rom=memory[1]
            #         expandable="-"
            # ram_l.append(ram)
            # rom_l.append(rom)
            # exp_l.append(expandable)

        # li_list=[]
        # li_d=phone.find_all("ul","_1xgFaf")
        features = [li.text for li in phone.find_all('li', {'class': 'rgWa7D'})]
        # result = [] # loop code in another Type
        # for li in phone.find_all('li', {'class': 'rgWa7D'}):
        #     result.append(li.text)
        # print(features)
        # check=features[0].split("|")
        # print(check)# #
        memory=[]
        for i in features[0].split("|"):
            memory.append(i)
        # print(l)
        if (len(memory) == 3):
            ram = memory[0]
            rom = memory[1]
            expandable = memory[2]
            # print(expandable)
        elif (len(memory) == 2):
            if (memory[1].endswith("GB" or "TB")):
                ram = "-"
                rom = memory[0]
                expandable = memory[1]
            elif (memory[0].endswith("ROM" or "Rom" or "rom")):
                ram = "-"
                rom = memory[0]
                expandable = memory[1]
            else:
                ram = memory[0]
                rom = memory[1]
                expandable = "-"
        ram_l.append(ram)
        rom_l.append(rom)
        exp_l.append(expandable)
        if(len(features)==5):
            display=features[1]
            camera=features[2]
            battary="not define"
            processor=features[3]
            warranty=features[4]
        elif(len(features)==6):
            display = features[1]
            camera = features[2]
            battary = features[3]
            processor = features[4]
            warranty = features[5]
        else:
            display = "not define"
            camera = "not define"
            battary = "not define"
            processor = "not define"
            warranty = "not define"
            # print(warranty)
        name_l.append(name)  # append all mobile phone names
        rating_l.append(rating)  # append all ratings
        price_l.append(price)# append all mobiles price
        display_l.append(display)
        camera_l.append(camera)
        battery_l.append(battary)
        processor_l.append(processor)
        warranty_l.append(warranty)

flipkart["Name"]=name_l
flipkart["Price"]=price_l
flipkart["Rating"]=rating_l
flipkart["Ram"]=ram_l
flipkart["Rom"]=rom_l
flipkart["Exp_Memory"]=exp_l
flipkart["Display"]=display_l
flipkart["Camera"]=camera_l
flipkart["Battery"]=battery_l
flipkart["Processor"]=processor_l
flipkart["Warranty"]=warranty_l

df=pd.DataFrame(flipkart,columns=["Name","Price","Ram","Rom","Exp_Memory","Rating","Display",'Camera',"Battery",'Processor',"Warranty"])
df.to_excel(r"C:\Users\Goutam\OneDrive\Desktop\WebScrapping\Full_Flipkart.xlsx",index=False)