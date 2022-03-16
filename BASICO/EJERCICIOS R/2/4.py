from sys import stdin
import time

def generador(nombre):
    return "Hola " +  nombre + " " +time.strftime( "%I:%M:%S" )
def main():
    nombre = input("Escriba su nombre: ")
    print(generador(nombre))
    
main()
