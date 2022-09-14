import time
import hashlib
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def main(profil_name):
    options=webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=")
    options.add_argument("--profile-directory=Profile2")
    
    driver = uc.Chrome(executable_path=r'',options=options)
    driver.get("https://www.instagram.com/"+profil_name+"/followers/")
    
    print("Programm wartet paar Sekunden")
    
    time.sleep(5)
    user_liste_ = set()  #Hier werden die Gescrappten Daten gespeichert und vergliechen

    int = 0
    
    ###20  * 12 (12 Pro scrollen) = 240User
    while(int <200):
        
        
        time.sleep(2)
        try:
            time.sleep(2)
            list_of_people = driver.find_elements(By.XPATH, '//div[@class="_ab8w  _ab94 _ab99 _ab9h _ab9m _ab9o _abcm"]//*//*//*//*//*//*//*')
            
            user_liste_hinzufügen = [user_liste_.add(person.text) for person in list_of_people]
            user_liste_hinzufügen
            
            #Gucken ob die Comprehession darüber so funktionert.
            # for person in list_of_people:
            #     user_liste_.add(person.text)

           

            driver.execute_script("arguments[0].scrollIntoView(true);", list_of_people[-1])
            int += 1

            print("Programm wartet paar Sekunden")
            
            time.sleep(1)
            
        except NoSuchElementException as exception:
            print(exception)


    user_mit_dupps = r""
    
    with open(user_mit_dupps, mode="a") as file: 
     file.write("\n".join(user_liste_))

     
def dups_löschen():

    input_file_path = r''   #Input ist mit Dups
    output_file_path = r''  #Output ist ohne DUps

    completed_lines_hash = set()
    output_file = open(output_file_path, 'r+')

    for line in open(input_file_path, 'r'):
        
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        
        if hashValue not in completed_lines_hash:
            output_file.write(line)
            completed_lines_hash.add(hashValue)
		    

    output_file.close()


if __name__ == "__main__":
   main(profil_name="#Name of the Instagram Profil")
   #dups_löschen()
