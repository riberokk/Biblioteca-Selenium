#Importa a biblioteca selenium e utiliza a função webdriver para controlar o navegador
from selenium import webdriver

#Importa a função By para identificar Id da pagina e facilia para encontrar elementos da pagina
from selenium.webdriver.common.by import By

#Importa a função Service para configurar o driver do navegador neste caso o ChromeDrive
from selenium.webdriver.chrome.service import Service

#Importa a biblioteca webdriver-manager e utiliza a função ChromeDriverManager, para excluir a nessecidade de instalar o driver de cada navegador
from webdriver_manager.chrome import ChromeDriverManager
import time

#Inicializando o driver


driver = webdriver.Chrome()

#Acessando o Google
driver.get("https://www.google.com")

#Encontrando a caixa de pesquisa e realizando uma ação
time.sleep(1)
driver.get('https://sp.senai.br/unidade/jundiai/')
driver.find_element(By.XPATH, '//*[@id="escola"]/div/div/div[2]/div/div[2]/div/div[4]/div/a').click()

#Fechando o navegador
time.sleep(2)
driver.quit()


#FUNÇÕES DE CADA LINHA

#service -> Nesta variavel ira instalar o driver de serviço da google
#driver -> Esta variavel ira inicializar o driver da google
#.get -> Insere o conteudo comentado ah caixa de entrada do navegador
#driver.quit -> Ira fechar o navegador utilizado
