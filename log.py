# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)

Copyright(c) Josenildo 
"""

"""
Esse script contem informações que serão salvas em um arquivo chamado 'log.txt',
o qual estará as informações registradas sobre as atividades dos usuarios com a data e a hr da realização dessas atividades.

"""

import data as dt

#def busca_user():
#pass

def Log(user, acao):
    arquivo = open ("log.txt", "a")
#    agr = datetime.now()
    arquivo.write("{}: {} as {} {}\n.".format(user, acao, dt.hora(), dt.data()))
    arquivo.close()
    

def recuperar_usuario(linha):
    """
    Recupera os dados do usuario no arquivo.
    """
    
    user = ""
    for item in linha:
        if item != ":":
            user += item
        else:
            return user

def recuperar_data(linha):
    """recupera as datas  no arquivo em que essas estão salvas 
    referente as atividades dos usuarios"""
    
    data=""
    for item in linha:
        if item !=" ":
            data = ""
        elif item != " " and item != ".":
            data +=item
        return data


def ler_user(user):
    """
    Faz a leitura dos usuarios no arquivo.
    """
    arquivo = open ("log.txt", "r")
    acao = arquivo.readline()
    lista_acao=[]
    while acao != "":
        if recuperar_usuario(acao) == user:
            lista_acao.append(acao)
        acao = arquivo.readline()
    return lista_acao
 
           
def ler_data(data):
    """
    Faz a leitura das datas no arquivo.
    """
    arquivo = open("log.txt", "r")    
    acao = arquivo.readline()
    lista_acao=[]
    while acao != "":
        if recuperar_usuario(acao) == data:
            lista_acao.append(acao)
        acao = arquivo.readline()
    return lista_acao


'''
fazer umas busca a partir daqui
'''
def buscar_log():
    opcao = input("Digite a opção desejada de busca pelo log 1-Data, 2-Usuario ")
    if opcao == "1":
        resultado = ler_data()
        print(resultado)
        for linha in resultado:
            print (linha)
    elif opcao == "2":
        resultado = ler_user()
        print(resultado)
        for linha in resultado:
            print (linha)
    else:
        print("Essa opção nao eh valida!")
        
    
def comparar_datas():
    data_usuario = input("Digite a data (dd/mm/aaaa): ")
    palavra = open("log.txt", "r")
    lista = []
    linha = palavra.readline()
    while linha != "":
        data = recuperar_arquivo_log(linha)
        if str(data_usuario) == str(data):
            lista.append(linha)
        linha = palavra.readline()        
    return lista
   

def comparar_usuarios():
    user = input("Digite o usuario: ")
    palavra = open("log.txt", "r")
    lista_user=[]
    linha = palavra.readline()
    while linha != "":
        usuario = recuperar_arquivo_log(linha)
        if usuario == user:
            lista_user.append(linha)
        linha= palavra.readline()
    return lista_user


'''
def recuperar_arquivo(string):
    arq = open("log.txt", "a")
    agora=datetime.datetime.now()
    for item in arq:
    arquivo.write("{}: {} as {} {}\n".format(usuario, acao()+" "+ dt.hora()+" "+ dt.data())
    arq.close()
    
   
for c in string:
        if c != '#' and c != '\n':
            aux += c
        elif c != '\n':
            y = int(aux)
            aux = ''
            x = chr((y**d)%n)
            texto += x
    return texto
'''


def recuperar_data(palavra):
    data = ""
    for i in reversed(palavra):
        if i != " ":
            data +=i
        else:
            return data[-1::-1]

            
def recuperar_usuario(palavra):
    palavra = open("log.txt", "r")
    usuario = ""
    for i in palavra:
        if i !=" ":
            usuario +=i
        else:
            return usuario
'''