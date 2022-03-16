from sys import stdin
 
def main():
    while True:        
        global A, B
        A = stdin.readline().strip()
        if A == "":
            break
        B = stdin.readline().strip()
        memo = [[0 for aa in range(0,len(B)+1)]for tt in range(len(A)+1)]

        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    memo[i][j] = 1+memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        print(memo[len(A)][len(B)])
main()
   
