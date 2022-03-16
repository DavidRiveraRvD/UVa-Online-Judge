from sys import stdin


def evaluador(pal, new):
    '''La funcion evaluador invierte la lista de la entrada
    agregando cada elemento a una nueva lista'''
    if len(pal)==1:
        new.insert(0, pal[0])
        return new
    else:
        new.insert(0, pal[0])
        pal = pal[1:]
        return evaluador(pal,new)

def comando(pal):
    '''La funcion comando hace el llamado de las funciones
    cuando la tiene la lista invertida'''
    new =[]
    impresion(evaluador(pal, new))

def impresion(new):
    '''La funcion Impresion imprime recursivamente la lista'''
    if len(new)==1:
        print(new[0])
    else:
        print(new[0], end="")
        new = new[1:]
        return impresion(new)
    
def RvD():
    '''La funcion principal recibe la entrada a evaluar y la
    envia a una funcion'''
    pal = [x for x in stdin.readline().strip()]
    while len(pal):
        comando(pal)
        pal = [x for x in stdin.readline().strip()]
        
RvD()
'''DiseÃ±ado por: RvD Rivera Vargas David'''
