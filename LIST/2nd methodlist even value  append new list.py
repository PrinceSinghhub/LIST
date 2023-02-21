n=[]
m=int(input("enter the number"))
for i in range(2,m):
    if i%2==0:
        n.append(i)
print(n)

#second method

print(list(range(1,30,3)))