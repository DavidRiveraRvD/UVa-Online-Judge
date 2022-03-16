from sys import stdin
class Heap:

    class_name = 'HEAP'
    
    def __init__(self, data):
        self.data=[int(i) for i in stdin.readline().strip().split()]
        self.lenght=len(self.data)

    def parent(self, i):
        return i//2

    def left(self, i):
        return i*2

    def right(self, i):
        return i*2+1

    def max_heapify(self, i):
        L=self.left(i)
        R=self.right(i)
        if L<= len(self.data)-1 and self.data[L]>self.data[i]:
            largest=L
        else: largest=i
        if R<=len(self.data)-1 and self.data[R]>self.data[largest]:
            largest=R
        if largest!=i:
            self.data[i],self.data[largest]=self.data[largest],self.data[i]
            self.max_heapify(largest)
            
    def build_max_heap(self):
        for j in range((len(self.data)//2),-1,-1):
            self.max_heapify(j)

    def heapsort(self):
        self.build_max_heap()
        lista=[]

        self.data[0],self.data[-1]=self.data[-1],self.data[0]
        num= self.data.pop()
        self.max_heapify(1)
        return [self.data,num]
        
class PriorityQueue(Heap):
        
    def heap_maximum(self):
        return self.data[0]

    def heap_extract_max(self):
        if len(self.data)<1:
            return ('Impossible')
        Max=self.data[0]
        self.data[0]=self.data[len(self.data)-1]
        self.max_heapify(1)
        return Max
        
    def heap_increase_key(self, i, key):
        if key<self.data[i]: return 'algo'
        self.data[i]=key
        while i>1 and self.data[self.parent(i)]<self.data[i]:
            self.data[i],self.data[self.parent(i)]=self.data[self.parent(i)],self.data[i]
            i= self.parent(i)

    def max_heap_insert(self, key):
        self.data[len(self.data)-1]=float('-inf')
        self.heap_increase_key(len(self.data)-1,key)

self=PriorityQueue(8)
self.build_max_heap()
print(self.data)
print('maximo valor:',self.heap_maximum())
self.max_heap_insert(0)
print(self.data)
for i in range(len(self.data)-1):
    self.data,num=self.heapsort()
    print(num,end=' ')
