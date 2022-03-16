from sys import stdin

def ordenamiento_quick(lista):
    '''La funcion de ordenamiento recive la lista y la ordenaa, finalmente retorna la lista ordenada'''
    if lista == []: return []
    else: return ordenamiento_quick([x for x in lista[1:] if x < lista[0]]) + lista[0:1] + ordenamiento_quick([x for x in lista[1:] if x >= lista[0]])


def RvD():
    lista = stdin.readline().strip().split(" ")

    '''La funcion recibe la lista la cual la evalua y la divide en dos, una los impares y la otra
    con los numeros pares'''

    not_lista = ["FIN", "DE", "EJERCICIO"]  
    while lista != not_lista:
        
        lista = [int(x) for x in lista]
        lista_par = []
        lista_impar = []
        
        for i in lista:
            if i%2 == 0:
                lista_par.append(i)
            else:
                lista_impar.append(i)
        
                
        lista_impar = ordenamiento_quick(lista_impar)
        lista_par = ordenamiento_quick(lista_par)
        lista_impar.reverse()
        
        '''Finalmente se toma la lista impar la cual la recorro y en la cual agrego los elementos
        de la lista impar a la lista par cada dos saltos'''
        
        cont = 1
        for i in lista_impar:
            lista_par.insert(cont, i)
            cont += 2

        print(*lista_par)
        print("")
        
        

        lista = stdin.readline().strip().split(" ")
        
        
RvD()
'''Elaborado por RvD. Rivera Vargas David'''

    
