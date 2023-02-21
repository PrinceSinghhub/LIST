r=int(input("Enter no of Rows"))
c=int(input("Enter a Collum"))
matrix=[]
for i in range (r):
    a=[]
    for j in range(c):
        n=int(input("Enter no"))
        a.append(n)
    matrix.append(a)
for i in range (r):
    for j in range (c):
        print(matrix[i][j],end=" ")
    print()
        
