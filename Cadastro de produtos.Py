# A ideia aqui é que esse codigo automatize totalmente a tarefa "cadastro de produtos em um site de loja" pode ser adaptado para outros tipos de tarefas, importando outras bibliotecas, aqui é apenas um exemplo
# lendo o arquivo com os dados, indo ate o local de cadastro e cadastrando enquanto voce vai tomar um café :)
# Vou comentar cada passo que eu fizer, para ficar bem claro para analise, ou ate mesmo para voce que quer usar para estudo, fique a vontade. 

#  1- passo: abrir o navegador

import pyautogui
import time

# Vamos fazer uma pausa a cada click para evitar que os comandos se atrolpelem. 
pyautogui.PAUSE = 0.6
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# 2-Passo: Abrir o site. 

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep (0.8)

# 3-Passo: Fazer o loguin no site.

# print(pyautogui.position()) 
    # isso aqui serve para achar a posição do mouse, para a gente poder dizer ao pyautogui onde clicar.. e assim continuar com o processo. mas como nao é necessario apos achar a posição, vou deixar ele comentado, mas quando for usar e so usar sem o "#"

# time.sleep(5) 
    # aqui serve para dar uma pausa enquanto o site abre, pra dar tempo de tu ir la e por o mouse no lugar certo, se precisar de mais tempo subistitua o "2" por mais, lembrando que o python conta o sleep em segundos.. se passar o mouse la em cima do comndo consegue ver essa informação 

# Dica: perdi um bom tempo tentando fazer o codigo clicar no lugar certo, resolvi da seguinte forma, antes dele pegar as cordenadas, voce mesmo clica, assim ele vai ser mais preciso. 

pyautogui.click(x=930, y=423)
pyautogui.write('emailfakesopratestar@gmail.com') # Email do usuario
time.sleep(1) # coloquei esse sleep porque as vezes tava dando erro na senha, estava indo muito rapido, e como eu quero que fique 100% confiavel, coloquei um sleep aqui
pyautogui.press('tab') # tab para passar pra proxima linha, funciona fora do programa tambem, testa ai :) 
pyautogui.write('umasenhabemforte') # Senha do usuario 
pyautogui.press('tab') # Tambem serve para pular para botoes, podia pegar as cordenadas novamente, mas acho que assim vai ficar mais preciso
pyautogui.press('enter')

# time.sleep(5)
# print(pyautogui.position())

# 4-Passo: Aqui vou Importar a tabela que vou trabalhar

import pandas as pd 

tabela = pd.read_csv('produtos.csv')

print(tabela)

# 5-Passo: iniciando o cadastro dos produtos da nossa loja

for linha in tabela.index:
# Serve para localizar os itens da tabela
    pyautogui.click(x=757, y=290)
    # localizar onde o pyautogui vai clicar 
    codigo = tabela.loc[linha,'codigo']
    # Começar a puxar os dados da tabela
    pyautogui.write(codigo)
    # passar para o proximo iten da tabela 
    pyautogui.press('tab')
    # proximo campo 
    pyautogui.write(str(tabela.loc[linha,'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'custo']))
    pyautogui.press('tab')
    obs = tabela.loc[linha,'obs']
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha,'obs']))
        # ignora informações vazias da tabela citada, e preenche apenas se tiver algo
    pyautogui.press('tab')
    pyautogui.press('enter')
    #cadastra o produto, botao enviar 

    # 6-Passo Repetir o processo de cadastro enquanto houver informações na tabela 
    pyautogui.scroll(5000)
    #sobe a tela ate o inicio, para dar continuidade ao processo.