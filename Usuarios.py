# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)

Copyright(c) Josenildo 
"""

"""
Esse script contém funções para realizar o cadastro dos usuarios, remover um usuario desejado
e alterar o nivel de um usuario caso assim desejar.
"""

dic_elementos ={}
dic_usuario = {}
dic_usuario["adm"]=("adm", "0")


def cadastrar_usuario(dic_usuario):
    '''
    Essa função vai varrer o dicionario de usuarios e verificar se o login ja existe
    caso ele ja exista vai informar que o usuario ja esta cadastrado.
    se não estiver cadastrado, cadastra o login, senha e nivel de usuario.
    '''
    
    continua = True
    while continua == True:
        login = input("Digite o Login: ")
                
        if login in dic_usuario:

            print("Usuario ja cadastrado!")
            continua = False
            

        else:
           senha = input("Digite a senha: ")
           nivel_usuario = 3
           print("Usuario Cadastrado com Sucesso!")
           dic_usuario[login]=(senha, nivel_usuario)
           continua = False


def remover_usuario(dic_usuario):
    '''
    Essa função varre o dicionario atraves da chave "login", se encontar o login solicitado ela
    remove o usuario, se não encontrar ela mostra usuario não encontrado.   
    '''
    
    login=input("Digite o login que deseja remover: ")
    continua = True
    while continua == True:
        if login in dic_usuario:
            dic_usuario.pop(login)
            print("Login: ",login,"removido!")
            continua = False 
                
        else:
            entrada=input("Usuario nao encontrado, deseja buscar outro?(s/n) ")
            if entrada=="s":
                continua=True
            elif entrada=="n":
                continua=False


def alterar_nivel_usuario(dic_usuario):
    '''
    Essa função altera o nivel do nivel do usuario, verifica se o login existe no dicionario de usuarios
    se o login existir, pede pra trocar o nivel de usuario de acordo com o nivel que desejar. se não
    mostra usuario não cadastrado.
    '''
    
    login = input("Digite o login que deseja modificar: ")
    continua = True
    while continua == True:
        if login in dic_usuario:           
            print("Login Localizado!")
            novo_nivel = input("Digite o novo nivel do usuario"+login+":")
            dic_usuario[login] = (dic_usuario[login][0], novo_nivel)
            continua = False
       
        else:
            entrada=input("Usuario nao encontrado, deseja buscar outro?(s/n) ")
            if entrada=="s":
                continua=True
            elif entrada=="n":
                continua=False