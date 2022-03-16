from sys import stdin

def RvD():

    "Recibimos las entradas"
    
    n, m, k = map(int, stdin.readline().strip().split())
    matriz = [["*" for i in range(m)] for j in range(n) ]

    """Utilizo un ciclo para recinir el numero de K de filas de la matriz y enseguida evaluo, nuevamete
    evaluo las filas de la entrada que llega y me dirijo a las posiciones en las que se encuentran
    postes de luz y sobre una matriz hago cambios que significan los postes"""
    for x in range(k):
        fil = [int(a) for a in stdin.readline().strip().split()]
        for i in range(fil[1]-1, fil[2] ):
            if matriz[fil[0]-1][i] == "*":
                matriz[fil[0]-1][i] = "0"
    """A la matriz de la cual hice el bosquejo, me dirijo y hago un conteo de los elementos iniciales que no
    cambiaron, finalmente imprimo el contador"""
    
    cont = 0
    for o in matriz:
        for m in o:
            if m == "*":
                cont += 1

    print(cont)
        
RvD()
"""Elaborado por: RvD Rivera Vargas David"""
    
