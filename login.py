# !\bin\python
# -*- coding: utf-8 -*-
from os import getenv
from bottle import debug, run, get, post, template, request, redirect
from dotenv import load_dotenv

# Carregando o arquivo .env para as variáveis de 
# ambiente da sessão.
load_dotenv()

# Obtendo a variável LISTA_PORT da variável de
# ambiente que foi carregado no .env 
PORT = getenv("LISTA_PORT", 8080)

# Obtendo a variável LISTA_AMBIENTE da variável de
# ambiente que foi carregado no .env 
AMBIENTE = getenv("LISTA_AMBIENTE", "PROD")

# Verificando se o ambiente é DEV ou PROD
# DEV = desenvolvimento
# PROD = produção
dev_mode = AMBIENTE == "DEV"

# Ativar modo debug
debug(dev_mode)

# Lista de assinantes
assinantes = {
    "email1@example.com": "senha123",
    "email2@example.com": "abc456",
    "email3@example.com": "senha789"
}

# Rota para a tela de login
@get("/login")
def mostrar_formulario_login():
    return template("login")

# Rota para validar o login
@post("/login")
def validar_login():
    email = request.forms.get("email")
    senha = request.forms.get("senha")

    if email in assinantes and assinantes[email] == senha:
        return "Encontrado"
    else:
        return "Inexistente"

# Execução do servidor
# Parâmetros:
# - port: porta de escuta
# - reloader: atualizar o servidor ao editar o arquivo
run(port=PORT, reloader=dev_mode)
