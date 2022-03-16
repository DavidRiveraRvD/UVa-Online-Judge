from sys import stdin


def RvD():

    x = int(stdin.readline())
    conta = 0
        
    '''El siguiente ciclo evalua los numeros a aplicarles los procedimientos'''
    while x >= 4:            
        cont = x-1
        lista = []

        '''este ciclo crea una lista, la lista es los valores de en medio a los unos de la impresion'''
        for i in range(x-2):
            lista.append(cont)
            cont -= 1

        '''el siguiente ciclo juega con los numeros que siempre van a estar cambiando de posicion en la impresion final'''
        
        for i in range(x+1):
            if i == 0 :
                unos = []
                for i in range (x):
                    unos.append(1)
                print(*unos)
                
            elif i == x:
                unos = []
                for i in range (x):
                    unos.append(1)
                print(*unos)
            elif i == 1:
                print("1", *lista, "1")
            else:
                new = lista[0]
                lista.remove(lista[0])
                lista.append(new)
                print("1", *lista, "1")
        print("")
                
        x = int(stdin.readline())
        conta += 1    
         
RvD()
