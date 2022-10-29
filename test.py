#Luego de tener esto hecho Tengo que hacer que me detecte la paguina que se me abre
#Utilizar requests para mandar el  json
#Tener la opcion de #options.headless = True para q no  me abra el navegador 
#Preguntar si lo mando por json y post
#Optimizar para que lo haga con mas de 2 datos en una fila -table
#Validar por si no existe el dato en el input
#Ice key 4000042139


# Librerías

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
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
options.headless = True

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
cont =0
datos = []
error = False
#Recorre Tabla
pathul ='//*[@id="paging"]/ul'
if find_element(pathul):

    #Esta es la parte hecha para que me                               
    elementos=driver.find_elements(By.XPATH,'//*[@id="paging"]/ul/li/a')
    tamano = len(elementos)
    #print(tamano)

    #El for asi ya que empieza en el likn numero a[1] = 2 y luego el kink a[2]=3
    for x in range (0 , tamano+1):
        print(x)

        rows = driver.find_elements(By.XPATH,"//table[@class='eptable']/tbody/tr") 
        
        row_count = len (rows)+1
        
        if(x==0):
            for i in range(2,row_count):
            
                Nombre = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[1]")
                link = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]/a[1]")
                link.click()
                cont= 15
                while error == False: 
                    if find_element("/html/body/div/div/div[2]/table[3]/tbody/tr["+str(cont)+"]/td[2]/b"):
                        Fecha_Cierre = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/table[3]/tbody/tr["+str(cont)+"]/td[2]/b").text
                        error = True
                    else:
                        cont= cont-1

                driver.execute_script('history.go(-1);')

                Desc = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]")
                publi = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[3]")
                apert = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[4]")
                Estado = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[5]")

                info ={
                    'id': i,
                    
                }
            
                datos.append(info)
                error = False
        else:
            for i in range(2,row_count):
            
                
                link = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]/a[1]")
                link.click() 
                cont= 15

                while error == False: 
                    if find_element("/html/body/div/div/div[2]/table[3]/tbody/tr["+str(cont)+"]/td[2]/b"):
                        Fecha_Cierre = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/table[3]/tbody/tr["+str(cont)+"]/td[2]/b").text
                        error = True
                    else:
                        cont= cont-1
        
                driver.execute_script('history.go(-1);')
                Nombre = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[1]")
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
                    'Fecha Cierre': Fecha_Cierre
                }
            
                datos.append(info)
                error = False

        #Este va a ser el for para las filas


        if(x==tamano):
            break
        else:
            pagbuton = driver.find_element(By.XPATH,"//*[@id='paging']/ul/li/a["+str(x+1)+"]")
            
            time.sleep(5)
            pagbuton.click()                                        
            time.sleep(5)

print(json.dumps({"Concursos":datos}))
time.sleep(5)