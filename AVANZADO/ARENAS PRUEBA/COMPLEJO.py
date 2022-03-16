class Complejo:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def suma(self, x):
        r = self.r+x.r
        i = self.i+x.i
        return Complejo(r,i)
def suma_complex(a, b):
    r = a.r + b.r
    i = a.i +b.i
    return Complejo(r, i)

x = Complejo(5, -2)
y = Complejo(7, -2)
print(x.r, x.i)
print(y.r, y.i)
z = x.suma(y)
print(z.r, z.i)
W = suma_complex(x, y)
print(W.r, W.i)
