from sys import stdin
def homer(m, n, t):
    mat = [0 for i in range(0, t+1)]

    if (t>=n or t>=m) and t>0:
        larg = 0
        mat[0] = 0
        con = 1

        for i in range(1, t+1):
            mat [i]= -1
            if i >=m and mat[i-m]>=0:
                mat[i] = mat[i-m]+1
            if i>=n and mat[i-n]>=0:
                mat[i] = max(mat[i-n]+1, mat[i])

        if mat[t]>=0:
            print(mat[t])
        else:
            c = 1
            while mat[t-c]==-1:
                c+=1
            print(mat[t-c], c)
    else:
        print(0, t)
    
def main():
    ining = stdin.readline().strip()
    while ining != "":
        m, n, t = [int(x) for x in ining.split()]
        homer(m, n, t)
        ining = stdin.readline().strip()
main()


        
