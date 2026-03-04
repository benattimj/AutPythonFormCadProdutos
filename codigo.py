# Bibliotecas = pacotes de código

import pyautogui
import time

pyautogui.PAUSE = 0.7

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# abrir o navegador

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

# Fazer o login
# Fazer uma pausa maior pro site carregar
time.sleep(3)

pyautogui.click(x=682, y=469)
pyautogui.write("pythonimpressionador@gmail.com")
time.sleep(0.1)
pyautogui.press("tab")
pyautogui.write("xxxx")
pyautogui.press("enter")

# Fazer uma pausa pro site carregar
time.sleep(1)


# Passo 3: Abrir a pasta de dados
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    # Passo 4: Cadastrar 1 Produto

    # Codigo
    pyautogui.click(x=652, y=313)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    time.sleep(0.1)
    pyautogui.press("tab")
    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    time.sleep(0.1)
    pyautogui.press("tab")
    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    time.sleep(0.1)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    time.sleep(0.1)
    pyautogui.press("tab")
    # preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    time.sleep(0.1)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    time.sleep(0.1)
    pyautogui.press("tab")
    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
   
    pyautogui.press("tab")  # Passar pro botão enviar


    pyautogui.press("enter") # clicar no botão enviar

    # Voltar pro inicio da tela

    pyautogui.scroll(10000)


# Passo 5: Repetir o passo 4 até acabar a lista de produtos
