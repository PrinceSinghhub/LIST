list1=[]
list2=[]
n=int(input("Enter a range"))
for i in range (n):
    a=int(input("Enter a number"))
    list1.append(a)
for num in list1:
    if num%2!=0:
        list2.append(num)
print(list2)
        
 
