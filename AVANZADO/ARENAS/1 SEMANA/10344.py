from sys import stdin

def mult(data,b,c):
    if b== len(data):
        return (c)
        b=1
    elif mult(data,b+1,c+data[b])==23:
        return (23)
        b=1
    elif mult(data,b+1,c-data[b])==23:
        return (23)
        b=1
    elif mult(data,b+1,c*data[b])==23:
        return "Possible"
    else:
        return "Impossible"

def main():
    data = [int(x) for x in stdin.readline().strip().split()]
    b=1
    c=int(data[0])
    d=int(data[1])
    print(mult(data,b,c))
main()
    
        
        
