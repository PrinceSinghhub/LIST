a=[1,2,3,4,5,6]
b=[1,2,3,4,5]
c=[1,2,3,4]
d=[]
for i in range (len(b)):
    d.append(a[i]+b[i])
print(d)
for j in range (len(b),len(a)):
    d.append(a[j])
print(d)
y=[]
for k in range (len(c)):
    y.append((d[k]+c[k]))
print(y)
for l in range (len(c),len(d)):
    y.append(d[l])
print('the sum of 3 list is ',y)