from sys import stdin

def insertion(lista, cont):
    '''La funcion de ordenamiento basada en el 'Insertion Sort' ordena la
    lista he imprime lo deseado'''
    
    for i in range(1, len(lista)):
        x = lista[i]
        pos = i
        while pos > 0 and lista[pos-1] > x:
            lista[pos] = lista[pos - 1]
            pos = pos-1
            cont += 1
        lista[pos] = x

    return cont

def RvD():
    casos = int(stdin.readline())
    
    
    while casos != 0:
        numero = stdin.readline().strip()
        lista = [int(i) for i in stdin.readline().strip().split(" ")]
        cont = 0
        print(insertion(lista, cont))
        
        casos -= 1

RvD()
