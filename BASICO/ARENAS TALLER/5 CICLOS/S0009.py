from sys import stdin


def evaluador(x, tem):
    '''Esta funcion permite cambiar o hacer la transformacion de la temperatura he imprimir
    esa conversion'''
    
    if tem == "F":
        r = (x-32)*(5/9)
        print(round(r, 2))
    else:
        r = (x/(5/9))+32
        print(round(r, 2))
    
def main():
    '''La funcion recibe los valores y los condiciona en ciclo hasta que se cumpla el numero de
    entradas, finalmente las envia a la segunda funcion que hace la conversion'''
    tem, num = stdin.readline().strip().split(" ")
    num = int(num)
    while num != 0:
        x = float(stdin.readline())
        (evaluador(x, tem))
        num -= 1
main()
