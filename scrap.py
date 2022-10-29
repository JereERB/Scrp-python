
from cgi import print_form
from os import system
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Scrapy():
    def __init__(self) :

        #Variable Inicalizadas
        
        self.options = Options()
        #self.options.headless = True
        self.PATH = "chromedriver\\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH, options=self.options)
        self.driver.get('https://www.sicop.go.cr/moduloOferta/search/EP_SEJ_COQ600.jsp')#URL
        self.datos = []
        self.cont =0
        self.error = False
        
    def first_window(self):
        #Primera ventana y Script para escribir en el txt que esta en readonly
        self.driver.execute_script('document.getElementsByName("cartelInstCd")[0].value=4000042139')
        #txt
        txt = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/form[1]/table/tbody/tr[5]/td/input[1]")
        txt.send_keys('4000042139')
        #Consultar
        btn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/p/span/a")
        btn.click()
        

    def secondo_window(self):
        pathul ='//*[@id="paging"]/ul'
        if self.__find_element(pathul):

            #Esta es la parte hecha para que me                               
            elementos=self.driver.find_elements(By.XPATH,'//*[@id="paging"]/ul/li/a')
            tamano = len(elementos)
            #print(tamano)

            #El for asi ya que empieza en el likn numero a[1] = 2 y luego el kink a[2]=3
            for x in range (0 , tamano+1):
            
                rows = self.driver.find_elements(By.XPATH,"//table[@class='eptable']/tbody/tr") 
            
                row_count = len (rows)+1
            
                if(x==0):
                    for i in range(2,row_count):
                
                        
                        link = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]/a[1]")
                        link.click()
                        cont= 15
                        while self.error == False: 
                            if self.__find_element("/html/body/div/div/div[2]/table[3]/tbody/tr["+str(cont)+"]/td[2]/b"):
                                Fecha_Cierre = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/table[3]/tbody/tr["+str(cont)+"]/td[2]/b").text
                                self.error = True
                            else:
                                cont= cont-1

                        self.driver.execute_script('history.go(-1);')
                        Nombre = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[1]")
                        Desc = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]")
                        publi = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[3]")
                        apert = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[4]")
                        Estado = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[5]")

                        info ={
                            'Nombre': Nombre.text,
                            'Descripcion': Desc.text,
                            'Fecha/hora de publicación' :publi.text,
                            'Fecha/hora de apertura' : apert.text,
                            'Estado del concurso' : Estado.text,
                            'Fecha Cierre': Fecha_Cierre
                        }
                    
                        self.datos.append(info)
                        self.error = False
                else:
                    for i in range(2,row_count):
                
                        
                        link = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]/a[1]")
                        link.click() 
                        cont= 15
                        while self.error == False: 
                            if self.__find_element("/html/body/div/div/div[2]/table[3]/tbody/tr["+str(cont)+"]/td[2]/b"):
                                Fecha_Cierre = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/table[3]/tbody/tr["+str(cont)+"]/td[2]/b").text
                                self.error = True
                            else:
                                cont= cont-1
                        self.driver.execute_script('history.go(-1);')
                        Nombre = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[1]")
                        Desc = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[2]")
                        publi = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[3]")
                        apert = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[4]")
                        Estado = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/table[2]/tbody/tr["+str(i)+"]/td[5]")

                        info ={                           
                            'Nombre': Nombre.text,
                            'Descripcion': Desc.text,
                            'Fecha/hora de publicación' :publi.text,
                            'Fecha/hora de apertura' : apert.text,
                            'Estado del concurso' : Estado.text,
                            'Fecha Cierre': Fecha_Cierre
                        }
                    
                        self.datos.append(info)
                        self.error = False
                #Este va a ser el for para las filas
                if(x==tamano):
                    break
                else:
                    pagbuton = self.driver.find_element(By.XPATH,"//*[@id='paging']/ul/li/a["+str(x+1)+"]")
                    pagbuton.click()                                              
        self.closescrap()
        return self.datos    
    
    def __find_element(self,path):
        #Lo que hace es encontrar el elemento segun el PATH
        try:
            #path de la tabla path ='//*[@id="paging"]/ul'
            self.driver.find_element(By.XPATH,path)
            #print("Si existe el elemento de pagination")
            return True    
        except:
            #Aca va el codigo para cuando no existe el pagination
            #  procedures = driver.find_element(by=By.TAG_NAME, value="tr")
            #print("No existe el elemento de pagination")
            return False
        
    
    def runscrap(self):
        self.first_window()
        self.secondo_window()

    def closescrap(self):
        self.driver.quit()

