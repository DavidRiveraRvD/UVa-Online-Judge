from  collections import *
from sys import stdin
parent=[]



def bfs(G,s,t,parent):
    N = len(G)
    visited=[False for  (x) in range(N)]
    cola=deque()
    visited[s]=True
    cola.append(s)
    while cola:
        u=cola.popleft()
        for i in range (N):
            if visited[i]==False and G[u][i]>0:
                visited[i]=True
                cola.append(i)
                parent[i]=u
    if visited[t]==True:
        return True
    else:
        return False
    
def MAX_FLOW(G,s,t):
    global parent
    maxflow=0
    u,v=0,0
    GR=G
    while bfs(GR,s,t,parent):
        pathflow=float("inf")
        v=t
        while v!=s:
            u=parent[v]
            pathflow=min(pathflow,GR[u][v])
            v=parent[v]
        v=t
        while v!=s:
            u=parent[v]
            GR[u][v]-=pathflow
            GR[v][u]+=pathflow
            v=parent[v]
        maxflow+=pathflow
    return maxflow
 
def main():
    global parent
    n, m, s, v = map(int, stdin.readline().strip().split(" "))
    matriz = [[0 for i in range(n+2)] for j in range(m+2)]
    dlimite = (v*s)
    gophers = []
    agujeros = []

    """Ciclo para recibir las posiciones de Gophers"""
    for i in range(n):
        x, y = map(float, stdin.readline().strip().split(" "))
        gophers.append([x, y])
        
    """Ciclo para recibir las posiciones de Agujeros"""
    for j in range(m):
        x, y = map(float, stdin.readline().strip().split(" "))
        agujeros.append([x, y])

    """Ciclo anidado para crear matriz-grafo y evaluadora de las conexiones entre Ghopers y Agujeros"""
    for i in range(n):
        for j in range(m):
            dista = (((gophers[i][0]-agujeros[j][0])**2)+((gophers[i][1]-agujeros[j][1])**2))**0.5
            if dista >dlimite:
                pass
            else:
                matriz[i+1][j+1] =  1

    """Source"""
    for i in range(len(matriz)):
        matriz[i][0] = 1
    """Target"""
    for i in range(len(matriz)):
        matriz[i][-1] = 1
                
    """Ciclo para imprimir matriz"""
    for z in matriz: print(z)

    """Total de hucos(m) - Flujo"""  
main()


"""
def graph():
    ngopher, nhuecos, time, velo = [float(x) for x in stdin.readline().strip().split()]
    mat = [[0 for x in range(int(nhuecos)+1)]for j in range(int(ngopher)+1)]
    cgopher = []
    chuecos = []
    distance = time*velo
    for f in range(len(mat)):
        mat[f][0]=1
    for j in range(len(mat[0])):
        mat[-1][j]=1
    for i in mat:
        print(i)
    print()
    for j in range(int(ngopher)):
        temp = [float(x) for x in stdin.readline().strip().split()]
        cgopher.append(temp)
    for j in range(int(nhuecos)):
        tem = [float(x) for x in stdin.readline().strip().split()]
        chuecos.append(tem)
    for j in range(int(ngopher)):
        for y in range(int(nhuecos)):
            dis = sqrt((cgopher[j][0]-chuecos[y][0])**2+(cgopher[j][1]-chuecos[y][1])**2)
            if dis<=distance:
                mat[j][y+1]=1
    for i in mat:
        print(i)

    print()
    global parent
    parent=[-1 for i in range(int(ngopher)+1)]
    print(MAX_FLOW(mat,0,ngopher))
    for i in mat:
        print(i)
graph()
"""
