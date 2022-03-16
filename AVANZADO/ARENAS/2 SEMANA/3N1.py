from sys import stdin


def recursion(a, cont):
    if a != 1:
        if a % 2 == 0: return(recursion(a/2, cont+1))
        else: return(recursion((3*a)+1, cont+1))
    else: return cont +1 

def RvD():
    entrada = list(stdin.readline().strip().split())
    while len(entrada)==2:
        a, b = int(entrada[0]), int(entrada[1])
        if a>b:
            con = 0
            for x in range(b, a+1):
                t = recursion(x, 0)
                if t>con:
                    con = t
        else:
            con = 0
            for x in range(a, b+1):
                t = recursion(x, 0)
                if t>con:
                    con = t
        print(a,b,con)
        entrada = list(stdin.readline().strip().split())
RvD()
