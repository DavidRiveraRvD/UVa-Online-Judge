from sys import stdin

def main():
    pri = stdin.readline().strip().split()    
    while len(pri) != 0:
        num, cad = int(pri[0]), pri[1]
        num2, cad2 = stdin.readline().strip().split()
        num2 = int(num2)
        memo = [[0 for x in range(num+1)] for y in range(num2+1)]

     
        for j in range(num+1):
            memo[0][j]=j*1  
        for i in range(num2+1):
            memo[i][0] = i*1
       
        for x in range(1, num2+1):
            for z in range(1, num+1):                
                if cad2[x-1] != cad[z-1]:
                    memo[x][z] = min(1+memo[x][z-1], 1+memo[x-1][z], 1+memo[x-1][z-1])
                elif cad2[x-1] == cad[z-1]:
                    memo[x][z]=memo[x-1][z-1]
        for i in memo:
            print(*i)
        print(memo[num2][num])
        pri = stdin.readline().strip().split()
                    
main()
        
        
