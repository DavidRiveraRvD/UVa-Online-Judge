from sys import stdin
import math

def num(var):
    if var >= 0:
        return("Numero Positivo")
    else:
        return("Numero Negativo")
    
def parr(var):
    if var == 0:
        return("Numero Par")
    elif var%2 == 0:
        return("Numero Par")
    else:
        return("Numero Impar")

def cuadrado(var):
    if ((int(math.sqrt(var)))**2) == var:
        return("Cuadrado Perfecto")
    else:
        return("El numero ingresado no es cuadrado perfecto")
    
def maximo(var):
    x = var+1
    return (x)

def minimo(var):
    y = var-1
    return(y)

def maxmin(var):
    s = (var-1)+(var+1)
    return s

def main():
    var = int(input("Ingrese un numero a evaluar: "))
    print(num(var))
    print(parr(var))
    print(cuadrado(var))
    print("Su mayor digito: ", maximo(var))
    print("Su menor digito: ", minimo(var))
    print("La suma del mayor dígito y el menor dígito es: ", maxmin(var))
main()    
