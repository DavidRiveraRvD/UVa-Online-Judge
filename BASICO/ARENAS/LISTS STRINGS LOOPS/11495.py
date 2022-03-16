from sys import stdin

def bubbleSort(n, cont):
    '''La funcion receibe la lista sobre la cual se va a trabajar y un contador que toma el
    numero de ordenamientos realizados que finalmente va retornar'''
    
    for x in range(len(n)-1):
        for i in range(len(n)-1-x):
            if n[i]>n[i+1]:
                temp = n[i]
                n[i] = n[i+1]
                n[i+1] = temp
                cont += 1
    return cont
            


def RvD():
    '''La funcion principal, recibe la lista para ordenar y envia esa lista a una funcion de
    ordenamiento'''
    
    n = [int(x) for x in stdin.readline().strip().split(" ")]
    while n[0] != 0:
        cont = 0
        n = n[1:]
        y = bubbleSort(n, cont)

        '''Los condicionales evaluan el numero de ordenamientos, he inprimen lo requerido'''
        
        if y%2 == 0:
            print("Carlos")
        else:
            print("Marcelo")
        n = [int(x) for x in stdin.readline().strip().split(" ")]
RvD()
