from sys import stdin



def RvD():
    """El codigo recibe el numero de casos en parrafos, mediante un
    ciclo evaluo las oraciones ingresadas y en otro extraigo las
    letras correspondientes para así finalmete, enviar la sumatoria
    de las letras a un arreglo y pedir la oracion siguiente, transcurrido
    el parrafo, imprimo el arreglo final, y continuo con el siguiente
    caso"""
    cas = int(stdin.readline())
    space = stdin.readline().strip().split()
    cont = 0
    while cas != cont:
        pal = []
        oracion = list(stdin.readline().strip().split())
        while len(oracion) != 0:
            trozo = ""
            pos = 0
            for i in range(len(oracion)):
                if pos < len(oracion[i]):
                    trozo = trozo+oracion[i][pos]
                    pos += 1
            pal.append(trozo)
            oracion = list(stdin.readline().strip().split())
                
        cont += 1
        print("Case #{}:".format(cont))
        for i in pal:
            if len(pal) != 0:
                print(i)
   
RvD()
"""Elaborado por: RvD Rivera Vargas David"""
