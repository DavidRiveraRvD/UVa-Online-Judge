from sys import stdin


def ordenamiento_quick(lista):
    '''La funcion recibe la lista y la ordena'''

    if lista == []:
        return []
    else:
        return ordenamiento_quick([x for x in lista[1:] if x < lista[0]]) + lista[0:1] + ordenamiento_quick([x for x in lista[1:] if x >= lista[0]])
    
def busqueda(lista):
    '''Esta funcion busca el elemento faltante en la serie de entradaordenada e imprime los dos numeros menores'''
    lista = ordenamiento_quick(lista)
    primer_num = lista[0]
    segundo_num = ""
    for i in lista:
        if i > primer_num:
          segundo_num = i
          break
    print(primer_num, "y", segundo_num)
    

def RvD():
    '''La funcion principal recibe los numeros a evaluar en una lista, posteriormete envia
    la lista a una funcion de busqueda'''
    
    lista = stdin.readline().strip()
    listamod = []

    '''El ciclo permite iterar sobre la entrada para volver los numeros de cadenas a enteros para asi evaluar el caso'''
    suma = ""
    for i in lista:
        if i == "[":
            continue
        elif i == "," or i == "]":
            suma = int(suma)
            listamod.append(suma)
            suma = ""
        else:
            suma += i
    busqueda(listamod)

RvD()
