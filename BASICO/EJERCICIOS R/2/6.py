from sys import stdin
import math

def fac(y):
    return math.factorial(y)
def Trigonometricas(letra, num):
    if letra == "S":
        return math.sin(num)
    elif letra == "C":
        return math.cos(num)
    elif letra == "T":
        return math.tan(num)
def Raiz(y):
    return math.sqrt(y)

def main():
    print("MENU:\nEn el menu va a ingresar la opcion a calcular (Enter), el numero a calcular, si es la segunda opcion ingresar el numero antecedido de una 'S'= Seno, 'C' = Coseno, 'T'= Tangente\nseparadas por un espacio.\n 1. Factorial\n 2. Seno, Coseno yTangente\n 3. Raiz cuadrada") 
    x = stdin.readline().strip()
    if x == "1":
        y = int(stdin.readline().strip())
        fac(y)
        print(fac(y))
    elif x == "2":
        y = stdin.readline().strip().split()
        letra = y[0]
        num = y[1]
        num = int(num)
        Trigonometricas(letra, num)
        print(Trigonometricas(letra, num))
    elif x == "3":
        y = int(stdin.readline().strip())
        Raiz(y)
        print(int(Raiz(y)))
    else:
        print("ERROR!!!")
main()
