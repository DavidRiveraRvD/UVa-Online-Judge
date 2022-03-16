from sys import stdin
class aset:
    def __init__(self):
        self.p = self
        self.rank = 0
        self.con = 1
        
def link(x, y):
    if x!=y:
        if x.rank > y.rank:
            y.p = x
            x.con+=y.con
        else:
            y.con+=x.con
            x.p = y
            if x.rank == y.rank:
                y.rank+=1
                
def findset(j):
    if j != j.p:
        j.p = findset(j.p)
    return j.p

def union(x, y):
    link(findset(x),  findset(y))

def main():
    num = int(stdin.readline().strip())
    varo = stdin.readline()
    cont = 0
    for i in range(num):
        cont += 1
        verdaderas = 0
        falsas = 0
        var =int(stdin.readline().strip())
        lista = dict()
        for v in range(var):
            c = aset()
            lista[v+1] = c
        trio = stdin.readline().strip()
        while trio != "":
            trio = [x for x in trio.split(" ")]
            a, b, c = trio[0], int(trio[1]), int(trio[2])
            if a == "c":
                if b not in lista:
                    var1= aset()
                    lista[a]=var1
                else:
                    var1 = lista[b]
                if c not in lista:
                    var2 = aset()
                    lista[c] = var2
                else:
                    var2 = lista[c]
                union(var1, var2)
            elif a == "q":
                if (findset(lista[b])==findset(lista[c])) == False:
                    falsas += 1
                else:
                    verdaderas += 1
            
            trio = stdin.readline().strip()
    
        if cont == num:
            print(str(verdaderas)+","+str(falsas))
        else:
            print(str(verdaderas)+","+str(falsas))
            print("")


main()
"""
2

10
c 1 5
c 2 7
q 7 1
c 3 9
q 9 6
c 2 5
q 7 5

1
q 1 1
c 1 1
q 1 1


"""
