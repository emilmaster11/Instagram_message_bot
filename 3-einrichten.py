import time
import schedule
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Den Account von den Typen morgen kurz einrichten und dann den Bot laufen lassen.

options=webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\emilb\\Desktop\\Python_projekte\\BOTS\\Chrome_Profile\\GoogleChromeProfile5")
options.add_argument("--profile-directory=Profile5")
###UserAgent einstellen auf meinen Browser  damit es richtig aussieht
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"')

driver = webdriver.Chrome(executable_path=r'C:\Users\emilb\Desktop\Python_projekte\BOTS\driver\chromedriver.exe',options=options)
driver.get("google.de")
time.slee(100)