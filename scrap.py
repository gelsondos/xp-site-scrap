from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv,sys
from datetime import datetime
from duplicates import find_duplicates_assets

# My Mac
driver = webdriver.Firefox(executable_path='/Users/gelson/Desktop/scrapproject/xp-site-scrap/geckodriver')

# My PC
#driver = webdriver.Chrome(executable_path="C:/Users/gdossantos/Downloads/scrapproject/xp-site-scrap/Drivers/chromedriver")

#driver.implicitly_wait(960) # seconds

driver.get("https://experiencia.xpi.com.br/minha-conta/#/carteira")

assets_csv=[]
assets_list=[]
try:
    print("start scrapping")
    element = WebDriverWait(driver, 560).until(
        EC.presence_of_element_located((By.ID, "patrimonio"))
    )
    page=driver.page_source
    soup = BeautifulSoup(page,'html.parser')
    
    #Filter the Assets NAME and TOTAL
    filter_div=soup.select("[class~=sc-xpqxbc-0] > span")
    if len(filter_div)==0:
        filter_div=soup.select("[class~=sc-rhhuh9-0] > span")

    len_filter=len(filter_div)
    if len_filter> 0:
        print(f'start computing data name x total, len= {len_filter}')
    else:
        print(f'ERROR 1 - NO FOUND DATA IN FILTER name x total, assets = {len_filter}')

    with open("data.csv", 'w' ,newline='') as f:
        writer=csv.writer(f)
        timestamp=datetime.now()
        
        print("Start CSV")
        for assets in filter_div:
            filter_p=assets.select("p")
            name=filter_p[0].get_text()
            money=filter_p[1].get_text()
            percentage=filter_p[2].get_text()
        
            assets_data=[name,money,percentage,timestamp]
            assets_list.append(assets_data)
        
        assets_list_duplicates=find_duplicates_assets(assets_list)

        for assets in assets_list_duplicates:
            writer.writerow(assets)
            assets_csv.append(assets)
        
        print("End CSV")
            

    
finally:
    driver.quit()