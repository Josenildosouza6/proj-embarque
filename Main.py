# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)

Copyright(c) Josenildo 
"""
"""
Esse script contem informações sobre onivel dos usuarios, o login, o menu principal, e o logout e a criação do arquivo 'log.txt'
e a importação dos scripts criptografia, usuarios, elementos, data e log.
"""

#ChavePublica {e,n}
#ChavePrivada {d,n}
import Criptografia as cp
import Usuarios  as us
import elementos as el
import data as dt
import log as lg

dic_usuario={}
dic_elementos={}
dic_usuario["adm"]=("adm", 0)
usuario = ''
try:
    log = open('log.txt', 'a')
except:
    log = open('log.txt', 'w')


def menu_nivel(nivel):
    '''
    Verifica o nivel de usuario  que dependendo do nivel que for o usuario terá algumas funções 
    em comum com os de todos os niveis e outras funções peculiares destinadas a usuarios com nivel superiores.
    '''
    if nivel == '-1':
        return
    
    global usuario
    print("""NIVEIS DE USUARIO:
-----------------
0 - GG =Gerente geral = Super usuario
1 - CMT = COMANDANTE = Gerente
2 - 1ON = 1ºoficial = Tecnico
3 - PON = PRATICANTE OFICIAL DE NAUTICA = Estagiario
""")

    
        
    if nivel == 3:
        parada = True
        while parada == True:
            print("PON = Estagiario")
                
            opcao = input("""Menu opçoes:
[1]-Buscar Tripulante
[2]-Mostrar Todos Tripulantes
[3]-Sair

Escolha a opçao: 
    """)
                
                
            if opcao =="1":
#                log.write(usuario+":"+" "+"fez uma pesquisa"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.buscar_elementos(dic_elementos)
                
            elif opcao == "2":
#                log.write(usuario+":"+" "+"visualizou todos os elementos"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.mostrar_todos_os_elementos(dic_elementos)
           
            elif opcao == "3":
                menu_sair()
                parada = False
                


    elif nivel == 2:
        parada = True
        while parada:
            print("1ON = Tecnico")
            
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo
    [4]-Cadastrar Tripulante
    [5]-Visualizar pelo Log
    [6]-Sair
    
    Escolha a opçao: 
        """)

                
            if opcao == "1":
#                log.write(usuario+":"+" "+"fez uma pesquisa"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.buscar_elementos(dic_elementos)
                
            elif opcao == "2":
#                log.write(usuario+":"+" "+"visualizou todos os elementos"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
#                log.write(usuario+":"+" "+"Fez uma pesquisa pelo cargo"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.buscar_cargo(dic_elementos)
                
            elif opcao == "4":
#                log.write(usuario+":"+" "+"cadastrou um tripulante"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.cadastrar_elementos(dic_elementos)
            
            elif opcao == "5":
#                log.write(usuario+":"+" "+"Fez Busca pelo log"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                lg.buscar_log()
            
                
            elif opcao == "6":
                menu_sair()
                parada = False



    elif nivel == 1:
        parada = True
        while parada == True:
            print("CMT = Gerente")
            
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante #buscar elementos
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo #buscar cargo
    [4]-Cadastrar Tripulante
    [5]-Remover Tripulante
    [6]-Atualizar Tripulante
    [7]-Impressão Ordenada
    [8]-Visualizar pelo Log
    [9]-Sair
    
    Escolha a opçao: 
        """)
                

            if opcao == "1":
#                log.write(usuario+":"+" "+"fez uma pesquisa"+" "+ dt.hora()+" "+ dt.data())
#               log.write("\n")
                el.buscar_elementos(dic_elementos)
            
            elif opcao == "2":
#                log.write(usuario+":"+" "+"+visualizou todos os elementos"+" "+ dt.hora()+" "+ dt.data())
#               log.write("\n")
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
#                log.write(usuario+":"+" "+"Fez uma pesquisa dos tripulantes pelo cargo"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.buscar_cargo(dic_elementos)                
                
            elif opcao == "4":
#                log.write(usuario+":"+" "+"+cadastrou um tripulante"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
#                log.write(usuario+" "+"Fez remoçao de tripulante"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.remover_elementos(dic_elementos)
                
            elif opcao == "6":
#                log.write(usuario+":"+" "+"Fez atualizaçao de tripulante"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.atualizar_elementos(dic_elementos)
                            
            elif opcao == "7":
#                log.write(usuario+":"+" "+"Fez impressao de tripulante pelo cpf"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.impressao_ordenada(dic_elementos)
                print("Impressão Feita no Arquivo 'impressao.txt'.")
            
            elif opcao == "8":
#                log.write(usuario+":"+" "+"Fez Busca pelo log"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                lg.buscar_log()
            
                
            elif opcao == "9":
                menu_sair()
                parada = False



    elif nivel == 0:
        parada=True
        cp.descriptografar_elementos("elementos.txt", dic_elementos)
        while parada == True:
            
            print("GG = Super usuario")
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo
    [4]-Cadastrar Tripulante
    [5]-Remover Tripulante
    [6]-Atualizar Tripulante
    [7]-Impressão Ordenada
    [8]-Alterar o nivel do usuario
    [9]-Remover Usuario
    [10]-Visualizar pelo Log
    [11]-Sair
    
    Escolha a opçao: 
        """)


            if opcao == "1":
