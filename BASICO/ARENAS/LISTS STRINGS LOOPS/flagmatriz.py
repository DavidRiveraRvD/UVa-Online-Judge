from  sys import stdin

def main():
    n=int(stdin.readline())
    while n>=4:
        for t in range(n):
            if t<n-1: print(1,end=' ')
            else: print(1)
        num=1
        for k in range(n-1):
            print(1,end=' ')
            for w in range(n-2):
                num-=1
                if num<=1:
                    num=n-1
                print(num,end=' ')
            print(1)
            num=n-(k+1)
        for t in range(n):
            if t<n-1: print(1,end=' ')
            else: print(1)
        n=int(stdin.readline())
        if n>=4: print()
main()
