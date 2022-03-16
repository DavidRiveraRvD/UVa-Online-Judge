from sys import stdin

def oprador(r, s, t):
    if int(s) > 5:
        print(int(r)*s)
    else:
        print(int(t)*s)
        


def main():
    var = stdin.readline()
    y = int(((((((((int(var))*567))/9)+7492)*235)/47)-498))
    y = str(y) 
    r = (y[-3])
    s = (y[-2])
    t = (y[-1])
    oprador(r, s, t)
    
main()
