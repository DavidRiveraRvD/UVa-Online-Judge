from sys import stdin
import random

def evaluador(var, num):
    if var == num:
        return True
    else:
        return 
    
    
def main():
    var = int(input("Adivine un numero entre el rango de 0 y 10: "))
    num = random.randint(0, 10)
    y =(evaluador(var, num))
    if y == True:
        print("Felicitaciones ha ganado!!!")
    else:
        print("No adivinaste el numero, era: "+ num)
        
        
main()
