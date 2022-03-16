from sys import stdin


def insertion(lista):
    '''La funcion de ordenamiento basada en el 'Insertion Sort' ordena la
    lista he imprime lo deseado'''
    
    for i in range(1, len(lista)):
        x = lista[i]
        pos = i
        while pos > 0 and lista[pos-1] > x:
  
            lista[pos] = lista[pos - 1]
            print(*lista)
            pos = pos-1

        lista[pos] = x
    print(*lista)

    return lista

def RvD():
    '''La funcion principal recibe las dos entradas, de las cuales una es una lista, posteriormente
    hace un llamado a una funcion la cual ordena la lista'''
    cont = int(stdin.readline())
    lista = [int(a) for a in stdin.readline().strip().split(" ")]
    insertion(lista)
RvD()
    
