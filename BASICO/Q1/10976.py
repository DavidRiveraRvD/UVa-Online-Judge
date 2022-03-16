from sys import stdin

def RvD():
    '''La funcion principal recibe una entrada "K" la cual por medio de ciclos y funciones
    calcula el numero de posibles sumas entre fraccionarios para que de 1/K = 1/x + 1/y'''
    
    k = stdin.readline().strip()
    
    while k  != "" and k != "0" and int(k)>0:
        k = int(k)
        y = int(k)+1
        cont = 0
        numerosx = []
        numerosy = []
        x = int((k*y)/(y-k))
        
        '''Mediante un cilo evaluo los numeros y los agrego a una lista que finamente los
        imprimira con otro ciclo'''
        
        '''while y <= x:
            x = (y*k)/(y-k)
            #x = int(1/((y-k)/(k*y)))
            x = int(x)
            lam = lambda x,y,k: ((round(x*(y-k),15)) == round((y*k), 15))
            if lam(x,y,k) == True:
                numerosx.append(int(x))
                numerosy.append(int(y))
                cont += 1
            y += 1'''
            
        while x >= y:
            x = (y*k)/(y-k)
            uno = 1/int(k)
            dos = 1/int(x) + 1/int(y)
            lam = lambda uno,dos : (round(uno,15) == round(dos,15))
            if lam(uno,dos)== True:
                cont += 1
                numerosx.append(int(x))
                numerosy.append(int(y))
                y += 1
            else:
                y += 1
            pos = 0
            c = 0
        print(cont)
        for i in range(len(numerosx)):
            print("1/{} = 1/{} + 1/{}".format(k, numerosx[i], numerosy[i]))
            
        k = stdin.readline().strip()

RvD()
"""Diseñado por: RvD Rivera Vargas David"""
