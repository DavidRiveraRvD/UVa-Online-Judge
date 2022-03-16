from sys import stdin


def ordenamiento_quick(lista):
    '''La funcion recibe la lista y la ordena'''

    if lista == []:
        return []
    else:
        return ordenamiento_quick([x for x in lista[1:] if x < lista[0]]) + lista[0:1] + ordenamiento_quick([x for x in lista[1:] if x >= lista[0]])
    
def busqueda(lista):
    '''Esta funcion busca el elemento faltante en la serie de entrada y la retorna para su impresion'''
    lista = ordenamiento_quick(lista)
    num = []
    
    for j in range(1, int(lista[-1])):
        if j not in lista:
            return j
            break
    

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

    print(busqueda(listamod))

RvD()

'''http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html'''
'''https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py'''
