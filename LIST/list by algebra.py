x = []
y = []
z = []
x1 = []
z1 = []

for i in range(4):
    n = input("Enter your name =")

    x.append(n)
    m = int(input("Enter your adhar number = "))
    x.append(m)

    o = input("Enter your mobile number")
    while (1 > 0):
        if (len(o) == 10):
            x.append(o)
            break
        else:
            o = input("Enter your number")
    print(x)
    break

for i in range(4):
    n = input("Enter your name =")

    y.append(n)
    m = int(input("Enter your adhar number = "))
    y.append(m)

    o = input("Enter your mobile number")
    while (1 > 0):
        if (len(o) == 10):
            y.append(o)
            break
        else:
            o = input("Enter your number")
    print(y)
    break

for i in range(4):
    n = input("Enter your name =")

    z.append(n)
    m = int(input("Enter your adhar number = "))
    z.append(m)

    o = input("Enter your mobile number")
    while (1 > 0):
        if (len(o) == 10):
            z.append(o)
            break
        else:
            o = input("Enter your number")
    print(z)

    break

for i in range(4):
    n = input("Enter your name =")

    x1.append(n)
    m = int(input("Enter your adhar number = "))
    x1.append(m)

    o = input("Enter your mobile number")
    while (1 > 0):
        if (len(o) == 10):
            x1.append(o)
            break
        else:
            o = input("Enter your number")
    print(x1)

    break

for i in range(4):
    n = input("Enter your name =")

    z1.append(n)
    m = int(input("Enter your adhar number = "))
    z1.append(m)

    o = input("Enter your mobile number")
    while (1 > 0):
        if (len(o) == 10):
            z1.append(o)
            break
        else:
            o = input("Enter your number")
    print(z1)
    break

d = 0
t = []
for i in range(3):
    t.append(x[d])
    t.append(y[d])
    t.append(z[d])
    t.append(x1[d])
    t.append(z1[d])
    break
print("======list given by user======")
print()
print(x)
print(y)
print(z)
print(x1)
print(z1)
print()
a = sorted(t)
print("======After sorting ======")
print()

if a[0] == x[0]:
    print(x)
elif a[0] == y[0]:
    print(y)
elif a[0] == z[0]:
    print(z)
elif a[0] == x1[0]:
    print(x1)
elif a[0] == z1[0]:
    print(z1)

if a[1] == x[0]:
    print(x)
elif a[1] == y[0]:
    print(y)
elif a[1] == z[0]:
    print(z)
elif a[1] == x1[0]:
    print(x1)
elif a[1] == z1[0]:
    print(z1)

if a[2] == x[0]:
    print(x)
elif a[2] == y[0]:
    print(y)
elif a[2] == z[0]:
    print(z)
elif a[2] == x1[0]:
    print(x1)
elif a[2] == z1[0]:
    print(z1)

if a[3] == x[0]:
    print(x)
elif a[3] == y[0]:
    print(y)
elif a[3] == z[0]:
    print(z)
elif a[3] == x1[0]:
    print(x1)
elif a[3] == z1[0]:
    print(z1)

if a[4] == x[0]:
    print(x)
elif a[4] == y[0]:
    print(y)
elif a[4] == z[0]:
    print(z)
elif a[4] == x1[0]:
    print(x1)
elif a[4] == z1[0]:
    print(z1)











