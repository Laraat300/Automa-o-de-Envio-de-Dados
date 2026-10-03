#Passo 1: Entrar no sistema da empresa 
#Passo 2: Fazer login
#Passo 3: Importar a base de produtos pra cadastrar
#Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

#importar a biblioteca de automação
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

#Passo 1: Entrar no sistema da empresa 
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("ENTER")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("ENTER")

#fazer pausa para abrir o site
time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=797, y=410)
pyautogui.write("batata@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("enter")

#Passo 3: Importar a base de produtos pra cadastrar

#ler a tabela emostrar
tabela = pd.read_csv("produtos.csv")
print (tabela)

#Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim
#para cada linha dentro da tabela / index = linha columns = coluna
for linha in tabela.index:
    pyautogui.click(x=766, y=285)

#localizar a primeira linha(codigo) da tabela
    codigo = tabela.loc[linha, "codigo"]
#cadastar os produtos e colocar em str para n dar conflico por ter numeros
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

#se a linha obs nao for NA(vazia) ele executa oq esta escrito
    if not pd.isna("obs"):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

#scrolar para o inicio da tela
    pyautogui.scroll(500)
