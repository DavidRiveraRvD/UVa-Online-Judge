from sys import stdin

def ordenamiento_quick(lista):
    '''La funcion recibe la lista y la ordena'''

    if lista == []:
        return []
    else:
        return ordenamiento_quick([x for x in lista[1:] if x < lista[0]]) + lista[0:1] + ordenamiento_quick([x for x in lista[1:] if x >= lista[0]])
    

 
def RvD():
    lista = stdin.readline().strip()
    '''La funcion principal recibe los numeros a evaluar en una lista, posteriormete envia
    la lista a una funcion de busqueda'''
    n = int(stdin.readline().strip())
    
    lista_1 = []

    '''El ciclo permite iterar sobre la entrada para volver los numeros de cadenas a enteros para asi evaluar el caso'''
    suma = ""
    for i in lista:
        if i == "[":
            continue
        elif i == "," or i == "]":
            suma = int(suma)
            lista_1.append(suma)
            suma = ""
        else:
            suma += i

    lista_1 = ordenamiento_quick(lista_1)
    lista_1.reverse
    
    '''El siguiente ciclo permite mirar cual suma es igual a n apartir de la suma de los numeros
    en la lista posteriormente monstrarla por pantalla'''
    num_1 = 0
    num_2 = 0
    suma = 0
    for i in lista_1:
        for j in lista_1:
            suma = i-j
            if suma == n:
                num_1 = i
                num_2 = j
                break
    if num_1 == 0 and num_2 == 0:
        print("Pareja no encontrada")
    else:print(num_1, "y", num_2)
RvD()
