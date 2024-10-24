# -*- coding: utf-8 -*-

def Soma(a,b):
    return a + b

def Soma(*numbers):
    soma = 0
    for n in numbers:
        soma = soma + n
        
    return soma

def Multiplicacao(a,b):
    return a * b