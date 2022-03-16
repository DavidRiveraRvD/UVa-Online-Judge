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
     
    
    listaneg = []
    listapos = []

    '''El ciclo permite iterar sobre la entrada para volver los numeros de cadenas a enteros para asi evaluar el caso'''
    suma = ""
    for i in lista:
        if i == "[":
            continue
        elif i == "," or i == "]":
            suma = int(suma)
            if suma < 0:
                listaneg.append(suma)
            else:
                listapos.append(suma)
            suma = ""
        else:
            suma += i

    listaneg = ordenamiento_quick(listaneg)
    listapos = ordenamiento_quick(listapos)
    listaneg.reverse
    
    '''El siguiente ciclo permite mirar cual suma es la menor apartir de la suma de numeros
    positivos y negativos posteriormente monstrarla por pantalla'''
    num_1 = 0
    num_2 = 0
    suma = 0
    for i in listapos:
        si = 0
        for j in listaneg:
            if suma == 0 and si == 0:
                si = abs(j+i)
                suma = abs(j+i)
                num_1 = i
                num_2 = j
            else:
                si = abs(j+i)
                if abs(si) < abs(suma):
                    suma = abs(si)
                    num_1 = i
                    num_2 = j
                    
    print(num_1, "y", num_2)
RvD()