#                log.write(usuario+" "+"fez uma pesquisa"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.buscar_elementos(dic_elementos)
            
            elif opcao == "2":
#                log.write(usuario+" "+"visualizou todos os elementos"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
#                log.write(usuario+" "+"Fez uma pesquisa dos tripulantes pelo cargo"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.buscar_cargo(dic_elementos) 
                
            elif opcao == "4":
                #log()
#                log.write(usuario+" "+"cadastrou um tripulante"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
#                log.write(usuario+" "+"Fez remoçao de tripulante"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.remover_elementos(dic_elementos)
                
            elif opcao == "6":
#                log.write(usuario+" "+"Fez atualizaçao de tripulante"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.atualizar_elementos(dic_elementos)
                
            elif opcao == "7":
#                log.write(usuario+" "+"Fez impressao de tripulante pelo cpf"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                el.impressao_ordenada(dic_elementos)
                print("Impressão Feita no Arquivo 'impressao.txt'.")
                
            elif opcao == "8":
#                log.write(usuario+" "+"Fez alteraçao do nivel de Usuario"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                us.alterar_nivel_usuario(dic_usuario)
                
            elif opcao == "9":
#                log.write(usuario+" "+"Fez remoçao de Usuario"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                us.remover_usuario(dic_usuario)
            
            elif opcao == "10":
#                log.write(usuario+" "+"Fez Busca pelo log"+" "+ dt.hora()+" "+ dt.data())
#                log.write("\n")
                lg.buscar_log()
            
                
            elif opcao == "11":
                 menu_sair()
                 parada = False



def login(dicionario, login, senha):
    '''
    Essa função varre o dicionario de usuario e verifica se o login existe no mesmo.
    se existir o usuario loga, se não o usuario não consegue logar.
    '''
    
    global usuario
    
    if not login in dicionario:
        return -1
    
    else:
        if dicionario[login][0] == senha:
            usuario = login
            return dicionario[login][1]
        else:
            return -1


             
def sair():
    '''
    Criptografa no "arquivo usuarios.txt" e "elementos.txt" as ações feitas tanto no dicionario de usuario como no de 
    elementos respectivamente
    '''
    print("Salvando dados...")  #função para atualizar os dados
    cp.criptografar_usuarios(dic_usuario, "usuarios.txt")
    cp.criptografar_elementos(dic_elementos, "elementos.txt")
    print("Fechando Programa")



def menu_sair():
    '''
    Pergunta ao usuario se o mesmo quer sair do programa, se a resposta for "s", o programa leva até a função sair, 
    se a resposta for = a "n", eh chamada a função que direciona o usuario para o menu principal, se a resposta
    for outra qualquer, aparece uma mensagem de opção invalida.
    '''
    
    continua = True
    while continua == True:
        entrada=input("Confirma saída do programa? s/n ")

        if entrada=="s":
            sair()
            continua = False
            
        elif entrada == "n":
            menu_principal()
            
        else:
            print("Opção inválida! digite s/n ")



def menu_principal():
    '''
    Oferece 3 opções ao usuario p/ logar, cadastrar o usuario ou sair do programa.
    se o usuario digitar uma outra opção aparece a mensagem opção invalida.  
    '''
    
    print("""MENU DE OPÇAO
[1]=Login
[2]=Cadastro usuario
[3]=Sair
""")
    
    
    global usuario
    cp.decifrar_usuarios("Usuarios.txt", dic_usuario)    
    while usuario == "":
        entrada=input("Digite opção: ")

        if entrada=="1":
            user = input("Digite o nome de usuário: ")
            password = input("Digite sua senha: ")
            acesso = login(dic_usuario, user, password)
            print(acesso.__repr__())
    
        elif entrada == "2":
            us.cadastrar_usuario(dic_usuario)
            
        elif entrada=="3":
            menu_sair()
            return '-1'
            
        else:
            print("Opção inválida!")
    
    return acesso

            
def main():
    nivel = menu_principal()
    print(nivel)
    menu_nivel(nivel)


main()

log.close()