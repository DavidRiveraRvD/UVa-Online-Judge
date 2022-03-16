from sys import stdin

def quick(trozo):
    """Recibo el trozo a ordenar, y lo ordeno, luego lo retorno"""
    if trozo == []:
        return []
    else:
        return quick([x for x in trozo[1:] if x < trozo[0]]) + trozo[0:1] + quick([x for x in trozo[1:] if x>= trozo[0]])

def RvD():
    a, b = stdin.readline().strip().split()
    a, b = int(a), int(b)
    matriz = []
    """Recibo la longitud de la matriz y en el rango de la fila
    evaluo las filas inmediatamente al recibirlas, las evaluo y
    divido en trozos el trozo al arreglar lo mando a un ordenamiento
    recursivo y cuando me retorna lo sumo al trozo que debe mantenerse
    original, luego lo agrego a la matriz y pido la siguiente fila,
    hasta terminar con las filas, luego imprimo la matriz"""
    for i in range(a):
        fil = [int(x) for x in stdin.readline().strip().split()]
        trozo = []
        con = 0
        complemento = []
        for j in range(len(fil)):
            if fil[j] != 2 and con == 0:
                trozo.append(fil[j])
            else:
                con += 1
                complemento.append(fil[j])

        matriz.append(quick(trozo)+complemento)
    for k in matriz:
        print(*k)
            
RvD()
"""Elaborado por: RvD Rivera Vargas David"""
