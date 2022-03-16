from sys import stdin
def quicksortR(array):
    '''La funcion de ordaniento lo ordena segun lo deseado, teniendo en cuenta el pivot'''
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[-1]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
    return less+equal+greater
def quicksort(array):
    '''La funcion de ordaniento lo ordena segun lo deseado, teniendo en cuenta el pivot'''
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
    return less+equal+greater

def quicksortC(array):
    '''La funcion de ordaniento lo ordena segun lo deseado, teniendo en cuenta el pivot'''
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[len(array)//2]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
    return less+equal+greater

def RvD():
    '''La funcion principal recibe los numeros a evaluar en una lista, posteriormete envia
    la lista a una funcion de ordenamiento'''
    
    
    cont = int(stdin.readline())
    conta = 1
    
    while cont != 0:
        c = int(stdin.readline())
        r = stdin.readline().strip()
        lista = [int(num) for num in stdin.readline().strip().split()]

        if r == "R":
            print("Case {}: ".format(conta), end=(""))
            print(*quicksortR(lista))

        elif r == "L":
            print("Case {}: ".format(conta), end=(""))
            print(*quicksort(lista))
            
        else:
            print("Case {}: ".format(conta), end=(""))
            print(*quicksortC(lista))
            
        cont-=1
        conta += 1
        
RvD()
