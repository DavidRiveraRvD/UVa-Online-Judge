from sys import stdin

def sumatoria(a, con):
    if len(a)==1:
        con += int(a[0])
        return con
    else:
        con += int(a[0])
        return sumatoria(a[1:], con)
        
def RvD():
    num = list(stdin.readline().strip().split())
    while len(num) == 2:
        a, b = num[0], int(num[1])
        cont = sumatoria(a, 0)
        cont = str(cont)
        cont *=b
        cont = sumatoria(str(cont), 0)
        if len(str(cont)) == 2:
               cont = sumatoria(str(cont), 0)
        if len(a) == 1:
            print(a)
        else: print(str(cont))
        num = stdin.readline().strip().split()
RvD()
"""Elaborado por: RvD Rivera Vargas David"""
