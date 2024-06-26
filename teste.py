import math

print("Cadastro de devs")

nome = input("Coloque seu nome, dev: ")
apelido = input("coloque seu apelido, dev: ")
ids = int(input("Coloque o seu id (apenas numeros), dev: "))
ativo = "nao"

def ja_cadastrado():
    if nome == "Vinicius dos Santos Pereira":
        pass
    if apelido == "Tanmo" or apelido == "Vnzin" or apelido == "Hood":
        print("Apelido ja cadastrado, por favor coloque outro.")
        apelido = input("coloque seu apelido, dev: ")
        ativo = "simAp"
    if ids == 3225 or 4041:
        ativo = "simId"
        print("ID ja cadastrado!!")
        ids = int(input("Coloque o seu id (apenas numeros), dev: "))

ja_cadastrado()