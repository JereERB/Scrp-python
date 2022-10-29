
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import time
#class Scrap():
#Ponerle el path para poder hacerlo con otros
def find_element(paths):
    try:
        #path de la tabla path ='//*[@id="paging"]/ul'
        driver.find_element(By.XPATH,paths)
        print("Si existe el elemento de pagination")
        return True    
    except:
        #Aca va el codigo para cuando no existe el pagination
        #  procedures = driver.find_element(by=By.TAG_NAME, value="tr")
        print("No existe el elemento de pagination")
        return False


# Opciones de navegación
options =  Options()

#Desactiva abrir el navegador
#options.headless = True

#ruta del ejecutable
PATH = "chromedriver\\chromedriver.exe"

#Driver => link
driver = webdriver.Chrome(PATH, options=options)
driver.get('https://www.sicop.go.cr/moduloOferta/search/EP_SEJ_COQ600.jsp')

#Accion para escribir el codigo del ICE
#time.sleep(3)


driver.execute_script('document.getElementsByName("cartelInstCd")[0].value=4000042139')
pro = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/form[1]/table/tbody/tr[5]/td/input[1]")
pro.send_keys('4000042139')
#time.sleep(3)


#Accion del boton buscar
pro = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/p/span/a")
pro.click()
#time.sleep(3)

datos = []
#Recorre Tabla
path ='//*[@id="paging"]/ul'
if find_element(path):
#path de la tabla path ='//*[@id="paging"]/ul'
    rows = driver.find_elements(By.XPATH,"//table[@class='eptable']/tbody/tr") 
        
    row_count = len (rows)+1
        
        #Este va a ser el for para las filas
    for i in range(2,row_count):
            
        Nombre = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[1]")

        link = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]/a[1]")
        link.click()

        Cierre = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/table[3]/tbody/tr[15]/td[2]/b").text
                                                

        driver.execute_script('history.go(-1);')

        Desc = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]")
        publi = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[3]")
        apert = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[4]")
        Estado = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[5]")

        info ={
            'id': i,
            'Nombre': Nombre.text,
            'Descripcion': Desc.text,
            'Fecha/hora de publicación' :publi.text,
            'Fecha/hora de apertura' : apert.text,
            'Estado del concurso' : Estado.text,
            'Fecha Cierre': Cierre
            }
            
        datos.append(info)
        
    print(json.dumps({"Concursos":datos}))
    time.sleep(5)

        