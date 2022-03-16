from sys import stdin

def evalua(matriz, fil, col):
    '''Las siguientes son las plantillas base para las comparaciones, con las vocales
    en todas las formas posibles'''
    
    A = [["X", "X", "X"],["X", "O", "X"],["X", "X", "X"], ["X", "O", "X"], ["X", "O", "X"] ]
    AA = [["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"] ]
    AAA = [["X", "X", "X", "X", "X"], ["X", "O", "X", "O", "O",], ["X", "X", "X",  "X", "X"]]
    AAAA = [["X", "X", "X", "X", "X"], ["O", "O", "X", "O", "X",], ["X", "X", "X",  "X", "X"]]
    
    E = [["X", "X", "X",], ["X", "O", "O"], ["X", "X", "X"], ["X", "O", "O"], ["X", "X", "X"] ]
    EE = [["X", "X", "X",], ["O", "O", "X"], ["X", "X", "X"], ["O", "O", "X"], ["X", "X", "X"] ]
    EEE = [["X", "X", "X", "X", "X"], ["X", "O", "X", "O", "X",], ["X", "O", "X",  "O", "X"]]
    EEEE = [["X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X",], ["X", "X", "X",  "X", "X"]]
    
    I = [["X", "X", "X",], ["O", "X", "O"], ["O", "X", "O"], ["O", "X", "O"], ["X", "X", "X"] ]
    II = [["X", "O", "O", "O", "X"], ["X", "X", "X", "X", "X",], ["X", "O", "O",  "O", "X"] ]

    O = [["X", "X", "X",], ["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"] ]
    OO = [["X", "X", "X", "X", "X"], ["X", "O", "O", "O", "X",], ["X", "X", "X",  "X", "X"] ]
    
    U = [["X", "O", "X",], ["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"] ]
    UU = [["X", "X", "X",], ["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
    UUU = [["X", "X", "X", "X", "X"], ["X", "O", "O", "O", "O",], ["X", "X", "X",  "X", "X"] ]
    UUUU = [["X", "X", "X", "X", "X"], ["O", "O", "O", "O", "X",], ["X", "X", "X",  "X", "X"] ]

    '''Contadores de vocales'''
    
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    '''Ciclos evaluadores y creadores de listas para comparacion'''
    
    for x in range(fil):
        for y in range(col):

            '''Primer ciclo'''
            cont = x+5;
            co = y+3
            una = []
            if cont<= fil and co<=col:
                for k in range(x,cont):
                    una.append(matriz[k][y:co])

            '''Condicionales de comparacion primer ciclo'''
            if una == A or una == AA or una == AAA or una == AAA:
                a += 1
            if una == E or una == EE or una == EEE or una == EEEE:
                e += 1
            if una == I or una == II:
                i += 1        
            if una == O or una == OO:
                o += 1
            if una == U or una == UU or una == UUU or una == UUUU:
                u += 1

            '''Segundo ciclo'''
            unas = []
            con = x+3;
            conta = y+5
            if con<=fil and conta<=col:
                for k in range(x,con):
                    unas.append(matriz[k][y:conta])

            '''Condicionales segundo ciclo'''
            if unas == O or unas == OO:
                o += 1
            if unas == U or unas == UU or unas == UUU or unas == UUUU:
                u += 1
            if unas == I or unas == II:
                i += 1
            if unas == E or unas == EE or unas == EEE or unas == EEEE:
                e += 1
            if unas == A or unas == AA or unas == AAA or unas == AAA:
                a += 1
            
    '''Impresion de contadores por vocales'''     
    print("A:",a)
    print("E:",e)
    print("I:",i)
    print("O:",o)
    print("U:",u)

    
def RvD():
    '''La funcion RvD() es la principal y recibe el numero de filas y columnas'''
    
    fila = int(stdin.readline())
    fil = 0
    col = int(stdin.readline())
    cas = []

    '''Mediante un ciclo creo el numero de filas por medio de las entradas'''
    while fila != 0:
        x = stdin.readline().strip().split(" ")
        cas.append(x)
        fila -= 1
        fil += 1 
    evalua(cas, fil, col)
RvD()
