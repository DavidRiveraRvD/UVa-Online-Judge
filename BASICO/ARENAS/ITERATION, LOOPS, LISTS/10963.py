from sys import stdin




def main():
    n = int(stdin.readline())
    while n != 0 :
        n -= 1
        lista = []
        d = True
        space = stdin.readline().strip()
        x = int(stdin.readline())
        while x != 0:
            x -=1
            num, num_2 = map(int, stdin.readline().strip().split())
            result = num_2 - num
            lista.append(result)
        for i in lista:
            if i != lista[0]:
                d = False
            
        if n>0:
            if d == False:
                print("no\n")
            else:
                print("yes\n")
        else:
            if d == False:
                print("no")
            else:
                print("yes")
main()
