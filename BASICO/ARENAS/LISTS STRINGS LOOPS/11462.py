from sys import stdin

def ordenamiento_quick(lista):
    '''La funcion de ordenamiento recive la lista y la ordenaa, finalmente retorna la lista ordenada'''
    if lista == []: return []
    else: return ordenamiento_quick([x for x in lista[1:] if x < lista[0]]) + lista[0:1] + ordenamiento_quick([x for x in lista[1:] if x >= lista[0]])

def RvD():
    '''La funcion principal recibe los numeros a evaluar en una lista, posteriormete envia
    la lista a una funcion de ordenamiento'''
    
    x = int(stdin.readline())
    while x != 0: lista = [int(num) for num in stdin.readline().strip().split()]; d = ordenamiento_quick(lista); print(*d); x = int(stdin.readline())

RvD()
