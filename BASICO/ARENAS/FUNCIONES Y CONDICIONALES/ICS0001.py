from sys import stdin
def gif(y, x):
    r = (y*8) / 5
    z = x/r
    s = round(z, 2)
    print(str (s) + " " + "images in GIF format can be stored")
def op(x, y):
    o = (y*24)/25
    r = x/o
    p = round(r, 2)
    print(str (p) + " " + "images in JPEG format can be stored")

def op_1(x, y):
    t = (y*24)/8
    u = x/t
    e = round(u, 2)
    print(str (e) + " " + "images in PNG format can be stored")
    
def op_2(x, y):
    l = (y*48)
    a = x/l
    q = round(a, 2)
    print(str (q) + " " + "images in TIFF format can be stored")

def main():
    num, var, r = stdin.readline().strip().split()
    y = float(num) * float(var)
    x = float(r)*1000000000
    gif(y, x)
    op(x, y)
    op_1(x, y)
    op_2(x, y)

main()
