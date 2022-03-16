from sys import stdin

def change(i,j):
    global memo,den

    if memo[i][j]==None:
        if i==0:res=1
        elif j==0:res=0
        elif i>=den[j]:res=change(i-den[j],j)+change(i,j-1)
        else:res = change(i,j-1)
        memo[i][j]=res
    return memo[i][j]

def main():
    global memo,den
    den = [0,1,5,10,25,50]
    memo = [[None]*len(den) for i in range(7500)]
    while True:
        line= stdin.readline().strip()
        if line=='':break
        n = int(line)
        print(change(n,len(den)-1))

main()
