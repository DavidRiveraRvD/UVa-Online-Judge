import sys

class Node:

    def __init__(self, x):
        self.x = x
        self.seg = None
        self.previa = None
        self.head = 0
        self.cola = 0
        self.data = [0 for h in range(0, x)]
        self.arriba = 0
        self.data = [0 for g in range(0, x)]
        
        """self.key = key
        self.prev = None
        self.next = None"""
    def __str__(self):
        return str(self.key)

class Lista(Node):
    def __init__ (self, x):
        Node.__init__(self, x)

    def push(self,x):
        if self.arriba < len(self.data): 
            self.data[self.arriba] = x
            self.arriba = self.arriba + 1
        else:
            raise NameError("Fuera de rango")

    def stack_empty(self):
        if self.arriba != 0:
            return False
        elif self.arriba == 0:
            return True
##"""def key(self):
##for j in range(1, len(self.x)-1):
##    print(self.x[j])
##    
##def previa(self):
##for i in range(1, len(self.x)-1):
##    print("KEY ANTES", self.x[i], "===", self.x[i-1])
##
##def segu(self):
##for z in range(1, len(self.x)-2):
##    print("KEY DESPUES", self.x[z], "===", self.x[i+1])
##
##def push(self, x):
##self.elemento = x
##sefl.x[-1] = str(self.element)
##self.x.append(0)
        
    def pop(self):
        if self.stack_empty():
            raise NameError('Pila vacia')
        else:
            self.arriba = self.arriba - 1
            return self.data[self.arriba]
        
    def enqueue(self, x):
        self.data[self.cola] = x
        if self.cola == len(self.data):
            self.cola= 1
        else:
            self.cola+=1

    def dequeue(self):
        x = self.data[self.head]
        if self.head == len(self.data):
            self.head = 1
        else:
            self.head+=1
        return x

print("Enqueue")
En = Lista(4)
print(*En.data)
En.enqueue(15)
print(*En.data)
En.enqueue(1)
print(*En.data)
En.enqueue(5)
print(*En.data)
print("*-*"*15)


print("Dequeue")
print(En.dequeue(), En.data)
print(En.dequeue(), En.data)
print(En.dequeue(), En.data)
print(En.dequeue(), En.data)
print("*-*"*15)



print("Push")
n = 4
S = Lista(5)
for j in range(1, n+1):
    S.push(j)
    print(*S.data)
print("\n", *S.data)
print("*-*"*15)




print("Pop")
num = 9
P = Lista(num)
for z in range(0, num):
    P.push(z)
for t in range(0,num):
    P.pop()
    print(P.arriba)
print("*-*"*15)

m = 9
s = Lista(9)
for y in range(0, 10):
    s.push(y)
print(s.data)        
    

##
##def pop(self):
##"""raise Exception('Not implemented yet')"""
##self.x.pop(len(self.x)-2)
##def enqueue(self, x):
##"""raise Exception('Not implemented yet')"""
##self.x.insert(1,str(x))
##
##def dequeue(self):
##"""raise Exception('Not implemented yet')"""
##self.x.pop(1)
##
##lista = []
##"""Donde ingresara el numero de elementos y los elementos a insertar"""
##num = int(sys.stdin.readline().strip())
##for i in range(num-1):
##elemento = sys.stdin.readline().strip()
##lista.append(elemento)
##lista.append(0)
##nodos = Node(lista)
##"""class List:
##
##def __init__(self):
##raise Exception('Not implemented yet')
##
##def push(self, x):
##raise Exception('Not implemented yet')
##
##def pop(self):
##raise Exception('Not implemented yet')



