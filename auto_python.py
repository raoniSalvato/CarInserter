from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

navegador = webdriver.Firefox()

lista_carros = [['VOLKSWAGEN', 'VOLKSWAGEN VOYAGE 1.6 MSI FLEX 16V 4P AUT', '2019', 'Automático', 'Sedã','Prata', '49999', 'Vila Velha'], ['FORD', 'FORD KA+ SEDAN 1.0 TIVCT FLEX 4P', '2019', 'Manual','Hatch', 'Prata', '55000', 'Vila Velha'], ['VOLKSWAGEN', 'VOLKSWAGEN VOYAGE TRENDLINE 1.6 T.FLEX8V 4P', '2018', 'Manual', 'Sedã', 'Branco', '53900', 'Vitória'], ['CHEVROLET', 'CHEVROLET PRISMASED. LT 1.4 8V FLEXPOWER 4P AUT.', '2019', 'Automático', 'Sedã', 'Preto', '49990', 'Serra'],['FORD', 'FORD KA 1.5 SEDAN SE 12V FLEX 4P MEC.', '2020', 'Manual', 'Sedã', 'Cinza', '56900','Vila Velha']]

def Login_Usuario():
    nome_usuario = navegador.find_element(By.ID,"username")
    nome_usuario.send_keys("raonibarbosa")

    senha = navegador.find_element(By.ID,"password")
    senha.send_keys("12345")

    time.sleep(3)
    botao_login = navegador.find_element(By.NAME,"submit")
    botao_login.click()

    botao_inserir_carro = navegador.find_element(By.XPATH,"/html/body/div/div/div/button")
    botao_inserir_carro.click()

def Cadastro_Carros():
    for carro in lista_carros:    
        marca = carro[0] 
        modelo = carro[1]
        ano = carro[2]
        cambio = carro[3]
        tipo = carro[4]
        cor = carro[5]
        valor = carro[6]
        municipio = carro[7]

        elemento_marca = navegador.find_element(By.ID, "marca")
        elemento_marca.send_keys(marca)

        elemento_modelo = navegador.find_element(By.ID, "modelo")
        elemento_modelo.send_keys(modelo)

        elemento_ano = navegador.find_element(By.ID, "ano")
        elemento_ano.send_keys(ano)

        if cambio == "Automático":
            elemento_cambio = navegador.find_element(By.ID, "cambioAutomatico")
            elemento_cambio.click()

        if tipo == "Sedã":
            elemnento_seda = navegador.find_element(By.ID, "c_sedan")
            elemnento_seda.click()    
        else :
            elemnento_hatch = navegador.find_element(By.ID, "c_hatch")
            elemnento_hatch.click()

        opcoes_cores = Select(navegador.find_element(By.ID, "cor"))
        if(cor == "Cinza"):
            opcoes_cores.select_by_value("outro")
        else:
            opcoes_cores.select_by_visible_text(cor) 

        elemento_valor = navegador.find_element(By.ID, "valor")
        elemento_valor.send_keys(valor)

        elemento_municipio = navegador.find_element(By.ID, "municipio")
        elemento_municipio.send_keys(municipio)

        time.sleep(3)
        botao_inserir = navegador.find_element(By.NAME, "insert")
        botao_inserir.click()

        time.sleep(3)
        botao_inserir_novo_carro = navegador.find_element('xpath', "/html/body/div/div/div[2]/button")
        botao_inserir_novo_carro.click()

navegador.get("http://weka.inf.ufes.br/IFESTP/login.php")
Login_Usuario()
Cadastro_Carros()
navegador.close()