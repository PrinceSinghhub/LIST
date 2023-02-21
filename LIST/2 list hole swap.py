n=[1,2,3,4,5,6,7,8,9]
n1=[10,22,33,42,56]
b=len(n1)
c=[]
for i in range(len(n)):
    c.append(n[i])
for i in range(b,len(n)):
    n.pop(-1)
# indexing si element pop nhi hoga kyuiki element km ho rha hai and go to out of index
# print(n)
for i in range (len(n)):
    n[i]=n1[i]
for i in range (len(n1)):
    n1[i]=c[i]
for i in range (len(n1),len(c)):
    n1.append(c[i])
print(n)
print(n1)

