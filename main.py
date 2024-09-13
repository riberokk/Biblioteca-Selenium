from functions import *
import os


while True:
    print("Menu de Login")
    print()
    print("01 - Logar")
    print("02 - Cadastrar")
    print("03 - Sair")
    inputl = int(input(">>> "))

    if inputl == 1:
        login()

    elif inputl == 2:
        cadastro()

    elif inputl == 3:
        os.system("cls")
        print("Você escolheu a opção sair, obrigado por testar o código!!")
        os.system("pause")
        break