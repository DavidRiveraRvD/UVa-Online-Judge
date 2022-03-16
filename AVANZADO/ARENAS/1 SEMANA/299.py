from sys import stdin

def Bubble(lista, cont):
    """ Codigo de ordenamiento burbuja, en el cual tengo una
    una variable contador que me lleva el numero de ordenamientos
    finalmente ordenado el arreglo retorno el la variable contador"""
    for x in range(len(lista)-1, 0, -1):
        for i in range(x):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                cont += 1
    return cont

def RvD():
    """Recibo el numero de casos y los condiciono con un ciclo
    hasta que los evalue todos, recibo el numero de elementos
    en el arreglo y finalmente recibo el arreglo que lo mando
    a una funcion de ordenamiento para que me retorne lo debido"""
    case = int(stdin.readline())
    while case != 0:
        case -= 1
        entrada = int(stdin.readline())
        lista = [int(r) for r in stdin.readline().strip().split()]
        orde = Bubble(lista, 0)
        print("Optimal train swapping takes", orde, "swaps.")
RvD()
"""Elaborado por: RvD Rivera Vargas David"""
