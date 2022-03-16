from sys import stdin

def evaluador(res, pot, n):
    if res == 0: return 1
    elif n**pot>res or res<0: return 0
    else: return evaluador(res, pot, n+1) + evaluador(res-(n**pot), pot, n+1)
    
def RvD():
    num = stdin.readline().strip()
    while num != "":
        num = int(num)
        pot = int(stdin.readline().strip())
        print(evaluador(num, pot, 1))
        num = stdin.readline().strip()
RvD()
"""Elaborado por: RvD Rivera Vargas David"""
