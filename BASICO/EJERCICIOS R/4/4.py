from sys import stdin


def ordenamiento_quick(lista):
    
    '''El odenamiento quick es un algoritmo basado en la técnica de divide y vencerás, que permite, en promedio, ordenar n elementos
    en un tiempo proporcional a n log n'''
    '''Todo esto lo hace por medio de pivotes que es el elemento de evaluacion
    cuando empieza a comparar valores'''
    
    if lista == []:
        return []
    else:
        return ordenamiento_quick([x for x in lista[1:] if x < lista[0]]) + lista[0:1] + ordenamiento_quick([x for x in lista[1:] if x >= lista[0]])


def RvD():
    '''La funcion recibe la entrada y llama a la funcion de ordenamiento, posteriormente la imprime'''
    
    lista = [int(num) for num in stdin.readline().strip().split(",")]
    print(ordenamiento_quick(lista))

RvD()

    
