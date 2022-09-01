import time
import random
import schedule
from random import randint 
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def sendmessages():
    options=webdriver.ChromeOptions()
    options.add_argument("lang=de-DE,de,en-US,en")
    options.add_argument("--user-data-dir=C:\\Users\\emilb\\Desktop\\Python_projekte\\BOTS\\Chrome_Profile\\GoogleChromeProfile2")
    options.add_argument("--profile-directory=Profile2")   
    options.add_argument(f'user-agent=Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.58 Mobile Safari/537.36') 
        
    driver = uc.Chrome(executable_path=r'C:\Users\emilb\Desktop\Python_projekte\BOTS\driver\chromedriver.exe',options=options)    
    driver.maximize_window() 

    instagram = "https://www.instagram.com/"  #Variablen Initialisieren um sie für später zu nutzen.
    name_der_txt_datei = r'C:\Users\emilb\Desktop\Business_mit_Nic\Insta_Bot\Oscar_Karem\oscar.karim.txt'  #Der Pfad zur Datei mit den Namen in einer Liste
    
    von_zeit = 1   #Zeitliche verzögerungen
    bis_zeit = 6 
    
    von_zeit1 = 1  #Zeitliche verzögerungen
    bis_zeit1= 3


    link_mit_nutzer, nutzer_name = "",""  #Der link_mit_nutzer dient als leerer link_mit_nutzer um daraus den Link mit dem User zu bilden
    angeschrieben, wie_viele_anschreiben = [], 0
    nachrichten = []

    with open(name_der_txt_datei, 'r') as file:  #Leuten aus der Liste die Nachricht schreiben
     text = file.readlines()
    
    schon_angeschrieben = open(r"C:\Users\emilb\Desktop\Business_mit_Nic\Insta_Bot\Oscar_Karem\angeschrieben.txt", 'r') #Ist die Liste mit den schon angeschriebenen Namen und Prüfen ob schon angeschrieben habe

    for user in text:

     if  wie_viele_anschreiben == 19:  #Wenn 100 leute angeschrieben dann break und 
      driver.quit()  #Den Driver quiten
      break

     link_mit_nutzer = instagram + user.strip()  #Txt in link_mit_nutzer umwandeln um die \n rauszubekommen   und jedes mal auf den Link von Insta resetten.
     nutzer_name =user.strip()  #Falls der User Privat auf der Instapage hat, dann muss ich den Namen später über die Inbox suchen.
     
     if (nutzer_name+"\n") in schon_angeschrieben:  #Wenn User schon angeschrieben wurde, ein Nutzername weiter in der Liste prüfen.
       continue
     
    
     try:
      time.sleep(randint(von_zeit,bis_zeit))   #Wartezeit bevor auf neues Profil geht
      driver.get(link_mit_nutzer) #Auf die Seite des Profiles gehen
     
      try:
       benachrichtungs_button= WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="_a9-- _a9_1"]'))) #Falls Benachrichtunfs Feld aufploppt
       benachrichtungs_button.click()
        
      except:
       print("Kein Benachrichtungs Button .. gehe weiter\n") 



     except NoSuchElementException as exception:
      print(exception)
      pass

     try:
      link_weiter = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_ab8w  _ab94 _ab99 _ab9h _ab9m _ab9p  _aba4 _abag _abcm"]//*//*//*')))  #Testen ob Die seite nicht verfügbar ist dann auf gehe zurück zu Instagram clicken und continue machen.
      link_weiter.click()
      
      print("Nutzer existiert nicht")

      angeschrieben = [nutzer_name+"\n"]  #Der User der angeschrieben wurde.
      with open(r'C:\Users\emilb\Desktop\Business_mit_Nic\Insta_Bot\Oscar_Karem\angeschrieben.txt', mode="a") as file:  #Fügt der Liste den User nach jedem Durchgang der Liste hinzu fall es mal abstürz oder zu lange dauert und damit es keine Duplicate gibt.
        file.write('\n'.join(angeschrieben))
      
      continue
       
     except :
      print(str(wie_viele_anschreiben)+"User existiert...")
      pass

     time.sleep(randint(1,5))  #Paar Sekunden auf der Insta Seite vom User warten.
     try:  #Nachrichen Button von der Instapage suchen, nicht Jeder user hat diese Option(Bei Privat nicht)
      time.sleep(2)
      button_nachrichten_finden = driver.find_element(by=By.XPATH, value='//button[@class="_acan _acap _acat"]') #Nachrichten Buttom vom User auf der Insta Page suchen.
      button_nachrichten_finden.click()  #Nachrichen Button clicken
      
      print("Normalen Nachrichten Button gefunden")
     
     except NoSuchElementException as exception:  #Funktion für den anderen Nachrichtenweg
        print(str(wie_viele_anschreiben)+"User hat kein Nachrichten Button auf der Instagram Page ... gehe anderen Weg .....\n")
        
        driver.get("https://www.instagram.com/direct/inbox/")
        
        try:
         benachrichtungs_button= WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="_a9-- _a9_1"]'))) #Falls Benachrichtunfs Feld aufploppt
         benachrichtungs_button.click()
        
        except:
         print("Kein Benachrichtungs Button .. gehe weiter\n") 
        
        time.sleep(randint(von_zeit,bis_zeit)) 
        anderer_weg_button_finden= WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_aa4m _aa4p"]//*')))
        
        time.sleep(randint(von_zeit,bis_zeit)) 
        anderer_weg_button_finden.click()  #Button zum suchen der User clicken
       
        time.sleep(randint(von_zeit,bis_zeit)) 
        element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class=" _aa2u"]//*')))  #User suchen in der Bar
   
        time.sleep(randint(von_zeit,bis_zeit)) 
        element.send_keys(nutzer_name)  #User eingeben
        
        time.sleep(randint(von_zeit1,bis_zeit1))   
        cirkel_auswählen = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm"]//*//*//*//*//*//*//*'))) #Cirkle auswählen

        time.sleep(randint(von_zeit1,bis_zeit1)) 
        cirkel_auswählen.click()  #Cirkel vom User auswählen

        time.sleep(randint(von_zeit1,bis_zeit1)) 
        user_weiter_clicken = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_ac7b _ac7d"]//*//*')))

        time.sleep(randint(von_zeit1,bis_zeit1)) 
        user_weiter_clicken.click()  #Weiter clicken

     time.sleep(randint(von_zeit,bis_zeit)) 
     try:  #Nachrichten schreiben Funktion
      time.sleep(5)
      nachricht_schreiben = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _abbh _abcm"]//*'))) #Warten bis Nachrichten Feld located ist
      
      time.sleep(randint(von_zeit1,bis_zeit1))
      nachrichten = ["Guten Tag ","Hey "+" alles klar bei dir?"," Hey "+" wie gehts wie stehts?"]
      nachricht_schreiben.send_keys(random.choice(nachrichten))  #Hier kommt die Nachricht rein

     except NoSuchElementException as exception:
       print(exception)
       pass

     
     try:
      time.sleep(randint(von_zeit1,bis_zeit1)) 
      nachricht_senden = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abbi _abcm"]//*')))  #Findet senden button

      time.sleep(randint(von_zeit1,bis_zeit1)) 
      nachricht_senden.click()  #Schickt nachricht ab
      

     except NoSuchElementException as exception:
        print(exception)
        pass

     try:
      angeschrieben = [nutzer_name+'\n']  #Der User der angeschrieben wurde.
      with open(r'C:\Users\emilb\Desktop\Business_mit_Nic\Insta_Bot\Oscar_Karem\angeschrieben.txt', mode="a") as file:  #Fügt der Liste den User nach jedem Durchgang der Liste hinzu fall es mal abstürz oder zu lange dauert und damit es keine Duplicate gibt.
        file.write('\n'.join(angeschrieben))

     except Exception as e:
      print(e)
      pass

     try:
      wie_viele_anschreiben +=1  #Der Counter der abbricht, wenn ich die Anzahl der verschickten Nachrichten erreicht habe.

     except Exception as e:
      print(e)
      pass



if __name__ == "__main__":

   sendmessages() 

   
  



    
