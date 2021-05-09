# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)

Copyright(c) Josenildo 
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
'''
mostra a data, dia, mês e ano
'''

def hora():

    agora = datetime.now()
    horas=agora.hour
    minutos=agora.minute
    segundos=agora.second

    return(str(horas)+":"+str(minutos)+":"+str(segundos))
'''
mostra a horas, minutos, e segundos
'''