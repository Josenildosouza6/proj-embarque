# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)

Copyright(c) Josenildo 

"""

"""
Esse scipt contem funções para fazer o cadastro dos elementos(Tripulantes), realizar uma busca de tripulantes peo cpf do memsmo, 
realizar uma de tripulantes pelo o seu cargo, remover um determinado tripulante, mostrar todos os tripulantes do dicionario de eleentos com todas
as suas informações, como cpf, nome data de nascimentos etc.
"""
#import Criptografia as cp

dic_elementos = {}


def cadastrar_elementos(dic_elementos):
    '''
    Faz uma varredura no dicionario de elementos, se o cpf do tripulante ja existir no mesmo
    aparece a mensagem de que esse cpf ja existe, se não a função cadastra o cpf e o restante das informações
    correspondente ao tripulante, como nome, cargo, data de nascimento etc.Fazer uma ordenação desses
    tripulantes de acordo com os seus cpfs e salver essas informações ordenadas em um arquivo chamado 'impressão.txt'.
    '''
    
    cpf = input("Digite o CPF do Tripulante: ")
    if cpf in dic_elementos:
            print("Esse CPF ja esta Cadastrado!")

    else:
        nome = input("Digite o nome do tripulante: ")
        funcao = input("Digite o cargo(Função) do tirpulante: ")
        data_de_nascimento = input("Digite a data de nascimento do tripulante: ")
        data_de_embarque = input("Digite a data de embarque: ")
        porto_de_referencia = input("Digite o porto de Referencia do tripulante: ")
        passaporte = input("Digite o nº do passaporte: ")
        matricula = input("Digite o nº da matricula: ")
        print("Tripulante Cadastrado com Sucesso!")
        dic_elementos[cpf]=(nome, funcao, data_de_nascimento, data_de_embarque, porto_de_referencia, passaporte, matricula)


def buscar_elementos(dic_elementos):
    '''
    Faz uma varredura no dicionario de elementos para buscar o tripulante atraves do cpf
    se o cpf não constar no dicionario de elementos, mostra os dados referentes ao tripulante buscado, se não existir mostra uma 
    de que o tripulante não existe.
    '''
    
    continua = True
    while continua == True:
        elemento_buscado = input("Digite o cpf do tripulante: ")

        if elemento_buscado in dic_elementos:
            print(dic_elementos[elemento_buscado])
            '''
            loog = login + str(data()) + 'Busca de tripulante efetuada'
            log(loog)
            '''
            escolha = input("Deseja outro Tripulante? (s/n) ")
            if escolha == "s":
                continua = True
            else:
                continua = False
        else:
            print("Tripulante nao encontrado em nosso banco de dados!")
            escolha1 = input("Deseja buscar outro Tripulante? s/n ")
            if escolha1 == "s":
                continua = True
            else:
                continua = False


def buscar_cargo(dic_elementos):
    '''
    Faz uma varredura no dicionario de elementos para buscar o tripulante atraves do cargo
    se o cargo não constar no dicionario de elementos, mostra os dados referentes ao tripulante buscado, se não existir mostra uma 
    de que o tripulante não existe.
    '''
        
    continua = True
    while continua == True:
        resultados = []
        cargo_buscado = input("Digite o cargo do tripulante: ")
        continua = False
        for cpf in dic_elementos:
            if dic_elementos[cpf][1] == cargo_buscado:
                resultados.append(dic_elementos[cpf])
        if len(resultados)== 0:
            print("Nenhum Tripulante com esse cargo")
            entrada = input("Deseja buscar outro Tripulante? (s/n) ")
            if entrada == "s":
                continua = True
            else:
                continua = False               
        else:
            for i in resultados:
                print(i)                
        

def remover_elementos(dic_elementos):
    '''
    Essa função varre o dicionario atraves da chave "cpf", se encontar o cpf solicitado ela
    remove o tripulante, se não encontrar ela mostra uma mensagem, Tripulante não encontrado.   
    '''
    
    continua = True
    while continua == True:
        cpf = input("Digite o cpf que deseja para remover o Tripulante: ")
        if cpf in dic_elementos:
            dic_elementos.pop(cpf)
            print("Tripulante Removido com Sucesso!")
            continua = False
    
        else:
            entrada=input("Tripulante nao encontrado, deseja buscar outro?(s/n) ")
            if entrada=="s":
                continua=True
            elif entrada=="n":
                continua=False
                    

def atualizar_elementos(dic_elementos):
    '''
    Essa função varre o dicionario atraves da chave "cpf", se encontar o cpf solicitado ela
    remove o tripulante, e o cadastra novamentecom os novos dados inseridos. se não encontrar ela mostra uma mensagem, Tripulante não encontrado.   
    '''
    
    continua = True
    while continua == True:
        cpf = input("Digite o cpf do Tripulante que vc quer atualizar: ")
        if cpf in dic_elementos:
            dic_elementos.pop(cpf)
            cadastrar_elementos(dic_elementos)
            print("Tripulante Atualizado com Sucesso!")
            continua = False
        else:
            continuar=input("Tripulante nao encontrado, deseja buscar outro?(s/n) ")
            if continuar=="s":
                continua=True
            elif continuar=="n":
                continua=False


def mostrar_todos_os_elementos(dic_elementos):
    '''
    Mostra uma mensagem de dicionario vazio caso este esteja assim.
    se não mostra todos o elementos que constam neste.
    '''
    
    if len(dic_elementos)==0:
        print("O dicionario de Tripulantes está vazio!")
    else:
        for chave in dic_elementos:
            print(dic_elementos[chave])
            

def ordenar_elementos(dic_elementos):
    '''
    Essa função varre o dicionario atraves da chave "cpf", adiciona taos os cpf 
    em uma lista vazia e ordena os cpf de acordo com o seu valor  
    '''
    
    lista = []
    for chave in dic_elementos:
        lista.append(chave)
    lista.sort()
    return lista

       
def impressao_ordenada(dic_elementos):
    '''
    Salva a ordenação dos elementos no arquivo "impressão.txt"  
    '''
    
    arq = open("impressao.txt", "w")
    lista = ordenar_elementos(dic_elementos)
    for chave in lista:
        arq.write(chave+':\n')
        arq.write("Nome: "+ dic_elementos[chave][0]+"\n")
        arq.write("Função: "+ dic_elementos[chave][1]+"\n")
        arq.write("Data de Nascimento: "+ dic_elementos[chave][2]+"\n")
        arq.write("Data de Embarque: "+ dic_elementos[chave][3]+"\n")
        arq.write("Porto de Referencia: "+ dic_elementos[chave][4]+"\n")
        arq.write("Passaporte: "+ dic_elementos[chave][5]+"\n")
        arq.write("Matricula: "+ dic_elementos[chave][6]+"\n\n")
    arq.close()