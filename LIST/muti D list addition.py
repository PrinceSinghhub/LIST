a=[1,2,3,4,5,10,20,3,0],[20,30,40]
b=[6,7,8]
c=[]
for i in range (0,len(b)):

    c.append(a[i]+b[i])
print(c)

for j in range (len(b),len(a)):
    v=a[j]
    c.append(v)
print(c)