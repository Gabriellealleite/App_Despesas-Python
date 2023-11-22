"""
Desenvolva um aplicativo que registra despesas e receitas. Use arquivos para salvar os dados 
e faça requisições a uma API de cotação de moedas para atualizar valores em diferentes moedas 
(da escolha do usuário). Além disso, permite que o usuário registre, pesquise, liste, edite e 
delete despesas ou receitas.
"""

import requests


# API
url = "http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,JPY-BRL"
resposta = requests.get(url)
#print(resposta.json())


# Variáveis
subtitulo = "Escolhas do Usuário"
despesas = 0
saldo = 0
total_despesas = 0
dic_receita = {}
dic_despesas = {}
escolhas = [
    "adicionar receita",
    "pesquisar despesas",
    "editar despesas",
    "remover despesas"
]
moedas = ['USD', 'EUR', 'JPY']
USD = float(resposta.json()['USDBRL']['bid'])
EUR = float(resposta.json()['EURBRL']['bid'])
JPY = float(resposta.json()['JPYBRL']['bid'])
title_USD = "Dólar"
title_EUR = "Euro"
title_JPY = "Iene Japonês"

#USD_BRL = USD * 


# Função 1
def adc_receita():
    print("=-" * 41)
    nova_receita = float(input("Qual o valor da nova receita: "))
    print(f"Nova receita adicionada com sucesso!!")
    print(f"Saldo atual: {nova_receita}")
    print("=-" * 41)
    return nova_receita


# Função 2
def pesquisar_despesa(dic_despesas):
    print("=-" * 41)
    pesquisa = input("Nome da despesa: ").lower()
    
    result = dic_despesas[pesquisa]
    print (f"Sua despesa com '{pesquisa}' foi: R$ {result}")
    print("=-" * 41)


# Função 3
def editar_despesas(dic_despesas):
    print("=-" * 41)
    for despesa, valor in dic_despesas.items():
        print(f"Despesa: '{despesa}' \tValor: R$ {valor}")
    despesa_selecionada = input("Qual despesa deseja editar: ")
    valor_nova_despesa = int(input(f"Qual será o novo valor de '{despesa_selecionada}': "))
    print(f"O valor de '{despesa_selecionada}' foi alterado para '{valor_nova_despesa}'!!")
    dic_despesas[despesa_selecionada] = valor_nova_despesa
    #print(dic_despesas)
    print("=-" * 41)
    #return dic_despesas


# Função 4
def remover_despesas(dic_despesas):
    print("=-" * 41)
    for despesa, valor in dic_despesas.items():
        print(f"Despesa: '{despesa}' \tValor: R$ {valor}")
    despesa_removida = input("Qual despesa deseja remover: ")
    dic_despesas.pop(despesa_removida)
    print(f"A despesa '{despesa_removida}' foi removida com sucesso!!")
    print(dic_despesas)
    print("=-" * 41)


