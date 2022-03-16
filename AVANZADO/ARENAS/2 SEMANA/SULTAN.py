from sys import stdin

casos = [None]*8

def damas(d):
    global casos ,tabla, mk
    if d == 8:
        g = 0
        for b in range(8): g += tabla[b][casos[b]-1]
        mk = max(g,mk)
        return 1
    else:
        s = 0
        for f in range(1,9):
            casos[d] = f
            if not provatoria(d): s += damas(d+1)
        return s

def provatoria(d):
    global casos, tabla, mk
    for i in range(0,d):
        if casos[i] == casos[d] or i+casos[i] == d+casos[d] or i-casos[i] == d-casos[d]: return True
    return False




def RvD():
    global casos, tabla, mk
    num = int (stdin.readline().strip())
    for j in range(num):
        tabla = []
        for k in range(8):
            lista1 = [int(i) for i in stdin.readline().strip().split()]
            lista2 = []
            for i in lista1: lista2.append(int(i))
            tabla.append(lista2)
        mk = 0
        damas(0)
        print(mk)
RvD()
"""Elaborado por RvD: Rivera Vragas David"""
