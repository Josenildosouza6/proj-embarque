# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)

Copyright(c) Josenildo
"""

"""
Esse script tem informações sobre a criptografia e descriptografia dos usuarios e elementos
onde essas infromações será salvas nos arquivos chamados 'Usuarios.txt' e 'elementos.txt'
respectivamente. 
"""

dic_elementos = {}
dic_usuario = {}
dic_usuario = {'adm':('adm', '0')}


def recuperar_chaves(arq):
    """Recupera os valores que constam nos atquivos 'CahvesPublicas e Privadas"""
    
    arquivo = open (arq, 'r')
    linha = arquivo.readline()
    arquivo.close()
    aux = ''
    for c in linha:
        if c != ' ':
            aux += c
        else:
            num1 = int(aux)
            aux = ''
    num2 = int(aux)
    return num1, num2


def criptografar_string(string, e, n):
    """
    Faz a criptografia das stringas inseridas no arquivo.
    """
    
    codigo = ''
    for x in string:
        y = (ord(x)**e)%n
        codigo += str(y)+'#'
    return codigo


def decifrar_codigo(string, d, n):
    """
    Faz a descriptografia das strings inseridas no arquivos.
    """
    
    texto = ''
    aux = ''
    for c in string:
        if c != '#' and c != '\n':
            aux += c
        elif c != '\n':
            y = int(aux)
            aux = ''
            x = chr((y**d)%n)
            texto += x
    return texto


def criptografar_usuarios(dic_usuario, arq):
    """
    Faz a criptografia dos usuarios inseridos no dicionario de usuario(login e a senha)
    """
    
    arquivo = open(arq, "a")
    e, n = recuperar_chaves("chavePublica.txt")
    for chave in dic_usuario:
        arquivo.write(criptografar_string(chave, e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_usuario[chave][0], e, n))
        arquivo.write("\n")
        arquivo.write(str(dic_usuario[chave][1]))
        arquivo.write("\n")
    arquivo.close()


def decifrar_usuarios(arq, dic_usuario):
    """
    Faz a descriptografia dos usuarios inseridos no dicionario de usuario(login e a senha)
    """
    
    arquivo = open(arq, "r")
    d, n = recuperar_chaves("chavePrivada.txt")
    linha = arquivo.readline()
    while linha != "":
        chave = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        senha = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        acesso = int(linha[0])
        dic_usuario[chave] = (senha, acesso)
        linha = arquivo.readline()
        if linha == "\n":
            linha = arquivo.readline()


def criptografar_elementos(dic_elementos, arq):
    """
    Faz a criptografia dos dados dos tripulantes inseridos no dicionario de 
    elementos(cpf, nome, função, datade nascimento e etc).
    """
    
    arquivo = open(arq, "a")
    e, n  = recuperar_chaves("chavePublica.txt")
    for chave in dic_elementos:
        arquivo.write(criptografar_string(chave, e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][0], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][1], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][2], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][3], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][4], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][5], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][6], e, n))
        arquivo.write("\n")
    arquivo.close()
     

def descriptografar_elementos(arq, dic_elementos):
    """
    Faz a descriptografia dos dados dos tripulantes inseridos no dicionario de 
    elementos(cpf, nome, função, datade nascimento e etc).
    """
    
    arquivo = open(arq, "r")
    d, n = recuperar_chaves("chavePrivada.txt")
    linha = arquivo.readline()
    while linha != "":
        chave = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        nome = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        funcao = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        data_de_nascimento = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        data_de_embarque = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        porto_de_referencia = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        passaporte = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        matricula = decifrar_codigo(linha, d, n)
        dic_elementos[chave]=(nome, funcao, data_de_nascimento, data_de_embarque, porto_de_referencia, passaporte, matricula)
        linha = arquivo.readline()

        if linha == "\n":
            linha = arquivo.readline()
    return dic_elementos


