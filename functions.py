from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os, time

contas = {}
y = 0


def login():
    while True:
        os.system("cls")
        print("Tela de Login")
        print()
        usuario = input("Insira o nome de seu usuário\n>>> ")
        senha = input("Insira sua senha\n>>> ")
        os.system("pause")
        for key, valores in contas.items():
            nome, usuario_stored, senha_stored = valores
            if usuario_stored == usuario and senha_stored == senha:
                menu()
                return

        os.system("cls")
        print("Senha ou Usuário incorreto!!")
        os.system("pause")


def cadastro():
    while True:
        os.system("cls")
        print("Tela de Cadastro")
        print()
        y = 1
        nome = input("Insira seu nome completo\n>>> ")
        usuario = input("Insira o seu usuario\n>>> ")
        senha = input("Insira sua senha\n>>> ")
        csenha = input("Comfirme sua senha\n>>> ")
        contas[y] = (nome, usuario, senha)
        os.system("pause")
        if senha == csenha:
            login()

        else:
            os.system("cls")
            print("Algo deu errado, tente novamente!!")
            os.system("pause")

def menu():
    while True:
        os.system("cls")
        print("Menu do Código")
        print()
        print("01 - Site do Senai")
        print("02 - Secretario do Senai")
        print("03 - Cursos EAD do Senai")
        print("04 - Cursos do Senai")
        print("05 - Sair")
        escolha = input(">>> ")

        if escolha == 1:
            os.system("cls")
            print("Você sera redirecionado ao site do Senai")
            driver = webdriver.Chrome()
            driver.get('https://sp.senai.br/unidade/jundiai/')
            os.system("pause")
            menu()

        if escolha == 2:
            os.system("cls")
            print("Você sera redirecionado a Secretaria do Senai")
            driver = webdriver.Chrome()
            driver.get('https://secretariadigital.sp.senai.br/')
            os.system("pause")
            menu()

        if escolha == 3:
            os.system("cls")
            print("Você sera redirecionado ao site de cursos EAD Senai")
            driver = webdriver.Chrome()
            driver.get('https://ead.sp.senai.br/')
            os.system("pause")
            menu()

        if escolha == 4:
            os.system("cls")
            print("Você sera redirecionado a area de Cursos do Senai")
            driver = webdriver.Chrome()
            driver.get('https://sp.senai.br/unidade/jundiai/')
            driver.find_element(By.XPATH, '//*[@id="escola"]/div/div/div[2]/div/div[2]/div/div[4]/div/a').click()
            os.system("pause")  
            menu()

        if escolha == 5:
            os.system("cls")
            print("Obrigado por testar o código!!!")
            time.sleep(5)
            break