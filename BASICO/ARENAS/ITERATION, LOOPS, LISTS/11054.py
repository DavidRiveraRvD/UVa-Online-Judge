from sys import stdin


def main():
    '''El codigo tiene como fin sumar las botellas de vino que tranporta a cada posicion,
        esto se suma por medio de un ciclo que recorre toda la linea que entra, dicha linea
        se interpreta como lista para mejor manejo'''
    
    n = int(stdin.readline())
    while n:
        lista = [int(x) for x in stdin.readline().split()]
        a = 0
        for i in range(1,n):
            b = lista[i-1]
            lista[i]=b+lista[i]
            a += abs(b)
        print(a)
        n = int(stdin.readline())
        

main()
