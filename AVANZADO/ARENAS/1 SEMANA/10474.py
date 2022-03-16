from sys import stdin

def RvD():
    num1, num2 = map(int, stdin.readline().strip().split())
    case = 1
    while num1 != 0 and num2!=0:
        lista1 = []
        for i in range(num1):
            x = int(stdin.readline())
            lista1.append(x)
        lista2 = []
        for j in range(num2):
            z = int(stdin.readline())
            lista2.append(z)
        print("CASE# {}:".format(case))
        lista1=sorted(lista1)
        for y in lista2:            
            if y in lista1: print(y, "found at", lista1.index(y)+1)
            else: print(y, "not found")
        case += 1        
        num1, num2 = map(int, stdin.readline().strip().split())
RvD()
"""Elaborado por: RvD Rivera Vargas David"""
