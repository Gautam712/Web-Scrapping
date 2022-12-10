import pandas as pd
from bs4 import BeautifulSoup
import requests
name_l=[]
rating_l=[]
price_l=[]
ram_l=[]
rom_l=[]
expandable_l=[]
flipkart={}
for i in range(1,10):
    url=fr'https://www.flipkart.com/search?q=mobile+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=mobile+phone%7CMobiles&requestId=c04043e1-dbaa-4e9f-8b3c-af7fddef090d&as-backfill=on&page={i}'
    hlml_code=requests.get(url).content
    soup=BeautifulSoup(hlml_code,'lxml')

    phones=soup.find_all('div','_3pLy-c row')
    for phone in phones:
        name=phone.find('div','_4rR01T').get_text()
        check=phone.find('div','_3LWZlK')
        if(check is None):
            rating=0.0
        else:
            rating=float(check.get_text())
        price=int(phone.find('div','_30jeq3 _1_WHN1').get_text().replace('₹','').replace(',',''))
        details=phone.find_all('ul','_1xgFaf')
        for detail in details:
            memory=detail.find('li','rgWa7D').get_text().split('|')
            if(len(memory)>=3):
                ram=memory[0]
                rom=memory[1]
                expandble=memory[2]
            elif(len(memory)==2):
                if (memory[1].endswith('GB' or 'TB')):
                    expandble = memory[1]
                    rom=memory[0]
                    ram='-'
                elif(memory[0].endswith('ROM')):
                    ram='-'
                    rom=memory[0]
                    expandble=memory[1]
                else:
                    ram=memory[0]
                    rom=memory[1]
                    expandble='-'
            ram_l.append(ram)
            rom_l.append(rom)
            expandable_l.append(expandble)

        name_l.append(name)
        rating_l.append(rating)
        price_l.append(price)
flipkart['Name']=name_l
flipkart['Rating']=rating_l
flipkart['Ram']=ram_l
flipkart['Rom']=rom_l
flipkart['Price']=price_l
flipkart['Expandable_Memory']=expandable_l
df=pd.DataFrame(flipkart,columns=['Name','Rating','Ram','Rom','Price','Expandable_Memory'])
df.to_excel(r'C:\Users\Goutam\OneDrive\Desktop\WebScrapping\My_result.xlsx',index=False)