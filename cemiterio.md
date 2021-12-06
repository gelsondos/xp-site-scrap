from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


driver = webdriver.Firefox(executable_path='/Users/gelson/Desktop/scrapproject/geckodriver')

#driver.implicitly_wait(960) # seconds

driver.get("https://experiencia.xpi.com.br/minha-conta/#/carteira")

try:
    element = WebDriverWait(driver, 560).until(
        EC.presence_of_element_located((By.ID, "patrimonio"))
    )
    element2=element.find_element(By.TAG_NAME, 'span')
    element3=element2.find_element(By.TAG_NAME, 'span')
    data=element3.get_attribute("outerHTML")
    soup = BeautifulSoup(data)
    print(soup.get_text())

    table=driver.find_element(By.CLASS_NAME, 'sc-8m7ew2-0 jCxMRh')
    table2=table.get_attribute('outerHTML')
    print(table2)
 

finally:
    driver.quit()

