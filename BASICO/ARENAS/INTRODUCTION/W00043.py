from sys import stdin
op = stdin.readline().strip()
x = float(stdin.readline())
y = float(stdin.readline())

def main():
    
    if op == "/" and y != 0:
        print (round((x/y),2))
    elif op == "+":
        print (round((x+y),2))
    elif op == "*":
        print (round((x*y),2))
    elif op == "-":
        print (round((x-y),2))
    elif op == "MOD" and y !=0 :
        print (round((x%y),2))
    elif op == "DIV" and y !=0:
        print (round((x//y),2))
    else:
        print("Imposible Dividir Por Zero")
main()
