from sys import stdin

def ordenamiento_quick(lista):
    '''La funcion recibe la lista y la ordena'''

    if lista == []:
        return []
    else:
        return ordenamiento_quick([x for x in lista[1:] if x < lista[0]]) + lista[0:1] + ordenamiento_quick([x for x in lista[1:] if x >= lista[0]])
    



def RvD():
    '''La funcion principal recibe los numeros a evaluar en una lista, posteriormete envia
    la lista a una funcion de busqueda'''
    listapri = stdin.readline().strip()
    listaseg = stdin.readline().strip()
    lista_1 = []

    '''El ciclo permite iterar sobre la entrada para volver los numeros de cadenas a enteros para asi evaluar el caso'''
    suma = "" 
    for i in listapri:
        if i == "[":
            continue
        elif i == "," or i == "]":
            suma = int(suma)
            lista_1.append(suma)
            suma = ""
        else:
            suma += i

    '''El ciclo permite iterar sobre la entrada para volver los numeros de cadenas a enteros para asi evaluar el caso'''
    suma = ""    
    for i in listaseg:
        if i == "[":
            continue
        elif i == "," or i == "]":
            suma = int(suma)
            lista_1.append(suma)
            suma = ""
        else:
            suma += i
    '''Despues de creada la lista princial, la ordenamos'''

    
    lista_1 = (ordenamiento_quick(lista_1))

    '''Creo los numeros centrales y los asigno a una variable para sacar la media'''
    centro = (len(lista_1)-1)//2
    num_1 = lista_1[centro]
    num_2 = lista_1[centro+1]
    resul = (num_1 + num_2)//2
    print(resul)

RvD()
