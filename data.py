# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1
Autor: Josenildo Lopes de Souza (jls2)
Email: jls2@cin.ufpe.br
Copyright(c) 2018 Josenildo Lopes de Souza
"""

"""
Esse script contem informações sobre a data e hora para serem inseridas na função de log 
para fazer o registro das atividades dos usuarios.
"""

from datetime import date, datetime

def data():
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    
    return (str(dia)+"/"+str(mes)+"/"+str(ano))


def hora():

    agora = datetime.now()
    horas=agora.hour
    minutos=agora.minute
    segundos=agora.second

    return(str(horas)+":"+str(minutos)+":"+str(segundos))
    