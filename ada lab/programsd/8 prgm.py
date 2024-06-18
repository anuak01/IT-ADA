#8 prgm
INF=9999
def printsolution(V,D):
    print("The All Pair Shortest Path:")
    for i in range(V):
        for j in range(V):
            if D[i][j]==INF:
                print("%7s"%"INF",end="")
            else:
                print("%7d"%D[i][j],end="")
        print()
        
        
def floyd(V,C):
    D=[[0]*V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            D[i][j]=C[i][j]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][j]>(D[i][k]+D[k][j]):
                    D[i][j]=D[i][k]+D[k][j]
    printsolution(V,D)
    
V=int(input("Enter the number of vertices:"))
C=[[0]*V for _ in range(V)]
print("Enter the cost matrix:")
print("Enter 9999 for Infinity")
print("Enter 0 for cost(i,i)")
for i in range(V):
    C[i]=list(map(int,input().split()))
floyd(V,C)