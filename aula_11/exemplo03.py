import os
import random


def gerar_numeros(ini, fim, qtd):
    lst_num = [random.randint(ini, fim) for i in range(qtd)]
    return lst_num

def soma(num1, num2):
    soma = (num1 + num2)
    return soma

def subtrai(num1, num2):
    subtrai = (num1 - num2)
    return subtrai

def multiplica(num1, num2):
    multiplica = (num1 * num2)
    return multiplica

def divide(num1, num2):
    divide = (num1 / num2)
    return divide

# Inicio do algoritmo 
inicio = 1
final = 10
quantidade = 2
lst_numeros = gerar_numeros(inicio, final, quantidade)
print(lst_numeros)

somando = soma(lst_numeros[0], lst_numeros[1]) 
print(somando)

subtraindo = subtrai(lst_numeros[0], lst_numeros[1]) 
print(subtraindo)

multiplicando = multiplica(lst_numeros[0], lst_numeros[1]) 
print(multiplicando)

dividindo = divide(lst_numeros[0], lst_numeros[1]) 
print(dividindo)




subtração = (lst_numeros[0] - lst_numeros[1])
multiplicação = (lst_numeros[0] * lst_numeros[1])
divisão = (lst_numeros[0] / lst_numeros[1])
print(lst_numeros)
print(lst_numeros[0])
print(lst_numeros[1])
print(soma, subtração, multiplicação, divisão)