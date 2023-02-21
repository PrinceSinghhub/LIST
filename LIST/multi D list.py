a=[[1,2,3,4,5],[6,7,8,9,10],[2,3,4]]
b=[[11,12,13,14,15],[16,17,18,19,20],[1,2,3]]
c=[1,2,3,4,5]
d=[6,7,8,9,10]
g=[]
h=[]
for i in range (len(c)):
    g.append(c[i]+d[i])
print(g)
for i in range (len(a)):
    for j in range (len(b[2])):
        h.append(a[i][j]+b[i][j])
print(h)
