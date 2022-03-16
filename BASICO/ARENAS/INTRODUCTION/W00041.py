from sys import stdin
def main():
    var = stdin.readline()
    a = int(var[0])
    b = int(var[1])
    c = int(var[2])
    d = int(var[3])
    if a>=b and a>=c and a>=d :
        print(a)
    elif b>=a and c<=b and d<=b:
        print(b)
    elif b<=c and a<=c and d<=c:
        print(c)
    else:
        print(d)
main()