# Função 5
def alterar_moeda(dic_despesas):
    

    print("Para qual moeda deseja alterar ['USD'] ['EUR'] ['JPY']")
    escolha_moeda = input("Sua escolha: ")

    if escolha_moeda == moedas[0]:
        
        print("")
        print(f"\033[43m{title_USD:=^82}\033[m")
        print(f"Sua receita total em Dólar será: $ \033[32m{receita * USD:.2}\033[m")
        print(f"Seu total de despesas em Dólar será: $ \033[31m{total_despesas * USD:.2}\033[m")
        if saldo > 0:
            print(f"Seu saldo atual em Dólar é: $ \033[32m{saldo * USD:.2}\033[m")
        elif saldo < 0:
            print(f"Seu saldo atual em Dólar é: $ \033[31m{saldo * USD:.2}\033[m")
        else:
            print(f"Seu saldo atual em Dólar é: $ {saldo * USD:.2}")

    if escolha_moeda == moedas[1]:
        
        print("")
        print(f"\033[46m{title_EUR:=^82}\033[m")
        print(f"Sua receita total em Euro será: € \033[32m{receita * EUR:.2}\033[m")
        print(f"Seu total de despesas em Euro será: € \033[31m{total_despesas * EUR:.2}\033[m")
        if saldo > 0:
            print(f"Seu saldo atual em Euro é: € \033[32m{saldo * EUR:.2}\033[m")
        elif saldo < 0:
            print(f"Seu saldo atual em Euro é: € \033[31m{saldo * EUR:.2}\033[m")
        else:
            print(f"Seu saldo atual em Euro é: € {saldo * EUR:.2}")


    if escolha_moeda == moedas[2]:
        
        print("")
        print(f"\033[46m{title_JPY:=^82}\033[m")
        print(f"Sua receita total em Iêne será: ¥ \033[32m{receita * JPY:.3}\033[m")
        print(f"Seu total de despesas em Iêne será: ¥ \033[31m{total_despesas * JPY:.3}\033[m")
        if saldo > 0:
            print(f"Seu saldo atual em Iêne é: ¥ \033[32m{saldo * JPY:.3}\033[m")
        elif saldo < 0:
            print(f"Seu saldo atual em Iêne é: ¥ \033[31m{saldo * JPY:.3}\033[m")
        else:
            print(f"Seu saldo atual em Iêne é: ¥ {saldo * JPY:.3}")


    print("=-" * 41)
    print("")


# Título
titulo = "Aplicativo de Despesas"
print(f"\033[1;44m{titulo:=^82}\033[m")
print("")


# Funcionamento

receita = float(input("Informe quanto foi a sua receita: "))
while True:
    # Inicial
    nome_despesas = input("Nome da despesa: ").lower()
    valor_despesas = float(input(f"Valor da despesa '{nome_despesas}': "))
    dic_despesas[nome_despesas] = valor_despesas
    #    print(dic_despesas)
    total_despesas += valor_despesas
    saldo = receita - total_despesas

    # Impressões


    # Listagem de itens
    print("=-" * 41)
    print(dic_despesas)
    print("=-" * 41)

    while True:
        # Escolhas usuário
        print(f"\033[1;42m{subtitulo:=^82}\033[m")
        print(escolhas)
        escolha_usuario = input("Sua escolha ['' para sair]: ").lower()


        #Verificação continuar
        if escolha_usuario == '':
            break


        # Adicionar nova receita
        if escolha_usuario == escolhas[0]:
            nova_receita = adc_receita()
            receita = receita + nova_receita

        
        # Pesquisar despesas
        if escolha_usuario == escolhas[1]:
            pesquisar_despesa(dic_despesas)


        # Editar despesas
        if escolha_usuario == escolhas[2]:
            editar_despesas(dic_despesas)

        
        # Remover despesas
        if escolha_usuario == escolhas[3]:
            remover_despesas(dic_despesas)

        
        """# Alterar moeda
        if escolha_usuario == escolhas[4]:
            alterar_moeda(dic_despesas)"""


    # Verificação continuação
    while True:
        resp = input("Deseja adicionar novas despesas? [S/N] ").strip().upper()[0]
        if resp in "SN":
            break
        print("ERRO! Por favor, digite apenas S ou N")
    if resp == "N":
        break


# Impressão 2
print("")
print("=-" * 41)
print(f"Sua receita total foi: R$ \033[32m{receita}\033[m")
print(f"Seu total de despesas foram: R$ \033[31m{total_despesas}\033[m")
if saldo > 0:
    print(f"Seu saldo atual é: R$ \033[32m{saldo}\033[m")
elif saldo < 0:
    print(f"Seu saldo atual é: R$ \033[31m{saldo}\033[m")
else:
    print(f"Seu saldo atual é: R$ {saldo}")


#Alteração de moeda
print("=-" * 41)

while True:
    verificacao_alterar_moeda = input("Deseja alterar a moeda [S/N]").strip().upper()[0]
    if verificacao_alterar_moeda == "N":
        
        break
    if verificacao_alterar_moeda == "S":
        alterar_moeda(dic_despesas)