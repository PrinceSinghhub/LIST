a=[1,0,3,4,6]
print(max(a),min(a))
#string convert in list
a="prince is a coder"
s=a.split()
print(s)

a="prince;singh;coder"
b=a.split(";")
print(b)

a=[1,0,3,4,6]
n=int(input("Enter your number"))
if n in a:
    print("yes")