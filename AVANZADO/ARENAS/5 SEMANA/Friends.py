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
    for i in range(num):
        var =int(stdin.readline().strip())
        lista = {}
        for j in range(var):
            a, b = stdin.readline().strip().split(" ")
            if a not in lista:
                var1= aset()
                lista[a]=var1
            else:
                var1=lista[a]
                
            if b not in lista:
                var2 = aset()
                lista[b]=var2
            else:
                var2 = lista[b]
            #print(findset(var1)==findset(var2))
            union(var1, var2)
            #print(findset(var1)==findset(var2))
            z = findset(var1)
            print(z.con)
main()
