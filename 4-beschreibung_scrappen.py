from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_argument("lang=de-DE, de,en-US,en")
options.add_argument("--user-data-dir=C:\\Users\\emilb\\Desktop\\Python_projekte\\BOTS\\Chrome_Profile\\GoogleChromeProfile 4")
options.add_argument("--profile-directory=Profile 4")

driver = uc.Chrome(executable_path=r'C:\Users\emilb\Desktop\Python_projekte\BOTS\driver\chromedriver.exe',options=options)  
driver.maximize_window() 

driver.get("https://www.instagram.com/oscar.karem/")

dic = {'Name':[],'Beschreibung':[]}

try:
  beschreibung_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_aa_c"]')))
  print(beschreibung_name.text)

except:
    pass