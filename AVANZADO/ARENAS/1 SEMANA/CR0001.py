from sys import stdin

def impresion(a):
    if len(a)== 1:
        print(a[0])
    else:
        print(a[0], end = "")
        return impresion(a[1:])

def minas(matriz, case):
    """Funcion para bordear las minas, mando la matriz a una funcion la cual suma 1
    a los ceros alrededor de los "*" y luego la imprimo"""
    for i in range(1, len(matriz)-1):
        for j in range(1, len(matriz[i])-1):
            if matriz[i][j] == "*":
                if matriz[i-1][j-1] != "*" : matriz[i-1][j-1] += 1
                if matriz[i-1][j] != "*": matriz[i-1][j] += 1
                if matriz[i-1][j+1] != "*": matriz[i-1][j+1] += 1
                if matriz[i][j-1] != "*": matriz[i][j-1] += 1
                if matriz[i][j+1] != "*": matriz[i][j+1] += 1
                if matriz[i+1][j-1] != "*": matriz[i+1][j-1] += 1
                if matriz[i+1][j] != "*": matriz[i+1][j] += 1
                if matriz[i+1][j+1] != "*": matriz[i+1][j+1] += 1
    if case >1: print("")
    print("Field #{}:".format (case))
    for i in matriz:
        print(i)
    for i in matriz[1:-1]:
        a = i[1:-1]
        impresion(a)

                                
def RvD():
    """La funcion principal recibe la longitud de la matriz, luego creo
    una matriz similar llana de ceros, y la bordeo con mas ceros,
    a la vez que voy recibiendo cada linea, intercambio los ceros
    en la matriz por asteriscos en las nuevas entradas"""
    num1, num2 = map(int, stdin.readline().strip().split())
    case = 1
    while num1 != 0 and num2 !=0:
        matriz = [[0 for x in range(num2+2)] for y in range(num1+2)]
        cont = 0
        
        for z in range(num1):
            fil = stdin.readline().strip()
            for i in range(len(fil)):
                if fil[i] == "*":
                    matriz[cont+1][i+1] = "*"
            cont += 1
        """Para bordear las minas, mando la matriz a una funcion la cual suma 1
        a los ceros alrededor de los "*" y luego la imprimo"""
        minas(matriz, case)
        case += 1
        num1, num2 = map(int, stdin.readline().strip().split())
    
RvD()
"""Elaborado por: RvD Rivera Vargas David"""
