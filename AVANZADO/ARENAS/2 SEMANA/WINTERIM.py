from sys import stdin

##def evaluador(i, num):
##    a = True
##    cont = 0
##    noches = 0
##    for j in range(len(num)):
##        cont += num[j]
##        if cont >i:
##            noches += 1
##            cont = 0
##            cont += num[j]
##    return noches
##            
##    
##

def RvD():
    lista = list(stdin.readline().strip().split())
    while len(lista) == 2:
        a, b = int(lista[0]), int(lista[1])
        num = []
        maxi = 0
        for i in range(a+1):
            cas = int(stdin.readline().strip())
            num.append(cas)
            maxi += cas
        p = max(num)
        temp = []
        while p<maxi:
            cont = 0
            if b==0:
                print(maxi)
                break
            else:
                prom = (p+maxi)/2
                #temp = []
                sumatoria_c = 0
                for i in num:
                    sumatoria_c += i
                    if sumatoria_c>prom:
                        cont += 1
                        sumatoria_c = i
                if cont<=b:
                    maxi = prom
                    temp.append(int(prom))
                else:
                    p = prom + 1
        if b!=0:
            temp.sort()
            print(temp[0])
        lista = list(stdin.readline().strip().split())
            
RvD()
"""Elaborado por RvD: Rivera Vargas David"""
       
            
        
