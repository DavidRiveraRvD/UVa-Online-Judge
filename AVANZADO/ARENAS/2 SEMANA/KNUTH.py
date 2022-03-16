from sys import stdin


def evaluador(cas, newcas, con):
    if len(cas)==con:
        print(newcas)
    else:
        for i in range(len(newcas)+1):
            print(evaluador(cas, newcas, con+1))

def RvD():
    cas = stdin.readline().strip()
    while len(cas)!= 0:
        newcas = []
        for i in range(len(cas)):
            newcas.append(cas[i])
        cas, con = newcas, 1
        evaluador(cas, newcas[0], con)
        cas = stdin.readline().strip()      
RvD()
"""Elaborado por RvD: Rivera Vargas David"""
    
